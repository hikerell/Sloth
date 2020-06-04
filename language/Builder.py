import importlib.machinery

from . import Parser

class Builder(object):
	"""docstring for Builder"""
	def __init__(self):
		super(Builder, self).__init__()
		self.rules = []
		self.libraries = []

	def load(self, file):
		lib = importlib.machinery.SourceFileLoader('JS', file).load_module()
		self.libraries.append(lib)

	def get_rules(self):
		return self.rules

	def build(self, description):
		r = Parser.parse(description)
		def decorate(f):
			rule = {'name': r['name'], 'nodes': r['nodes'], 'description': description, 'maker': f}
			self.rules.append(rule)

			def wapper(*args, **kwargs):
				return None
		return decorate

builders = {}

def get_builder(name='default'):
	if name not in builders.keys():
		builders[name] = Builder()
	return builders[name]

