import os, sys
import time
import json
import re
import math
import copy
import logging

from . import Config
from . import Crasher
from . import Notifier
from . import Helper

logger = logging.getLogger(__name__)

MAKE_STATE_SUCCESS = 0
MAKE_STATE_FAIL    = 1

class MakerException(Exception):
	pass
		

class Maker(object):
	"""docstring for Maker"""
	def __init__(self, defination, environment):
		self.defination = defination
		self.environment = environment

		# config
		self.MAX_DEPTH = 50

		# rule defination
		self._rules = {}  # self._rules[rid] = rule
		self._weighted_rids = {} # self._weighted_rids[name] = [rid, rid...]
		self._end_rids = [] # end-term rule ids
		self.structure(defination)

		# runtime context
		self.count_Id = 0
		self.scope_stack = None
		self.level = -1
		self._maked_rids = []
		self._maked_names = []

		# buildin environment
		self.builtin = {
			'Type': {},
			'Property': {},
			'Function': {},
		}

		self.hook = {
			'Property': {},
			'Function': {},
			'Argument': {},
		}
		self.initilize(environment)

	def initilize(self, environment):
		"""
		runtime and builtin environment init
		"""
		self.scope_stack = [ ]
		self.scope_enter(tags=['global'])
		for x in environment['Id']:
			self.scope_set_Id(n=x['name'], t=x['type'])

		for t, e in environment['Type'].items():
			self.builtin['Type'][t] = e

		self.builtin['Property'] = environment['Property']
		self.builtin['Function'] = environment['Function']

		self.hook['Property'] = environment['Hook']['Property']
		self.hook['Function'] = environment['Hook']['Function']
		self.hook['Argument'] = environment['Hook']['Argument']

	def structure(self, defination):
		self._rules = {}  # self._rules[rid] = rule
		self._weighted_rids = {} # self._weighted_rids[name] = [rid, rid...]
		self._end_rids = []
		for rname in defination.keys():
			rules = defination[rname]
			for rule in rules:
				rid = rule['id']
				weight =int(rule['w'])
				assert(weight>0)
				self._rules[rid] = rule
				if rname not in self._weighted_rids:
					self._weighted_rids[rname] = []
				self._weighted_rids[rname].extend([rid]*weight)
				if rule['e']:
					self._end_rids.append(rid)

	##########
	#  Debug #
	##########
	def debug_show_scope_stack(self):
		count = 0
		for scope in self.scope_stack:
			prefix = '[D][scope %04d] ' % count
			print(prefix + 'onlylocal: %s' % str(scope['onlylocal']))
			print(prefix + 'tags: %s' % str(scope['tags']))
			print(prefix + 'ids: %s' % str(scope['ids']))
			print(prefix + 'n_t_ids:')
			indent = '[D]' + ' ' * (len(prefix) - 4) + '> '
			for n_t in scope['n_t_ids']:
				print(indent + 'name=%s' % n_t[0] + ' type=%s' % n_t[1])
			print(prefix + 'type:')
			indent = '[D]' + ' ' * (len(prefix) - 4) + '> '
			for tname, tids in scope['type'].items():
				print(indent + 'type=%s' % tname + ' ids: %s' % str(tids))
			count += 1

	def debug_show_AST(self):
		print('[D] ', end='')
		for n in self._maked_names:
			print('@%s' % n, end=' => ')
		print('[CURRENT]')
		for rid in self._maked_rids:
			print('%d' % rid, end=' => ')
		print('[CURRENT]')

		print('[D] Rule Selection:', end='')
		indent = '[D] > '
		idx = 0
		for rid in self._maked_rids:
			name = self._maked_names[idx]
			rule = self.get_rule(rid)
			print(indent + 'rule name @%s select rid %d: %s' % (name, rid, rule['d']))
			idx += 1


	##########
	# Random #
	##########
	def choice(self, objs):
		return Helper.choice(objs)

	def randint(self, s, e):
		return Helper.rnd(s, e)

	##################
	# MakerException #
	##################
	def restart(self, desc='nothing to report'):
		raise(MakerException(desc))
			
	#########
	# Scope #
	#########
	def scope_set_Id(self, n='', t='', scope=None):
		if not scope:
			scope = self.scope_current()
		scope['ids'].append(n)
		if t not in scope['type'].keys():
			scope['type'][t] = []
		scope['type'][t].append(n)
		scope['n_t_ids'].append([n, t])

	def scope_current(self):
		return self.scope_stack[-1]

	def scope_enter(self, tags=[], onlylocal=False):
		scope = {'ids': [], 'type': {}, 'n_t_ids': [], 'tags': tags, 'onlylocal': False}
		self.scope_stack.append(scope)
		#print('[scope] enter ... now total hold scope depth: %d' % len(self.scope_stack))

	def scope_exit(self):
		self.scope_stack.pop()
		#print('[scope] exit  ... now total hold scope depth: %d' % len(self.scope_stack))

	def scope_under(self, s):
		"""
		desc: tag1.tag2.tag3
		current_scope tags should include 'tag3'
		previous_scope tags should include 'tag2'
		previous_previous_scope tags should include 'tag1'
		"""
		tags = s.split('.')
		if len(self.scope_stack)<len(tags):
			return False
		scopes = self.scope_stack[-len(tags):]
		for idx in range(0, len(tags)):
			if not tags[idx] in scopes[idx]['tags']:
				return False
		return True
		
	#########
	#  Id   #
	#########
	def new_Id(self):
		n = 'id%s' % self.count_Id
		self.count_Id += 1
		return n

	def ref_Id(self, t=''):
		n_t_ids = []
		for scope in reversed(self.scope_stack):
			n_t_ids.extend(scope['n_t_ids'])
			if scope['onlylocal']:
				break

		if len(n_t_ids)==0:
			raise(MakerException('no available ids'+' for type %s'%t if not t else ''))
		
		if not t:
			return Helper.choice(n_t_ids)[0]

		ids = [x[0] for x in n_t_ids if x[1]==t]

		if len(ids)==0:
			raise(MakerException('no available ids'+' for type %s'%t if not t else ''))
		return Helper.choice(ids)

	##################################################
	#
	##################################################
	def rule_under(self, s):
		names = s.split('.')
		if len(self._maked_names)<len(names):
			return False

		wanted = 0
		for m in self._maked_names:
			if m == names[wanted]:
				wanted += 1
			if wanted == len(names):
				break

		return wanted == len(names)
	####
	#  #
	####
	def get_rule(self, rid):
		if rid not in self._rules.keys():
			return None
		return self._rules[rid]

	def get_rules_by_name(self, name):
		if name not in self.defination.keys():
			return []
		return self.defination[name]

	def get_weighted_rids(self, name):
		if name not in self._weighted_rids.keys():
			return []
		return self._weighted_rids[name]
	#

	def generate(self, name):
		s = self.make(name)
		return s

	def should_make_builtin(self, name):
		if 'Expression' not in name:
			return False
		
		if self.randint(0, 100) > 0 + self.level:
				return False
		return True

	def make_builtin(self):
		return 'Object()'
		#t = self.choice(list(self.builtin['Type'].keys()))
		#print(t)
		#print('make_builtin ...')
		if self.choice([0, 1])==0:
			return self.make_builtin_property()
		return self.make_builtin_call()

	def make_builtin_property(self):
		#print('make_builtin_property ...')
		name = self.choice(list(self.builtin['Property'].keys()))

		if name in self.hook['Property'].keys():
			callback = self.hook['Property'][name]
			return callback(self, name)

		return name

	def make_builtin_call(self):
		#print('make_builtin_call ...')
		name = self.choice(list(self.builtin['Function'].keys()))
		args = self.builtin['Function'][name]['args']
		rets = self.builtin['Function'][name]['rets']
		if args==None:
			args = [None] * self.randint(0, 5)
		args_maked = []
		for arg in args:
			args_maked.append(self.make_argument(arg))

		if name in self.hook['Function'].keys():
			callback = self.hook['Function'][name]
			return callback(self, name, args_maked, [])
		return '%s(%s)' % (name, ','.join(args_maked))

	def make_argument(self, argument):
		if argument == None:
			return self.ref_Id()
		else:
			return self.make(argument)

	def make(self, name):
		if self.should_make_builtin(name):
			return self.make_builtin()

		w_rids = self.get_weighted_rids(name)
		if len(w_rids) == 0:
			#logger.info('not define rules for "%s"' % name)
			#self.restart('not define rules for "%s"' % name)
			#raise(Exception('not define rules for "%s"' % name))
			return 'NO_%s' % name

		s = self._make(name, w_rids)
		return s

	def _make(self, name, weighted_rids):
		if self.level>self.MAX_DEPTH:
			print('level limit')
			raise(MakerException('level limit'))

		w_rids = self._prepare_rids(weighted_rids)
		while True:
			if len(w_rids)==0:
				print('no choose')
				raise(MakerException('no choose'))

			rid = Helper.choice(w_rids)
			rule = self.get_rule(rid)
			self._maked_rids.append(rid)
			self._maked_names.append(name)
			self.level += 1
			print('choose %d' % rid)

			"""
			user_defined_function may call scope_enter/scope_exit,
			but before scope_exit, there is an exception,
			so scope_exit failed to execute.
			To fix it, save current scope_stack before call user_defined_function
			and restore iit after called.
			So there should be a hint, that if user-defined-function should control
			scope, it must call scope_enter/scope_exit pair. This Maker algo don't
			allow single scope_enter call or signal scope_exit call exists in UDF.
			"""
			len_scope_stack = len(self.scope_stack)
			bak_current_scope = copy.deepcopy(self.scope_stack[-1])
			try:
				s = rule['f'](self)
				print('[SYNTAX] %s' % rule['d'])
				print('[LANGUAGE] %s' % s)
				break
			except MakerException as e:
				# make rule(rid) failed
				w_rids = list(filter(lambda a: a != rid, w_rids))
			
				self._maked_rids.pop()
				self._maked_names.pop()
				self.level -= 1

				rule = self.get_rule(rid)
				print('choose %d failed:' % (rid))
				print('      Reason: %s' % str(e))
				print('      AST: name @%s select rid %d: %s' % (name, rid, rule['d']))

				self.scope_stack = self.scope_stack[:len_scope_stack]
				self.scope_stack[-1] = bak_current_scope
				#print('[scope] detect an exception before scope exit, so force scope exit ...')

		self._maked_rids.pop()
		self._maked_names.pop()
		self.level -= 1
		return s

	def _prepare_rids(self, weighted_rids):

		if len(self._maked_rids)>=3:
			if self._maked_rids[-1]==self._maked_rids[-2] and self._maked_rids[-1]==self._maked_rids[-3]:
				#print('drop for direct 3-recursion')
				return []
		if len(self._maked_rids)>=16:
			stred_rids = [s.strip() for s in str(self._maked_rids)[1:-1].split(',')]
			rulepath = '-'.join(stred_rids)
			pattpath = '-'.join(stred_rids[-2:])
			if rulepath.count(pattpath)>3:
				#print('drop for 2-recursion')
				return []
			pattpath = '-'.join(stred_rids[-3:])
			if rulepath.count(pattpath)>3:
				#print('drop for 3-recursion')
				return []
			pattpath = '-'.join(stred_rids[-4:])
			if rulepath.count(pattpath)>3:
				#print('drop for 4-recursion')
				return []
		w_rids = list(weighted_rids)
		"""
		for rid in set(weighted_rids):
			if rid in self._end_rids:
				w_rids.extend([rid]*int(self.level/1))
		print(w_rids)
		"""
		return w_rids		

	