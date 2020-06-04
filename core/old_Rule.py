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

TOKEN_TYPE_TEXT = 0
TOKEN_TYPE_RULE = 1
TOKEN_TYPE_SYS  = 2

"""
token:
{
	'type': 0,
	'value': '',
	'attr': {}
}
"""

"""
rule:
{
	'name': 'rule_name',
	'attr': {},
	'text': '',
	'id': 0,
	'tokens': [ token ],
	'location':{'file': 'rule_file', 'line': 0}
}
"""

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
		self.reSplit = re.compile(r"(<.+>)")

	def tokenize(self, text):
		tokens = []
		parts = self.re_token.split(text)
		for part in parts:
			if not part:
				continue
			token = {'type': -1, 'value': None, 'attr': {}}
			if part[0]=='<' and part[-1]=='>':
				attrs = [attr for attr in part[1:-1].split(' ') if attr!='']
				value = attr[0]
				if value[0] == '@':
					token['type'] = TOKEN_TYPE_SYS
				else:
					token['type'] = TOKEN_TYPE_RULE

				for attr in attrs[1:]:
					n, v = attr.split('=')
					token['attr'][n] = v
			else:
				token['type'] = TOKEN_TYPE_TEXT

	def parse_rule(self, text):
		head, body = text.split(':')
		head_tokens = self.tokenize(head.strip())
		body_tokens = self.tokenize(body.strip())
		if len(head_tokens)!=1 or len(body_tokens)==0:
			logger.debug('rulerize failed at\n\t%s' % text)

		rule = {
			'name': head_tokens['value'],
			'attr': head_tokens['attr'],
			'text': text,
			'id': -1,
			'tokens': body_tokens,
			'location':{'file': None, 'line': -1}
		}

		return rule

	def load_file(self, file):
		with open(file, 'r') as fr:
			lines = fr.readlines()
			for line in lines:
				line = re.sub('#.*$', '', line)
				line = line.strip()
				if not line:
					continue
				rule = self.parse_rule(line)
				rid = len(self.rules)
				rule['id'] = rid
				self.rules.append(rule)
				if rule['name'] not in self.defination.keys():
					self.defination[rule['name']] != []
				self.defination[rule['name']].append(rule)

				# [TODO] static semantic parse

	# [TODO: rewrite]
	def show_rules(self):
		for rname,rids in self.defination.items():
			for rid in rids:
				print(self.rules[rid]['text'])

	# [TODO: delete]
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
