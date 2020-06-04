from language import Builder

builder = Builder.get_builder()

all_properties = [
	'keyFor', 'getOwnPropertyDescriptors', 'toExponential', 'unscopables', 'bold', 'strike', 'setYear', 'getUTCDay', 
	#'for', 'catch', 'delete', 
	'big', 'defineProperty', 'getOwnPropertyNames', 'setMinutes', 'entries', 'split', 'isSafeInteger', 'from', 'getSeconds',
	'sub', 'getUint32', 'UTC', 'stackTraceLimit', 'constructor', 'hasOwnProperty', 'species', 'dotAll', 'isView',
	'toString', 'toISOString', 'setSeconds', 'some', 'input', 'getFloat32', 'toLocaleString', 'call', 'setUTCMinutes', 'reduce',
	 'flags', 'isFinite', 'propertyIsEnumerable', 'italics', 'getOwnPropertySymbols', 'set', 'forEach', 'then', 'revocable',
	 'getHours', 'getMinutes', 'ignoreCase', 'setMonth', 'asUintN', 'normalize', 'getUTCHours', 'getUTCMinutes', 'size', 'MAX_VALUE',
	 'name', 'unicode', 'bind', 'hasInstance', 'toDateString', 'BYTES_PER_ELEMENT', 'fontsize', 'fill', 'sticky', 'getUTCDate', 'blink',
	 'defineProperties', 'setInt8', 'values', 'source', 'fromCodePoint', 'isNaN', 'getTime', 'setUint16', 'EPSILON', 'lastMatch', 'setFloat64',
	 'global', 'copyWithin', 'lastParen', 'assign', 'isExtensible', 'asIntN', 'charCodeAt', 'getInt16', 'getDate', 'codePointAt', 'is',
	 'getMilliseconds', 'localeCompare', 'getDay', 'push', 'getUTCMonth', '__proto__', 'getBigInt64', '__defineSetter__', 'small', 'finally',
	 'compile', 'NaN', 'toStringTag', 'setUint32', 'lastIndexOf', 'trimStart', 'indexOf', 'toPrecision', 'trimEnd', 'reject', 'toLocaleDateString',
	 'setFloat32', 'freeze', 'isFrozen', 'replace', 'anchor', 'trimLeft', 'resolve', 'exec', 'setBigUint64', 'shift', 'charAt', 'endsWith', 'filter',
	 'iterator', 'getPrototypeOf', 'setDate', '__lookupGetter__', 'concat', 'includes', 'MIN_VALUE', 'reverse', 'setFullYear', 'substring',
	 'toLocaleTimeString', 'getUTCMilliseconds', 'setUTCSeconds', 'parseInt', 'apply', 'getUint8', 'getInt32', 'substr', 'multiline', 'byteOffset',
	 'trim', 'length', 'getFloat64', 'getUTCSeconds', 'create', 'isSealed', 'keys', 'toGMTString', 'link', 'every', 'match', 'MAX_SAFE_INTEGER',
	 'parse', 'rightContext', 'getBigUint64', 'toJSON', 'callee', 'asyncIterator', 'getYear', 'getUTCFullYear', 'setHours', 'search', 'getFullYear',
	 'MIN_SAFE_INTEGER', 'test', 'isPrototypeOf', 'sort', 'valueOf', 'unshift', 'leftContext', 'toLocaleLowerCase', 'setUint8', 'splice', 'setInt16',
	 'trimRight', 'message', '__defineGetter__', 'toLowerCase', 'setUTCMilliseconds', 'getTimezoneOffset', 'setBigInt64', 'fixed', 'setPrototypeOf',
	 'caller', 'isInteger', 'setUTCHours', 'clear', 'getOwnPropertyDescriptor', 'padStart', 'fromCharCode', 'fontcolor', 'toTimeString', 'setUTCFullYear',
	 'add', 'toPrimitive', 'prototype', 'of', 'repeat', 'isConcatSpreadable', '__lookupSetter__', 'arguments',
	 'NEGATIVE_INFINITY', 'byteLength', 'find', 'padEnd', 'captureStackTrace', 'sup', 'setUTCMonth', 'findIndex', 'setMilliseconds', 'race', 'toFixed',
	 'buffer', 'toLocaleUpperCase', 'has', 'get', 'getUint16', 'getInt8', 'map', 'setInt32', 'seal', 'reduceRight', 'join', 'startsWith', 'preventExtensions',
	 'setTime', 'getMonth', 'isArray', 'toUpperCase', 'now', 'slice', 'toUTCString', 'pop', 'all', 'raw', 'POSITIVE_INFINITY', 'setUTCDate', 'parseFloat',
	 'value', 'writable']

BaseClass = [
	'Object', 'Array', 'Function', 'Number', 'Boolean', 'String',
	'Symbol', 'Date', 'Promise', 'RegExp', 
	'ArrayBuffer',
	'Uint8Array', 'Int8Array', 'Uint16Array', 'Int16Array',
	'Uint32Array', 'Int32Array', 'Float32Array', 'Float64Array',
	'Uint8ClampedArray', 'SharedArrayBuffer', 'DataView',
	'Map', 'Set', 'WeakMap', 'WeakSet', 'Proxy', 
]
"""
IdentifierName
"""
@builder.rule('IdentifierName', w=1)
def _(m):
	""" IdentifierName: """
	return m.ref_Id()

"""
IdentifierName
"""
@builder.rule('StringLiteral', w=1)
def _(m):
	""" StringLiteral: """
	return '"%s"' % m.choice(all_properties)

"""
IdentifierName
"""
@builder.rule('NumericLiteral', w=1)
def _(m):
	""" NumericLiteral: """
	return '%d' % m.randint(-0xFFFFFFFFFFFFFFFF, 0xFFFFFFFFFFFFFFFF+1)

"""
TemplateLiteral
"""
@builder.rule('TemplateLiteral', w=1)
def _(m):
	""" TemplateLiteral: $empty """
	return '``'

@builder.rule('TemplateLiteral', w=1)
def _(m):
	""" TemplateLiteral: just_properties """
	return '`%s`' % m.choice(all_properties)

@builder.rule('TemplateLiteral', w=1)
def _(m):
	""" TemplateLiteral: `${Expression}` """
	return '`${%s}`' % m.make('Expression')


@builder.rule('BuiltInBaseClass', w=1)
def _(m):
	""" @BuiltInBaseClass: [...]  """
	base = m.choice(BaseClass)
	return base

#############################
#############################
#############################

@builder.rule('TestDeepArray', w=1, e=True)
def _(maker):
	""" @ArrayInit: new Array() """
	return '1'

@builder.rule('TestInt', w=1, e=True)
def _(maker):
	""" @ArrayInit: new Array() """
	return '0xFFFFFFFF'

@builder.rule('TestDeepArray', w=5)
def _(maker):
	""" @ArrayInit: new Array() """
	return '%s+%s' % (maker.make('TestDeepArray'), maker.make('TestDeepArray'))


@builder.rule('TestNewTarget', w=1)
def _(maker):
	""" TestNewTarget: Newtarget """
	return '%s' % (maker.make('Newtarget'))

#################################
#
#################################

