import importlib.machinery

class Builder(object):
	"""docstring for Builder"""
	def __init__(self):
		super(Builder, self).__init__()
		self.rules = {} #{}
		self.count = 0
		self.environment = {
			'Id': [],
			'Type': {},

			'Property': {},
			'Function': {},
			
			'Hook': {
				'Property': {},
				'Function': {},
				'Argument': {}
			}
		}
		self.libraries = []

	def load(self, file):
		lib = importlib.machinery.SourceFileLoader('JS', file).load_module()
		self.libraries.append(lib)

	def get_rules(self):
		return self.rules

	def _build_rule(self, n='', w=1, f=None, d='', e=False):
		"""
		d: description
		e: end term
		"""
		rid = self.count
		rule = {'n': n, 'id': rid, 'w': w, 'f': f, 'd': d, 'e': e}
		if n not in self.rules.keys():
			self.rules[n] = []
		self.rules[n].append(rule)
		self.count += 1

	def rule(self, name, w=1, e=False):
		def decorate(f):
			self._build_rule(n=name, w=w, f=f, d=f.__doc__.strip(), e=e)
			
			def wapper(*args, **kwargs):
				return None
		return decorate

	def r(self, w=1, d=''):
		self.sample_rule(w=w, d=d)

	def sample_rule(self, w=1, d=''):
		"""
		define format:
		ruleName: @ruleNameReferenceA textTokenN @ruleNameReferenceB ...
		"""
		d = d.strip()
		head = d.split(':')[0]
		body = d[len(head)+1:]
		n = head.strip()
		tokens = body.strip().split(' ')
		f = lambda m: ' '.join([m.make(tk[1:]) if len(tk)>0 and tk[0]=='@' else tk for tk in tokens])
		self._build_rule(n=n, w=1, f=f, d=d, e=False)

	def get_environment(self):
		return self.environment

	def define_Id(self, n, t):
		self.environment['Id'].append({'name':n, 'type':t})

	#def define_Type(self, t, e):
	#	self.environment['Type'][t] = e
	def define_Type(self, t='', declare_fn=None, property_fn=None, call_fn=None, extends=[]):

		self.environment['Type'][t] = {
			'declare_fn': declare_fn,
			'property_fn': property_fn,
			'call_fn': call_fn
		}

	def define_Property(self, name=''):
		self.environment['Property'][name]={}

	def define_Function(self, name='', args=None, rets=None):
		self.environment['Function'][name]={ 'args': args, 'rets': rets }

	def hook_Property(self, target, callback):
		self.environment['Hook']['Property'][target] = callback

	def hook_Function(self, target, callback):
		self.environment['Hook']['Function'][target] = callback
		

builders = {}

def get_builder(name='default'):
	if name not in builders.keys():
		builders[name] = Builder()
	return builders[name]

