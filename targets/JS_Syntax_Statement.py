from language import Builder

builder = Builder.get_builder()

"""
13 ECMAScript Language: Statements and Declarations
Statement: BlockStatement 
Statement: VariableStatement 
Statement: EmptyStatement
Statement: ExpressionStatement 
Statement: IfStatement 
Statement: BreakableStatement 
Statement: ContinueStatement 
Statement: BreakStatement 
Statement: ReturnStatement 
Statement: WithStatement 
Statement: LabelledStatement 
Statement: ThrowStatement 
Statement: TryStatement 
Statement: DebuggerStatement
Declaration: HoistableDeclaration
Declaration: ClassDeclaration
Declaration: LexicalDeclaration
HoistableDeclaration: FunctionDeclaration
HoistableDeclaration: GeneratorDeclaration
HoistableDeclaration: AsyncFunctionDeclaration
HoistableDeclaration: AsyncGeneratorDeclaration
BreakableStatement: IterationStatement 
BreakableStatement: SwitchStatement 
"""
builder.r(w=1, d='Statement: @BlockStatement')
builder.r(w=1, d='Statement: @VariableStatement')
builder.r(w=1, d='Statement: @EmptyStatement')
builder.r(w=1, d='Statement: @ExpressionStatement')
builder.r(w=1, d='Statement: @IfStatement')
builder.r(w=1, d='Statement: @BreakableStatement')
#builder.r(w=1, d='Statement: @ContinueStatement')
@builder.rule('Statement', w=1)
def _(m):
	""" Statement: @ContinueStatement """
	#
	#It is a Syntax Error if this ContinueStatement is not nested, directly or indirectly (but not crossing function boundaries), within an IterationStatement.
	#
	if not m.rule_under('IterationStatement'):
		m.restart('ContinueStatement should under IterationStatement')
	return m.make('ContinueStatement')

#It is a Syntax Error if this ContinueStatement is not nested, directly or indirectly (but not crossing function boundaries), within an IterationStatement.

#builder.r(w=1, d='Statement: @BreakStatement')
@builder.rule('Statement', w=1)
def _(m):
	""" Statement: @BreakStatement """
	#
	#It is a Syntax Error if this BreakStatement is not nested, directly or indirectly (but not crossing function boundaries), within an IterationStatement or a SwitchStatement.
	#
	if not (m.rule_under('IterationStatement') or m.rule_under('SwitchStatement')):
		m.restart('BreakStatement should under IterationStatement or SwitchStatement')
	return m.make('BreakStatement')

builder.r(w=1, d='Statement: @ReturnStatement')
builder.r(w=1, d='Statement: @WithStatement')
builder.r(w=1, d='Statement: @LabelledStatement')
#builder.r(w=1, d='Statement: @ThrowStatement')
#builder.r(w=1, d='Statement: @TryStatement')
#builder.r(w=1, d='Statement: @DebuggerStatement')

#builder.r(w=1, d='Declaration: @HoistableDeclaration')
#builder.r(w=1, d='Declaration: @ClassDeclaration')
builder.r(w=10, d='Declaration: @LexicalDeclaration')

builder.r(w=1, d='HoistableDeclaration: @FunctionDeclaration')
builder.r(w=1, d='HoistableDeclaration: @GeneratorDeclaration')
builder.r(w=1, d='HoistableDeclaration: @AsyncFunctionDeclaration')
builder.r(w=1, d='HoistableDeclaration: @AsyncGeneratorDeclaration')

builder.r(w=1, d='BreakableStatement: @IterationStatement')
builder.r(w=1, d='BreakableStatement: @SwitchStatement')

"""
13.2 Block
BlockStatement: Block
Block: {} 
Block: {StatementList}
StatementList: StatementListItem
StatementList: StatementList StatementListItem 
StatementListItem: Statement 
StatementListItem: Declaration
"""
builder.r(w=1, d='BlockStatement: @Block')

builder.r(w=1, d='Block: { }')
builder.r(w=1, d='Block: { @StatementList }')

builder.r(w=1, d='StatementList: @StatementListItem')
builder.r(w=1, d='StatementList: @StatementListItem @StatementListItem')
builder.r(w=1, d='StatementList: @StatementListItem @StatementListItem @StatementListItem')

@builder.rule('StatementList', w=1)
def _(m):
	""" StatementList: StatementListItem xN"""
	count = m.randint(3, 10)
	items = [ m.make('StatementListItem') for x in range(0, count) ]
	return ' '.join(items)

builder.r(w=10, d='StatementListItem: @Statement')
builder.r(w=1, d='StatementListItem: @Declaration')

