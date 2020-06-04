import fixTestImport

from core.Parser import Parser

if __name__=="__main__":
	p = Parser()
	rule = p.parse_line()
	print(rule)