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
		self.special_rule = {}
		self.special_rule['N::Group'] = {}
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
			head = line.split(':')[0]
			body = ':'.join(line.split(':')[1:]).strip()
			if not head or not body:
				raise
			name = head
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

			#'$classname: Object'
			if ruleName[0]=='$':
				groupName = ruleName[1:]
				idName = ruleBody
				self.definationContext.groupID(ruleName[1:], idName)
				#print('parseDefination scope: %s' % str(self.cxt.getCurrentScope()))
			
			#sprcial rule: create group reference
			for token in ruleSyntax:
				if token.startswith('$N:'):
					cmd, opts = self.analyze(token)
					if opts[1]:
						if opts[1] not in self.special_rule['N::Group'].keys():
							self.special_rule['N::Group'][opts[1]] = []
						self.special_rule['N::Group'][opts[1]].append(ruleId)
		self.newRuntime()

	def newRuntime(self):
		self.cxt = Context(cxt=self.definationContext)

	def analyze(self, cmdText):
		l = cmdText.split(':')
		cmd = l[0]
		options = [] if len(l)==1 else l[1:]
		options.extend([None, None, None, None])
		return cmd, options

	def chooseSyntax(self, syntaxIds, syntaxStack=[]):
		return Helper.choice(syntaxIds)

	def get_syntaxids_by_N_group_name(self, group_name):
		return self.special_rule['N::Group'][group_name]

	def get_dependences(self, rule_tokens):
		dependence = []
		for token in rule_tokens:
			if not token.startswith('$R:'):
				continue
			cmd, opts = self.analyze(token)
			if not opts[1]:
				continue
			if opts[1] in dependence:
				continue
			if self.cxt.getGroupIDs(opts[1]):
				continue
			dependence.append(opts[1])
		return dependence

	def resolve_dependence(self, dependence):
		syn_ids = self.get_syntaxids_by_N_group_name(dependence)
		syn_id = self.chooseSyntax(syn_ids)
		rule = self.rules[syn_id]
		#print('[expandRuleName] rule:%s' % str(rule))
		tokens = rule['syntax']
		
		prologues, statement = self.expandRuleTokens(tokens, ruleName='[dependence]')
		return prologues, statement

	def expandRuleTokens(self, ruleTokens, ruleName='', check_dependence=True):
		logger.debug('expandRuleTokens: ruleName %s ruleTokens: %s' % (ruleName, str(ruleTokens)))
		prologues = []
		deps = self.get_dependences(ruleTokens)
		for dep in deps:
			pstmts, stmt = self.resolve_dependence(dep)
			prologues.extend(pstmts)
			prologues.append(stmt)
			# debug print
			#print('resolve dependence:')
			#for p in pstmts:
			#	print('resolve dependence: %s' % p)
			#print('resolve dependence: %s' % stmt)
		self.cxt.RuleEnter(ruleName=ruleName, ruleTokens=ruleTokens)
		texts = []
		#self.cxt.rule_enter()
		for token in ruleTokens:
			pstmts = []
			text = token
			if token[0]=='@':
				pstmts, text = self.expandRuleName(token)
			elif token[0]=='$':
				try:
					child_tokens = self.cxt.parse(token)
				except Exception as e:
					print('parse error ruleName: %s' % ruleName)
					print('parse error tokens: %s' % str(ruleTokens))
					print('parse error token: %s' % str(token))
					logger.exception('parse error:')
					raise(e)
				pstmts, text = self.expandRuleTokens(child_tokens, ruleName='[anonymous]')
			prologues.extend(pstmts)
			texts.append(text)
		#self.cxt.rule_exit()
		self.cxt.RuleExit()
		#print('---- texts ----')
		#print(texts)
		#print('---------------')
		statement = ''.join(texts)
		#print('expandRuleTokens return prologues: %s' % str(prologues))
		return prologues, statement

	def expandRuleName(self, ruleName):
		logger.debug('expandRuleName ruleName:%s' % ruleName)
		#print(self.defination.keys())
		#if ruleName in self.defination.keys():
		#	print('rule name [%s] found!' % ruleName)
		#else:
		#	print('rule name [%s] not found!' % ruleName)
		assert ruleName in self.defination.keys(), 'ruleName "%s" is undefined' % ruleName
		syntaxIds = self.defination[ruleName]
		syntaxId = self.chooseSyntax(syntaxIds)
		#print('[expandRuleName] syntaxId:%d' % syntaxId)
		rule = self.rules[syntaxId]
		#print('[expandRuleName] rule:%s' % str(rule))
		tokens = rule['syntax']
		
		prologues, statements = self.expandRuleTokens(tokens, ruleName=ruleName)
		return prologues, statements

	def safeExpandRuleName(self, ruleName):
		try:
			return self.expandRuleName(ruleName)
		except Exception as e:
			logger.error('safeExpandRuleName %s' % e)
			raise(e)
		return []
