import os
import importlib.machinery

import fixTestImport

from core import Maker
from language import Builder

if __name__=="__main__":

	builder = Builder.get_builder()
	builder.load('res/ecma_2018_9_0/JS_Syntax_Expression.py')
	builder.load('res/ecma_2018_9_0/JS_Syntax_Statement.py')
	builder.load('res/ecma_2018_9_0/JS_Syntax_Function.py')
	builder.load('res/ecma_2018_9_0/JS_BuiltIn.py')
	#builder.load('targets/JS_BuiltIn.py')
	#builder.load('targets/JS_BuiltIn_Object.py')
	#builder.load('targets/JS_BuiltIn_Array.py')
	rules = builder.get_rules()
	environment = builder.get_environment()

	#print(rules)
	#print(environment)

	m = Maker.Maker(rules, environment)
	for x in range(0,1):
		#print(m.make('ArrayLiteral'))
		#print(m.make('ObjectLiteral'))
		#print(m.make('MemberExpression'))
		#print(m.make('TestDeepArray'))
		print(m.make('Expression'))
		
		#print(m.make('ConditionalExpression'))
		
		#print('try{ %s }catch(e){ console.log(e); }' % m.make('Expression'))
		#print(m.make('FunctionExpression'))
		#print('%s' % m.make('ClassExpression'))
		print('%s' % m.make('Statement'))

		#print('%s' % m.make('LexicalDeclaration'))

		
		
	