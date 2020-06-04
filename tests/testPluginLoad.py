import os
import importlib.machinery

import fixTestImport

pluginDir = os.path.realpath('./plugins')
plugins = []

print('Plugin Directory: %s' % pluginDir)

def isPlugin(dirpath, filename):
	filepath = os.path.join(dirpath, filename)
	if not os.path.isfile(filepath):
		return None
	if filename.startswith('__'):
		return None
	return True

plugins = [os.path.join(pluginDir, x) for x in os.listdir(pluginDir) if isPlugin(pluginDir, x)]

print(plugins)
for p in plugins:
	print('loading %s...' % p)
	lib = importlib.machinery.SourceFileLoader('JS',p).load_module()
	print(lib.export)
	fn_regex = lib.export['expression']['regex']
	for x in range(0, 10):
		s = fn_regex()
		print('[regex] %s' % s)

