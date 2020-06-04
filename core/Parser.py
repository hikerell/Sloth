import os, sys
import time
import json
import re
import math
import copy
import logging

from . import Config
from .Ruler import Context
from . import Helper

logger = logging.getLogger(__name__)

class Parser(object):
	"""docstring for Parser"""
	def __init__(self):
		self.defination = {} # {"name": [ruleid, ]}
		self.rules = [] # [ {"name": "xxx", "ruleid": ruleid, "syntax": []}, ]
		self.special_rule = {}
		self.special_rule['N::Group'] = {}
		self.MAX_DEPTH = 32
		self.definationContext = None
		self.cxt = None
		self.reSplit = re.compile(r"([@\$][:\w_]+|[@\$]\.\.\.[\w_]*|\$[{}])")

		self.re_rule = re.compile(r'([@$][a-zA-Z][a-zA-Z0-9_]*<[a-zA-Z0-9_=,"\s]*>)')

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

	def parse_line(self, line):
		tokens = self.re_rule.split(line)
		assert(len(tokens)>0)
		if len(tokens)==1:
			pass



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

	def analyze(self, cmdText):
		l = cmdText.split(':')
		cmd = l[0]
		options = [] if len(l)==1 else l[1:]
		options.extend([None, None, None, None])
		return cmd, options

@rule('name', p=1)
def _(ast, cxt):
	""" """
	
if __name__=='__main__':
	p = Parser()
	#p.parse()
	rule = p.parse_line('@AssignExpr: $N() = @RightExpr()')
	print(rule)
