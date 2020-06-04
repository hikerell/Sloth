from language import Builder

builder = Builder.get_builder()

builder.define_Id('a', 'Array')

#builder.r(w=1, 'BuiltInExpression_Type_Array_declare: @BuiltInExpression_Type_Array_Instance')
#builder.r(w=1, 'BuiltInExpression_Type_Array: @BuiltInExpression_Type_Array_Instance')
#builder.r(w=1, 'BuiltInExpression_Type_Array: @BuiltInExpression_Type_Array_Type')

#builder.r(w=1, 'BuiltInArrayExpression: @BuiltInArrayTypeExpression')

t = 'Array'

def declare_fn(m):
	name = m.new_Id()
	s = 'new Array(0,1,2,3)'
	m.scope_set_Id(n=name, t=t)
	return '%s=%s;' % (name, s)

properties = [
	'Array.length',
	'Array.name',
	'Array.prototype',
	'Array.isArray',
	'Array.from',
	'Array.of',
	'Array.prototype.length',
	'Array.prototype.constructor',
	'Array.prototype.concat',
	'Array.prototype.find',
	'Array.prototype.findIndex',
	'Array.prototype.pop',
	'Array.prototype.push',
	'Array.prototype.shift',
	'Array.prototype.unshift',
	'Array.prototype.slice',
	'Array.prototype.splice',
	'Array.prototype.includes',
	'Array.prototype.indexOf',
	'Array.prototype.keys',
	'Array.prototype.entries',
	'Array.prototype.forEach',
	'Array.prototype.filter',
	'Array.prototype.map',
	'Array.prototype.every',
	'Array.prototype.some',
	'Array.prototype.reduce',
	'Array.prototype.reduceRight',
	'Array.prototype.toString',
	'Array.prototype.toLocaleString',
	'Array.prototype.join',
	'Array.prototype.reverse',
	'Array.prototype.sort',
	'Array.prototype.lastIndexOf',
	'Array.prototype.copyWithin',
	'Array.prototype.fill',
	'Array.prototype.values'
]
def property_fn(m):
	prop = m.choice(properties)
	if 'Array.prototype.' in prop and m.choice([0, 1])==1:
		try:
			name = m.ref_Id(t=t)
			return prop.replace('Array.prototype', name)
		except Exception as e:
			pass
	return prop

methods = [
	'Array.isArray',
	'Array.from',
	'Array.of',
	'Array.prototype.length',
	'Array.prototype.constructor',
	'Array.prototype.concat',
	'Array.prototype.find',
	'Array.prototype.findIndex',
	'Array.prototype.pop',
	'Array.prototype.push',
	'Array.prototype.shift',
	'Array.prototype.unshift',
	'Array.prototype.slice',
	'Array.prototype.splice',
	'Array.prototype.includes',
	'Array.prototype.indexOf',
	'Array.prototype.keys',
	'Array.prototype.entries',
	'Array.prototype.forEach',
	'Array.prototype.filter',
	'Array.prototype.map',
	'Array.prototype.every',
	'Array.prototype.some',
	'Array.prototype.reduce',
	'Array.prototype.reduceRight',
	'Array.prototype.toString',
	'Array.prototype.toLocaleString',
	'Array.prototype.join',
	'Array.prototype.reverse',
	'Array.prototype.sort',
	'Array.prototype.lastIndexOf',
	'Array.prototype.copyWithin',
	'Array.prototype.fill',
	'Array.prototype.values',
	'Array.prototype.__defineGetter__',
	'Array.prototype.__defineSetter__',
	'Array.prototype.hasOwnProperty',
	'Array.prototype.__lookupGetter__',
	'Array.prototype.__lookupSetter__',
	'Array.prototype.isPrototypeOf',
	'Array.prototype.propertyIsEnumerable',
	'Array.prototype.toString',
	'Array.prototype.valueOf',
	'Array.prototype.__proto__',
	'Array.prototype.toLocaleString'
]
def call_fn(m):
	method = m.choice(methods)
	if method.startswith('Array.prototype.') and m.choice([0, 1])==1:
		try:
			name = m.ref_Id(t=t)
			method =  method.replace('Array.prototype', name)
		except Exception as e:
			pass
	method = method+'.call' if method.startswith('Array.prototype.') else method
	args = m.make('Arguments')
	return '%s%s' % (method, args)

