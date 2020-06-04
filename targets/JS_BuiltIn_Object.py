from language import Builder

builder = Builder.get_builder()

properties = [
	'Object.length',
	'Object.name',
	'Object.prototype',
	'Object.assign',
	'Object.getOwnPropertyDescriptor',
	'Object.getOwnPropertyDescriptors',
	'Object.getOwnPropertyNames',
	'Object.getOwnPropertySymbols',
	'Object.is',
	'Object.preventExtensions',
	'Object.seal',
	'Object.create',
	'Object.defineProperties',
	'Object.defineProperty',
	'Object.freeze',
	'Object.getPrototypeOf',
	'Object.setPrototypeOf',
	'Object.isExtensible',
	'Object.isFrozen',
	'Object.isSealed',
	'Object.keys',
	'Object.entries',
	'Object.values',
	'Object.prototype.constructor',
	'Object.prototype.__defineGetter__',
	'Object.prototype.__defineSetter__',
	'Object.prototype.hasOwnProperty',
	'Object.prototype.__lookupGetter__',
	'Object.prototype.__lookupSetter__',
	'Object.prototype.isPrototypeOf',
	'Object.prototype.propertyIsEnumerable',
	'Object.prototype.toString',
	'Object.prototype.valueOf',
	'Object.prototype.__proto__',
	'Object.prototype.toLocaleString'
]

methods = {
	'Object.assign': {'args': None, 'rets': None},
#	'Object.getOwnPropertyDescriptor': {'args': None, 'rets': None},
#	'Object.getOwnPropertyDescriptors': {'args': None, 'rets': None},
#	'Object.getOwnPropertyNames': {'args': None, 'rets': None},
#	'Object.getOwnPropertySymbols': {'args': None, 'rets': None},
#	'Object.is': {'args': None, 'rets': None},
#	'Object.preventExtensions': {'args': None, 'rets': None},
#	'Object.seal': {'args': None, 'rets': None},
#	'Object.create': {'args': None, 'rets': None},
#	'Object.defineProperties': {'args': None, 'rets': None},
#	'Object.defineProperty': {'args': None, 'rets': None},
#	'Object.freeze': {'args': None, 'rets': None},
#	'Object.getPrototypeOf': {'args': None, 'rets': None},
#	'Object.setPrototypeOf': {'args': None, 'rets': None},
#	'Object.isExtensible': {'args': None, 'rets': None},
#	'Object.isFrozen': {'args': None, 'rets': None},
#	'Object.isSealed': {'args': None, 'rets': None},
#	'Object.keys': {'args': None, 'rets': None},
#	'Object.entries': {'args': None, 'rets': None},
#	'Object.values': {'args': None, 'rets': None},
#	'Object.prototype.constructor': {'args': None, 'rets': None},
#	'Object.prototype.__defineGetter__': {'args': None, 'rets': None},
	'Object.prototype.__defineSetter__': {'args': ['TString', 'TFunction'], 'rets': None},
#	'Object.prototype.hasOwnProperty': {'args': None, 'rets': None},
#	'Object.prototype.__lookupGetter__': {'args': None, 'rets': None},
#	'Object.prototype.__lookupSetter__': {'args': None, 'rets': None},
#	'Object.prototype.isPrototypeOf': {'args': None, 'rets': None},
#	'Object.prototype.propertyIsEnumerable': {'args': None, 'rets': None},
	'Object.prototype.toString': {'args': [], 'rets': None},
#	'Object.prototype.valueOf': {'args': None, 'rets': None},
#	'Object.prototype.toLocaleString': {'args': None, 'rets': None}
}

def property_callback(m, target):
	if target.startswith('Object.prototype.') and m.randint(0, 4)!=0:
		# 75% use Id
		try:
			name = m.ref_Id()
			target =  target.replace('Object.prototype', name)
		except Exception as e:
			pass
	return target

def function_callback(m, target, args, rets):
	#print('function_callback ...')
	if target.startswith('Object.prototype.') and m.randint(0, 4)!=0:
		# 75% use Id
		try:
			name = m.ref_Id()
			target =  target.replace('Object.prototype', name)
		except Exception as e:
			pass
	target = target+'.call' if target.startswith('Object.prototype.') else target
	if target.endswith('.call'):
		try:
			arg0 = m.ref_Id()
			args.insert(0, arg0)
		except Exception as e:
			pass		
	return '%s(%s)' % (target, ','.join(args))

for name in properties:
	builder.define_Property(name=name)
	builder.hook_Property(target=name, callback=property_callback)

for name in methods.keys():
	builder.define_Function(name=name, args=methods[name]['args'], rets=methods[name]['rets'])
	builder.hook_Function(target=name, callback=function_callback)


#builder.hook_Argument(target='')

@builder.rule('TString', w=1)
def _(m):
	""" ARG_String:  """
	return m.make('StringLiteral')

@builder.rule('TFunction', w=1)
def _(m):
	""" ArgFunctionExpression:  """
	return m.make('FunctionExpression')