"""
13.3 Declarations and the Variable Statement
13.3.1Let and Const Declarations

LexicalDeclaration:
	LetOrConst BindingList;

LetOrConst:
	let
	const

BindingList:
	LexicalBinding
	BindingList,LexicalBinding

LexicalBinding:
	BindingIdentifier
	BindingIdentifier Initializer
	BindingPattern Initializer 
"""
@builder.rule('LexicalDeclaration', w=1)
def _(m):
	""" LexicalDeclaration: let|const BindingIdentifier ; """
	let_or_const = m.choice(['let', 'const'])
	name = m.new_Id()
	m.scope_set_Id(n=name)
	return '%s %s ;' % (let_or_const, name)

@builder.rule('LexicalDeclaration', w=10)
def _(m):
	""" LexicalDeclaration: let|const BindingIdentifier Initializer ; """
	let_or_const = m.choice(['let', 'const'])
	name = m.new_Id()
	stmt = m.make('Initializer')
	m.scope_set_Id(n=name)
	return '%s %s %s;' % (let_or_const, name, stmt)

#[TODO]
#@builder.rule('LexicalDeclaration', w=1)
def _(m):
	""" LexicalDeclaration: let|const BindingPattern Initializer ; """
	let_or_const = m.choice(['let', 'const'])
	name = m.new_Id()
	stmt = m.make('Initializer')
	m.scope_set_Id(n=name)
	return '%s %s %s;' % (let_or_const, name, stmt)

"""
13.3.2Variable Statement
VariableStatement[Yield, Await]:
varVariableDeclarationList ;
VariableDeclarationList:
VariableDeclaration[?In, ?Yield, ?Await]
VariableDeclarationList[?In, ?Yield, ?Await],VariableDeclaration[?In, ?Yield, ?Await]
VariableDeclaration[In, Yield, Await]:
BindingIdentifier[?Yield, ?Await]Initializer[?In, ?Yield, ?Await]opt
BindingPattern[?Yield, ?Await]Initializer[?In, ?Yield, ?Await]
"""

"""
13.3.3Destructuring Binding Patterns
BindingPattern[Yield, Await]:
ObjectBindingPattern[?Yield, ?Await]
ArrayBindingPattern[?Yield, ?Await]
ObjectBindingPattern[Yield, Await]:
{}
{BindingRestProperty[?Yield, ?Await]}
{BindingPropertyList[?Yield, ?Await]}
{BindingPropertyList[?Yield, ?Await],BindingRestProperty[?Yield, ?Await]opt}
ArrayBindingPattern[Yield, Await]:
[ElisionoptBindingRestElement[?Yield, ?Await]opt]
[BindingElementList[?Yield, ?Await]]
[BindingElementList[?Yield, ?Await],ElisionoptBindingRestElement[?Yield, ?Await]opt]
BindingRestProperty[Yield, Await]:
...BindingIdentifier[?Yield, ?Await]
BindingPropertyList[Yield, Await]:
BindingProperty[?Yield, ?Await]
BindingPropertyList[?Yield, ?Await],BindingProperty[?Yield, ?Await]
BindingElementList[Yield, Await]:
BindingElisionElement[?Yield, ?Await]
BindingElementList[?Yield, ?Await],BindingElisionElement[?Yield, ?Await]
BindingElisionElement[Yield, Await]:
ElisionoptBindingElement[?Yield, ?Await]
BindingProperty[Yield, Await]:
SingleNameBinding[?Yield, ?Await]
PropertyName[?Yield, ?Await]:BindingElement[?Yield, ?Await]
BindingElement[Yield, Await]:
SingleNameBinding[?Yield, ?Await]
BindingPattern[?Yield, ?Await]Initializer opt
SingleNameBinding[Yield, Await]:
BindingIdentifier[?Yield, ?Await]Initializer opt
BindingRestElement[Yield, Await]:
...BindingIdentifier[?Yield, ?Await]
...BindingPattern[?Yield, ?Await]
"""

"""
13.4 Empty Statement
EmptyStatement: ;
"""
builder.r(w=1, d='EmptyStatement: ;')

"""
13.5 Expression Statement
ExpressionStatement[Yield, Await]:
[lookahead ∉ { {, function, async [no LineTerminator here] function, class, let [ }] Expression ;
"""
@builder.rule('ExpressionStatement', w=1)
def _(m):
	""" ExpressionStatement: Expression """
	count = m.randint(3, 10)
	items = [ m.make('StatementListItem') for x in range(0, count) ]
	tried = 0
	MAX_TRIED = 10
	bans = ['{', 'function', 'async function', 'class', 'let', '[']
	s = ''
	while tried < MAX_TRIED:
		tried += 1
		s = m.make('Expression')
		for ban in bans:
			if s.strip().startswith(ban):
				continue
		break
	return '%s;' % s

"""
13.6 The if Statement
Syntax
IfStatement: if( Expression ) Statement else Statement
if( Expression ) Statement 
"""
builder.r(w=1, d='IfStatement: if( @Expression ) @Statement else @Statement')
builder.r(w=1, d='IfStatement: if( @Expression ) @Statement')

