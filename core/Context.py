import copy
import logging

from . import Helper

logger = logging.getLogger(__name__)

class Context(object):
	"""docstring for Context"""
	def __init__(self, cxt=None):
		self.idCount = 0
		self.scopeStack = [ self.newScope() ]
		self.ruleStack = []

		if cxt:
			self.updateContext(cxt)

	def updateContext(self, cxt):
		self.scopeStack = copy.deepcopy(cxt.scopeStack)

	#
	#
	#
	def newRule(self, ruleName, ruleTokens):
		r = {}
		r['name'] = ruleName
		r['syntax'] = ruleTokens
		r['alias'] = {}
		return r

	def getCurrentRule(self):
		return self.ruleStack[-1]

	def RuleEnter(self, ruleName='[anonymous]', ruleTokens=[]):
		r = self.newRule(ruleName, ruleTokens)
		self.ruleStack.append(r)

	def RuleExit(self):
		self.ruleStack.pop()

	def aliasID(self, aliasName, idName):
		r = self.getCurrentRule()
		r['alias'][aliasName] = idName

	def getAliasIDs(self, aliasName):
		r = self.getCurrentRule()
		return r['alias'][aliasName]
	#
	#
	#
	def newScope(self):
		#{ 'LocalIDs':[], 'ParamIDs':[], 'taggedIDs': {}}
		scope = {}
		scope['LocalIDs'] = []
		scope['ParamIDs'] = []
		scope['taggedIDs'] = {}
		scope['taggedIDs']['groups'] = {}
		scope['taggedIDs']['aliases'] = {}
		return scope

	def getCurrentScope(self):
		return self.scopeStack[-1]

	def newIDName(self):
		idName = 'id%d' % self.idCount
		self.idCount += 1
		return idName

	def groupID(self, groupName, idName, scope=None):
		scope = scope if scope else self.getCurrentScope()
		if groupName not in scope['taggedIDs']['groups'].keys():
			scope['taggedIDs']['groups'][groupName] = []
		scope['taggedIDs']['groups'][groupName].append(idName)

	def getGroupIDs(self, groupName):
		ids = []
		for scope in self.scopeStack[-1::-1]:
			if groupName in scope['taggedIDs']['groups'].keys():
				gids = scope['taggedIDs']['groups'][groupName]
				ids.extend(gids)
		return ids

	def setScopeID(self, idName, scope=None, groupName=None, aliasName=None):
		scope = scope if scope else self.getCurrentScope()
		#print('setScopeID scope: %s' % str(scope))
		#print('setScopeID idName: %s' % idName)
		scope['LocalIDs'].append(idName)
		if groupName:
			self.groupID(groupName, idName, scope=scope)
		if aliasName:
			self.aliasID(aliasName, idName)

	def deleteScopeID(self, idName, scope=None):
		scope = scope if scope else self.getCurrentScope()
		if idName in scope['LocalIDs']:
			scope['LocalIDs'].remove(idName)
			return True
		return None

	def getIDsByScope(self, scope):
		ids = []
		ids.extend(scope['LocalIDs'])
		ids.extend(scope['ParamIDs'])
		return ids

	def getCurrentScopeIDs(self):
		return self.getIDsByScope(self.getCurrentScope())

	def getAllIDs(self):
		ids = []
		for scope in self.scopeStack[-1::-1]:
			sids = self.getIDsByScope(scope)
			ids.extend(sids)
		return ids

	def ScopeEnter(self):
		#logger.debug('scope enter ...')
		self.scopeStack.append(self.newScope())

	def ScopeExit(self):
		#logger.debug('scope exit ...')
		scope = self.scopeStack.pop()

	"""
	def getDelayIdentites(self):
		return self.delayids

	def rule_enter(self):
		pass

	def rule_exit(self):
		for fn,args in self.run_at_rule_exit_list:
			fn(args)
		self.run_at_rule_exit_list = []

	def run_at_rule_exit(self, fn, args):
		self.run_at_rule_exit_list.append((fn ,args))

	def fn_id_delay_reference(self, idname):
		print('delay run: idname'+ idname)
		assert(idname in self.delayids)
		self.delayids.remove(idname)
		self.ids.append(idname)
	"""

	def Cmd_NewIdentify(self, options):
		idName = self.newIDName()
		aliasName = options[0] if options and len(options)>0 and options[0] else None
		groupName = options[1] if options and len(options)>1 and options[1] else None
		self.setScopeID(idName, groupName=groupName, aliasName=aliasName)
		return [ idName ]

	def Cmd_ReferenceIdentity(self, options):
		ids = []
		aliasName = options[0] if options and len(options)>0 and options[0] else None
		groupName = options[1] if options and len(options)>1 and options[1] else None
		if groupName:
			ids = self.getGroupIDs(groupName)
		elif aliasName:
			ids = [ self.getAliasIDs(aliasName) ]
		else:
			ids = self.getAllIDs()
		assert len(ids)>0, "not available ids"
		idName = Helper.choice(ids)
		return [ idName ]

	def Cmd_ParameterResolve(self, options):
		#return self.Cmd_ReferenceIdentity(options)
		#return ['@RightHandSideExpression']
		return ['@ParameterExpression']

	def Cmd_MultiParametersResolve(self, options):
		return Helper.choice([[], ['$P'], ['$P', ',', '$P'], ['$P', ',', '$P',',', '$P']])

	def Cmd_DollarCharResolve(self, options):
		return ['$']

	def Cmd_Empty(self, options):
		return []