#builder.define_Type('Array', 
#	declare_fn=declare_fn, property_fn=property_fn, call_fn=call_fn)

####
m = {}
m['Array.isArray'] = {'args': None, 'rets': None}

methods = {
	'Array.isArray':{ 'args': None, 'rets': None },
	'Array.from':{ 'args': None, 'rets': None },
	'Array.of':{ 'args': None, 'rets': None },
	'Array.prototype.length':{ 'args': None, 'rets': None },
	'Array.prototype.constructor':{ 'args': None, 'rets': None },
	'Array.prototype.concat':{ 'args': None, 'rets': None },
	'Array.prototype.find':{ 'args': None, 'rets': None },
	'Array.prototype.findIndex':{ 'args': None, 'rets': None },
	'Array.prototype.pop':{ 'args': None, 'rets': None },
	'Array.prototype.push':{ 'args': None, 'rets': None },
	'Array.prototype.shift':{ 'args': None, 'rets': None },
	'Array.prototype.unshift':{ 'args': None, 'rets': None },
	'Array.prototype.slice':{ 'args': None, 'rets': None },
	'Array.prototype.splice':{ 'args': None, 'rets': None },
	'Array.prototype.includes':{ 'args': None, 'rets': None },
	'Array.prototype.indexOf':{ 'args': None, 'rets': None },
	'Array.prototype.keys':{ 'args': None, 'rets': None },
	'Array.prototype.entries':{ 'args': None, 'rets': None },
	'Array.prototype.forEach':{ 'args': None, 'rets': None },
	'Array.prototype.filter':{ 'args': None, 'rets': None },
	'Array.prototype.map':{ 'args': None, 'rets': None },
	'Array.prototype.every':{ 'args': None, 'rets': None },
	'Array.prototype.some':{ 'args': None, 'rets': None },
	'Array.prototype.reduce':{ 'args': None, 'rets': None },
	'Array.prototype.reduceRight':{ 'args': None, 'rets': None },
	'Array.prototype.toString':{ 'args': None, 'rets': None },
	'Array.prototype.toLocaleString':{ 'args': None, 'rets': None },
	'Array.prototype.join':{ 'args': None, 'rets': None },
	'Array.prototype.reverse':{ 'args': None, 'rets': None },
	'Array.prototype.sort':{ 'args': None, 'rets': None },
	'Array.prototype.lastIndexOf':{ 'args': None, 'rets': None },
	'Array.prototype.copyWithin':{ 'args': None, 'rets': None },
	'Array.prototype.fill':{ 'args': None, 'rets': None },
	'Array.prototype.values':{ 'args': None, 'rets': None },
	'Array.prototype.__defineGetter__':{ 'args': None, 'rets': None },
	'Array.prototype.__defineSetter__':{ 'args': None, 'rets': None },
	'Array.prototype.hasOwnProperty':{ 'args': None, 'rets': None },
	'Array.prototype.__lookupGetter__':{ 'args': None, 'rets': None },
	'Array.prototype.__lookupSetter__':{ 'args': None, 'rets': None },
	'Array.prototype.isPrototypeOf':{ 'args': None, 'rets': None },
	'Array.prototype.propertyIsEnumerable':{ 'args': None, 'rets': None },
	'Array.prototype.toString':{ 'args': None, 'rets': None },
	'Array.prototype.valueOf':{ 'args': None, 'rets': None },
	'Array.prototype.__proto__':{ 'args': None, 'rets': None },
	'Array.prototype.toLocaleString':{ 'args': None, 'rets': None },
}

#builder.hook(category='Argument', target='Array.prototype.toString')
#@builder.builtin(category='prop')
#@builder.builtin(category='call')

#builder.hook(category='Argument', target='Array.prototype.toString')