"""
13.7Iteration Statements
"""

"""
13.8The continue Statement
Syntax
ContinueStatement[Yield, Await]:
continue;
continue[no LineTerminator here]LabelIdentifier[?Yield, ?Await];
"""
builder.r(w=1, d='ContinueStatement: continue;')

@builder.rule('ContinueStatement', w=1)
def _(m):
	""" ContinueStatement: continue LabelIdentifier; """
	name = m.ref_Id(t='LabelIdentifier')
	return 'continue %s;' % name

"""
13.9The break Statement
BreakStatement[Yield, Await]:
break;
break[no LineTerminator here]LabelIdentifier[?Yield, ?Await];
"""
builder.r(w=1, d='BreakStatement: break;')

@builder.rule('BreakStatement', w=1)
def _(m):
	""" BreakStatement: break LabelIdentifier; """
	name = m.ref_Id(t='LabelIdentifier')
	return 'break %s;' % name

"""
13.10 The return Statement
ReturnStatement[Yield, Await]:
return;
return[no LineTerminator here]Expression[+In, ?Yield, ?Await];
"""
builder.rule('ReturnStatement', w=1)
def _(m):
	""" ReturnStatement: return; """
	if not n.scope_under('function'):
		m.restart('ReturnStatement should under scope function')
	return 'return;'

builder.rule('ReturnStatement', w=10)
def _(m):
	""" ReturnStatement: return @Expression ; """
	if not n.scope_under('function'):
		m.restart('ReturnStatement should under scope function')
	s = m.make('Expression')
	return 'return %s;' % s

"""
13.11 The with Statement
WithStatement[Yield, Await, Return]:
with(Expression[+In, ?Yield, ?Await])Statement[?Yield, ?Await, ?Return]
"""
builder.r(w=1, d='WithStatement: with( @Expression ) @Statement')


"""
13.12The switch Statement
Syntax
SwitchStatement:
switch(Expression)CaseBlock 
CaseBlock:
	{CaseClauses opt}
	{CaseClauses opt DefaultClause CaseClauses opt}
CaseClauses:
CaseClause[?Yield, ?Await, ?Return]
CaseClauses[?Yield, ?Await, ?Return]CaseClause[?Yield, ?Await, ?Return]
CaseClause:
caseExpression:StatementList[?Yield, ?Await, ?Return]opt
DefaultClause:
default:StatementList[?Yield, ?Await, ?Return]opt
"""
builder.r(w=1, d='SwitchStatement: switch( @Expression ) @CaseBlock')

builder.r(w=1, d='CaseBlock: { }')
builder.r(w=1, d='CaseBlock: { @CaseClauses }')
builder.r(w=1, d='CaseBlock: { @DefaultClause }')
builder.r(w=1, d='CaseBlock: { @CaseClauses @DefaultClause }')
builder.r(w=1, d='CaseBlock: { @DefaultClause @CaseClauses }')
builder.r(w=1, d='CaseBlock: { @CaseClauses @DefaultClause @CaseClauses }')

builder.r(w=1, d='CaseClauses: @CaseClause')
builder.r(w=1, d='CaseClauses: @CaseClause @CaseClause')
builder.r(w=1, d='CaseClauses: @CaseClause @CaseClause @CaseClause')
@builder.rule('CaseClauses', w=1)
def _(m):
	""" ExpressionStatement: CaseClause xN """
	count = m.randint(4, 10)
	items = [ m.make('CaseClause') for x in range(0, count) ]
	return ' '.join(items)

builder.r(w=1, d='CaseClause: case @Expression :')
builder.r(w=1, d='CaseClause: case @Expression : @StatementList')

builder.r(w=1, d='DefaultClause: default:')
builder.r(w=1, d='DefaultClause: default: @StatementList')

"""
13.13Labelled Statements
Syntax
LabelledStatement[Yield, Await, Return]:
LabelIdentifier[?Yield, ?Await]:LabelledItem[?Yield, ?Await, ?Return]
LabelledItem[Yield, Await, Return]:
Statement[?Yield, ?Await, ?Return]
FunctionDeclaration[?Yield, ?Await, ~Default]
"""
@builder.rule('LabelledStatement', w=1)
def _(m):
	""" LabelledStatement: @LabelIdentifier: @LabelledItem """
	name = m.new_Id()
	s = m.make('LabelledItem')
	m.scope_set_Id(n=name, t='LabelIdentifier')
	return '%s: %s' % (name, s)

builder.r(w=1, d='LabelledItem: @Statement')
#[TODO]
#builder.r(w=1, d='LabelledItem: @FunctionDeclaration')

"""
13.14The throw Statement
Syntax
ThrowStatement[Yield, Await]:
throw[no LineTerminator here]Expression[+In, ?Yield, ?Await];
"""
#builder.r(w=1, d='ThrowStatement: throw @Expression ;')







