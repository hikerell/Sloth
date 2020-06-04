import random

from . import Stage
from . import State

class RuleNotFoundException(Exception):
	pass

class MakeFailedException(Exception):
	pass

class Ruler(object):
	"""docstring for Ruler"""
	def __init__(self):
		super(Ruler, self).__init__()
		self.rules = []
		self.rulemap = {}
		self.rule_stack = []

		self.no_recursive_weight = 100
		self.max_rule_stack_depth = 400

		self.uuid_count = -1

	def load_rules(self, rules=[]):
		rid = 0
		for rule in rules:
			rule['rid'] = rid
			rule['metadata'] = {}
			if rule['name'] not in self.rulemap.keys():
				self.rulemap[rule['name']] = []
			self.rulemap[rule['name']].append(rid)
			rid += 1
		self.rules = rules
		self.analyze_rules()

	def analyze_rules(self):
		new_rules = []
		recursive_rids = []
		for rule in self.rules:
			looprule = False
			for node in rule['nodes']:
				if node['type']!='NAME':
					continue
				if rule['name']==node['value']:
					looprule = True
					break
			if looprule:
				rule['metadata']['selfreference'] = True
				recursive_rids.append(rule['rid'])
			else:
				rule['metadata']['selfreference'] = False
		for name, rids in self.rulemap.items():
			recursive_count = 0
			for recursive_rid in recursive_rids:
				if recursive_rid in rids:
					recursive_count += 1
			if recursive_count>0:
				weighted_rids = []
				weight = recursive_count * self.no_recursive_weight
				for rid in rids:
					if rid in recursive_rids:
						weighted_rids.append(rid)
					else:
						weighted_rids.extend([rid]*weight)
				self.rulemap[name] = weighted_rids
				print('[analyze] rule %s contains recursive rules, just adjust there weight!')
				print('    from %s to %s' %(str(rids), str(weighted_rids)))

	def analyze_max_rule_depth(self):
		for rule in self.rules:
			pass

	def dump_rule_stack(self):
		print('======== [DEBUG] rule_stack ========')
		indent = 0
		for node in self.rule_stack:
			print(' '*indent + 'name: ' + node['name'])
			print(' '*indent + 'description: ' + node['rule']['description'])
			print(' '*indent + 'target: ' + node['target'])
			indent += 2
	def dump_rule_stack_tree(self):
		print('======== [DEBUG] rule_stack ========')
		indent = 0
		for node in self.rule_stack:
			print('%d ' % node['rule']['rid'] + 'name: ' + node['name'] + ' => ' + node['rule']['description'])


	def contain_blacklist(self, rule, blacklist=[]):
		for name in blacklist:
			s = ' %s ' % name
			if s in rule['description']:
				return True
		return False

	def make_dfs(self, context, name):
		if len(self.rule_stack)>self.max_rule_stack_depth:
			return None
		if name not in self.rulemap.keys():
			return 'No_%s' % name
			self.dump_rule_stack()
			raise(RuleNotFoundException('Not found rule name "%s"' % name))

		rids = list(self.rulemap[name])
		retry = False
		blacklist = []
		while len(rids)>0:
			rid = random.choice(rids)
			rule = self.rules[rid]
			#if retry and rule['metadata']['selfreference']:
			if self.contain_blacklist(rule, blacklist):
				print('\rretry again: Failed at %s because of blacklist%s'
					% (name, ' '*64),
					end='')
				while rid in rids:
					rids.remove(rid)
				#print()
				continue
			retry = False
			blacklist.append(rule['name'])
			texts = []
			maker = rule['maker']
			target = ''
			storage = {'rule_stack': self.rule_stack}
			state = maker(context, self, stage=Stage.Prepare, target=target, storage=storage)
			if state == State.Stop:
				return storage['text']
			elif state == State.Continue:
				for node in rule['nodes']:
					if node['type']=='TEXT':
						texts.append(node['value'])
					else:
						self.rule_stack.append({'name': name, 'rule': rule, 'target': node['value']})
						result = self.make(context, node['value'])
						self.rule_stack.pop()
						if result == None:
							retry = True
							blacklist.append(node['value'])
							break
						else:
							texts.append(result)
				if not retry:
					text = ' '.join(texts)
					return text
			print('\rretry again: Failed at %s%s' % (name, ' '*64), end='')
			while rid in rids:
				rids.remove(rid)
		print('\rrestart again: Failed at %s, back to up level, stacks: %d %s'
		 	%(name, len(self.rule_stack), ' '*64),
		 	end='')
		#self.dump_rule_stack_tree()
		#print()
		#print()
		#self.dump_rule_stack()
		#import time
		#time.sleep(0.5)
		return None
		#raise(MakeFailedException('Failed to make at rule name: "%s"' % name))

	def pick_rule(self, name,  blacklist=[]):
		rids = list(self.rulemap[name])
		while len(rids)>0:
			rid = random.choice(rids)
			rule = self.rules[rid]
			if self.contain_blacklist(rule, blacklist):
				while rid in rids:
					rids.remove(rid)
				continue
			return rule
		return None

	def get_uuid(self):
		self.uuid_count += 1
		return 'uuid_%d' % self.uuid_count

	def make(self, context, name):
		ast_tree = {}
		init_ast = {
			'uuid': self.get_uuid(),
			'rid': -1,
			'name': 'root',
			'nodes': [{'type': 'NAME', 'value': name}],
			'description': 'root : %s' % name,
			'maker': lambda c, r: None,
			'storage': {},
			'blacklist': [],
			'value': None
			}
		init_ast['nodes'][0]['uuid'] = init_ast['uuid']
		ast_stack = [ init_ast ]
		targets = [ init_ast['nodes'][0] ]
		while len(targets)>0:
			ast = ast_stack[-1]
			target = targets.pop()
			if target['type']=='TEXT':
				continue
			# target is a NAME node
			if target['value'] not in self.rulemap.keys():
				target['ast'] = None
				target['ast'] = None
				continue
				#self.dump_rule_stack()
				#raise(RuleNotFoundException('Not found rule name "%s"' % name))

			rule = self.pick_rule(target['value'], blacklist=ast['blacklist'])
			if rule:
				new_ast = {
					'uuid': self.get_uuid(),
					'rid': rule['rid'],
					'name': rule['name'],
					'nodes': [dict(node) for node in rule['nodes']],
					'description': rule['description'],
					'blacklist': []
				}
				for node in new_ast['nodes']:
					node['uuid'] = new_ast['uuid']
				ast_stack.append(new_ast)
				targets.extend(new_ast['nodes'])
				target['ast'] = new_ast
			else:
				droped_ast = ast_stack.pop()
				for node in targets:
					if node['uuid'] == droped_ast['uuid']:
						targets.remove(node)
				upper_ast = ast_stack[-1]
				upper_ast['blacklist'].append(droped_ast['name'])
				upper_ast['blacklist'].append(upper_ast['name'])
				targets.push(target)
			#print('targets list length: %d'%len(targets))
		for ast in ast_stack:
			ast_tree[ast['uuid']] = ast

		s = self.makeup(ast_tree, init_ast)
		print(s)
		return ''
		#raise(MakeFailedException('Failed to make at rule name: "%s"' % name))

	def makeup_dfs(self, tree, root):
		result = []
		for node in root['nodes']:
			if node['type'] == 'TEXT':
				result.append(node['value'])
			else:
				child = tree[node['uuid']]
				result.append(self.makeup(tree, child))
		return ' '.join(result)

	def makeup(self, tree, root):
		result = []
		nodes = []
		nodes.extend(root['nodes'][::1])
		while len(nodes)>0:
			node = nodes.pop()
			if node['type'] == 'TEXT':
				result.append(node['value'])
			else:
				#print('node: %s' % str(node))
				child = node['ast']
				if child:
					nodes.extend(child['nodes'][::-1])
				else:
					result.append('No_%s' % node['value'])
		return ' '.join(result)