import os, sys
import time
import json
import re
import math
import copy
import logging

from . import Config
from .RuleContext import Context
from . import Crasher
from . import Notifier
from . import Helper

logger = logging.getLogger(__name__)

class Ruler(object):
	"""docstring for Ruler"""
	def __init__(self):
		self.defination = {} # {"name": [ruleid, ]}
		self.rules = [] # [ {"name": "xxx", "ruleid": ruleid, "syntax": []}, ]
		self.MAX_DEPTH = 32
		self.definationContext = None
		self.cxt = None
		self.reSplit = re.compile(r"([@\$][:\w_]+|[@\$]\.\.\.[\w_]*|\$[{}])")

	def split(self, text):
		return [part for part in self.reSplit.split(text) if part !='']

	def loadfile(self, file):
		contents = []
		with open(file, 'r') as fr:
			lines = fr.readlines()
			for line in lines:
				line = re.sub('#.*$', '', line)
				line = line.strip()
				if line:
					contents.append(line)
		#print(contents)
		self.parseDefination(contents)

	def showDefination(self):
		for ruleName,ruleIds in self.defination.items():
			print(ruleName + ':')
			for ruleId in ruleIds:
				print('  ' + ''.join(self.rules[ruleId]['syntax']))
	
	def parseDefinationLine(self, line):
		if not line:
			print('[parseDefinationLine] %s' % line)
			raise Exception("defination line is empty")
		try:
			name = line.split(':')[0]
			body = ':'.join(line.split(':')[1:]).strip()
			if not name or not body:
				raise
		except Exception as e:
			print('[parseDefinationLine] %s' % line)
			raise Exception("defination line invalid")
		return name, body

	def parseDefination(self, contents):
		self.definationContext = Context()		
		for line in contents:
			ruleName, ruleBody = self.parseDefinationLine(line)
			ruleSyntax = self.split(ruleBody)
			ruleId = len(self.rules)
			rule = {'name': ruleName, 'id': ruleId, 'syntax': ruleSyntax}
			self.rules.append(rule)
			if ruleName not in self.defination.keys():
				self.defination[ruleName] = []
			self.defination[ruleName].append(ruleId)
			if ruleName[0]=='$':
				groupName = ruleName[1:]
				idName = ruleBody
				self.definationContext.groupID(ruleName[1:], idName)
				#print('parseDefination scope: %s' % str(self.cxt.getCurrentScope()))
		self.newRuntime()

	def newRuntime(self):
		self.cxt = Context(cxt=self.definationContext)

	def chooseSyntax(self, syntaxIds, syntaxStack=[]):
		return Helper.choice(syntaxIds)

	def expandRuleTokens(self, ruleTokens, ruleName=''):
		logger.debug('expandRuleTokens: ruleName %s ruleTokens: %s' % (ruleName, str(ruleTokens)))
		self.cxt.RuleEnter(ruleName=ruleName, ruleTokens=ruleTokens)
		texts = []
		#self.cxt.rule_enter()
		for token in ruleTokens:
			text = token
			if token=='@BuiltInFunction':
				# hack...
				text = self.expandRuleName(token)
				ptext = self.expandRuleTokens(['$...'], ruleName='[BuiltInFunction Arguments]')
				text = '%s(%s)' % (text, ptext)
			elif token[0]=='@':
				text = self.expandRuleName(token)
			elif token[0]=='$':
				try:
					child_tokens = self.cxt.parse(token)
				except Exception as e:
					print('parse error ruleName: %s' % ruleName)
					print('parse error tokens: %s' % str(ruleTokens))
					print('parse error token: %s' % str(token))
					logger.exception('parse error:')
					#raise e
					child_tokens = ['this']

					
				text = self.expandRuleTokens(child_tokens, ruleName='[anonymous]')
			texts.append(text)
		#self.cxt.rule_exit()
		self.cxt.RuleExit()
		return ''.join(texts)

	def expandRuleName(self, ruleName):
		logger.debug('expandRuleName ruleName:%s' % ruleName)
		#print(self.defination.keys())
		assert ruleName in self.defination.keys(), 'ruleName %s undefined' % ruleName
		syntaxIds = self.defination[ruleName]
		syntaxId = self.chooseSyntax(syntaxIds)
		#print('[expandRuleName] syntaxId:%d' % syntaxId)
		rule = self.rules[syntaxId]
		#print('[expandRuleName] rule:%s' % str(rule))
		tokens = rule['syntax']
		
		return self.expandRuleTokens(tokens, ruleName=ruleName)

	def safeExpandRuleName(self, ruleName):
		try:
			return self.expandRuleName(ruleName)
		except Exception as e:
			pass
		return ''
