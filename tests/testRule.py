import fixTestImport

import logging
from language import Builder
from language import Ruler



logger = logging.getLogger(__name__)
logger.info('test running...')


if __name__=='__main__':
	builder = Builder.get_builder()
	builder.load('js/Expressions_rules.py')
	builder.load('js/Statements_and_Declarations_rules.py')
	builder.load('js/Functions_and_Classes_rules.py')
	builder.load('js/BuiltIn_Array_rules.py')

	ruler = Ruler.Ruler()
	ruler.load_rules(rules=builder.get_rules())

	for x in range(0,9):
		t = ruler.make(None, 'FunctionDeclaration')
		print('---------------------------------------')
		print()
		print(t)
		print()