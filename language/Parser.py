import ply.lex as lex
import ply.yacc as yacc

tokens = (
	'ID',
	'TEXT',
	'COLON'
)

t_ignore = ' \t'

t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_TEXT = r'`[^`]*`'
t_COLON = r':'

def t_error(t):
	raise(Exception("Illegal character '%s'" % t.value[0]))

"""
RULE : RULENAME COLON RULENODES
RULENAME : ID
RULENODES : RULENODE
		  | RULENODES RULENODE
RULENODE : TEXTNODE
		 | NAMENODE

TEXTNODE : TEXT
NAMENODE : RULENAME
"""
def p_rule(p):
	"""
	RULE : RULENAME COLON RULENODES
	"""
	rule = {}
	rule['name'] = p[1]
	rule['nodes'] = p[3]

	p[0] = rule

def p_rulename(p):
	"""
	RULENAME : ID
	"""
	p[0] = p[1]

def p_rulenodes(p):
	"""
	RULENODES : RULENODE
			  | RULENODES RULENODE
	"""
	nodes = []
	if len(p) == 2:
		nodes.append(p[1])
	else:
		nodes.extend(p[1])
		nodes.append(p[2])
	p[0] = nodes

def p_rulenode(p):
	"""
	RULENODE : TEXTNODE
			 | NAMENODE
	"""
	p[0] = p[1]

def p_textnode(p):
	"""
	TEXTNODE : TEXT
	"""
	node = {}
	node['type'] = 'TEXT'
	node['value'] = p[1][1:-1]
	p[0] = node

def p_namenode(p):
	"""
	NAMENODE : RULENAME
	"""
	node = {}
	node['type'] = 'NAME'
	node['value'] = p[1]
	p[0] = node	

def p_error(p):
	raise(Exception("rule error at %s" % p))
#lexer = lex.lex()
#lexer.input(test_data)

#for tok in lexer:
#	print(tok)

lex.lex()
parser = yacc.yacc()

def parse(text):
	print('[parse] %s' % text)
	ast = parser.parse(text)
	ast['text'] = text
	#print('[parse] %s' % str(ast))
	return ast

if __name__=='__main__':
	test_data = 'TestRule: ArgumentList COLON ArgumentList `,` `...` AssignmentExpression'
	print(parse(test_data))