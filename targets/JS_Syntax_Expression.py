from language import Builder

builder = Builder.get_builder()
rule = builder.rule

"""
#12.2Primary Expression
PrimaryExpression: this
PrimaryExpression: IdentifierReference
PrimaryExpression: Literal
PrimaryExpression: ArrayLiteral
PrimaryExpression: ObjectLiteral
PrimaryExpression: FunctionExpression
PrimaryExpression: ClassExpression
PrimaryExpression: GeneratorExpression
PrimaryExpression: AsyncFunctionExpression
PrimaryExpression: AsyncGeneratorExpression
#PrimaryExpression: RegularExpressionLiteral
PrimaryExpression: TemplateLiteral
PrimaryExpression: ParenthesizedExpression
"""

@builder.rule('PrimaryExpression', w=1)
def _(m):
	""" PrimaryExpression: this """
	return 'this'

@builder.rule('PrimaryExpression', w=1)
def _(m):
	""" PrimaryExpression: IdentifierReference """
	return m.ref_Id()

@builder.rule('PrimaryExpression', w=1)
def _(m):
	""" PrimaryExpression: Literal """
	return m.make('Literal')

@builder.rule('PrimaryExpression', w=1)
def _(m):
	""" PrimaryExpression: ArrayLiteral """
	return m.make('ArrayLiteral')

@builder.rule('PrimaryExpression', w=1)
def _(m):
	""" PrimaryExpression: ObjectLiteral """
	return m.make('ObjectLiteral')

@builder.rule('PrimaryExpression', w=1)
def _(m):
	""" PrimaryExpression: FunctionExpression """
	return m.make('FunctionExpression')

@builder.rule('PrimaryExpression', w=1)
def _(m):
	""" PrimaryExpression: ClassExpression """
	return m.make('ClassExpression')

@builder.rule('PrimaryExpression', w=1)
def _(m):
	""" PrimaryExpression: GeneratorExpression """
	return m.make('GeneratorExpression')

@builder.rule('PrimaryExpression', w=1)
def _(m):
	""" PrimaryExpression: AsyncFunctionExpression """
	return m.make('AsyncFunctionExpression')

@builder.rule('PrimaryExpression', w=1)
def _(m):
	""" PrimaryExpression: AsyncGeneratorExpression """
	return m.make('AsyncGeneratorExpression')

@builder.rule('PrimaryExpression', w=1)
def _(m):
	""" PrimaryExpression: TemplateLiteral """
	return m.make('TemplateLiteral')

@builder.rule('PrimaryExpression', w=1)
def _(m):
	""" PrimaryExpression: ParenthesizedExpression """
	return m.make('ParenthesizedExpression')

"""
ParenthesizedExpression[Yield, Await]:
(Expression[+In, ?Yield, ?Await])
"""
@builder.rule('ParenthesizedExpression', w=1)
def _(m):
	""" ParenthesizedExpression: Expression """
	return '(%s)' % m.make('Expression')

"""
@CoverParenthesizedExpressionAndArrowParameterList: (@Expression)
@CoverParenthesizedExpressionAndArrowParameterList: (@Expression,)
@CoverParenthesizedExpressionAndArrowParameterList: ()
@CoverParenthesizedExpressionAndArrowParameterList: (...@BindingIdentifier)
@CoverParenthesizedExpressionAndArrowParameterList: (...@BindingPattern)
@CoverParenthesizedExpressionAndArrowParameterList: (@Expression,...@BindingIdentifier)
@CoverParenthesizedExpressionAndArrowParameterList: (@Expression,...@BindingPattern)
"""

@builder.rule('CoverParenthesizedExpressionAndArrowParameterList', w=1)
def _(m):
	""" @CoverParenthesizedExpressionAndArrowParameterList: (@Expression) """
	return '(%s)' % m.make('Expression')

@builder.rule('CoverParenthesizedExpressionAndArrowParameterList', w=1)
def _(m):
	""" @CoverParenthesizedExpressionAndArrowParameterList: (@Expression,) """
	return '(%s,)' % m.make('Expression')

@builder.rule('CoverParenthesizedExpressionAndArrowParameterList', w=1)
def _(m):
	""" @CoverParenthesizedExpressionAndArrowParameterList: () """
	return '()'

@builder.rule('CoverParenthesizedExpressionAndArrowParameterList', w=1)
def _(m):
	""" @CoverParenthesizedExpressionAndArrowParameterList: (...BindingIdentifier) """
	n = m.ref_Id()
	return '(...%s)' % n

#[TODO]
@builder.rule('CoverParenthesizedExpressionAndArrowParameterList', w=1)
def _(m):
	""" @CoverParenthesizedExpressionAndArrowParameterList: (...BindingPattern) """
	n = m.ref_Id()
	return '(...%s)' % n

@builder.rule('CoverParenthesizedExpressionAndArrowParameterList', w=1)
def _(m):
	""" @CoverParenthesizedExpressionAndArrowParameterList: (Expression, ...BindingIdentifier) """
	e = m.make('Expression')
	n = m.ref_Id()
	return '(%s, ...%s)' %(e, n)

@builder.rule('CoverParenthesizedExpressionAndArrowParameterList', w=1)
def _(m):
	""" @CoverParenthesizedExpressionAndArrowParameterList: (Expression, ...BindingPattern) """
	e = m.make('Expression')
	n = m.ref_Id()	
	return '(%s, ...%s)' %(e, n)
"""
#12.2.4
Literal: NullLiteral
Literal: BooleanLiteral
Literal: NumericLiteral
Literal: StringLiteral
"""
@builder.rule('Literal', w=1)
def _(m):
	""" Literal: NullLiteral """
	return 'null'

@builder.rule('Literal', w=1)
def _(m):
	""" Literal: BooleanLiteral """
	literals = ['true', 'false']
	return m.choice(literals)

@builder.rule('Literal', w=1)
def _(m):
	""" Literal: NumericLiteral """
	return m.make('NumericLiteral')

@builder.rule('Literal', w=1)
def _(m):
	""" Literal: StringLiteral """
	return m.make('StringLiteral')

"""
#12.2.5 Array Initializer
ArrayLiteral: []
ArrayLiteral: [ Elision ]
ArrayLiteral: [ ElementList ]
ArrayLiteral: [ ElementList, ]
ArrayLiteral: [ ElementList, Elision ]
"""
@builder.rule('ArrayLiteral', w=1)
def _(m):
	""" ArrayLiteral: [] """
	return '[]'

@builder.rule('ArrayLiteral', w=1)
def _(m):
	""" ArrayLiteral: [ Elision ] """
	s = '[%s]' % m.make('Elision')
	return s

@builder.rule('ArrayLiteral', w=1)
def _(m):
	""" ArrayLiteral: [ ElementList ] """
	s = '[%s]' % m.make('ElementList')
	return s

@builder.rule('ArrayLiteral', w=1)
def _(m):
	""" ArrayLiteral: [ ElementList, ] """
	s = '[%s,]' % m.make('ElementList')
	return s

@builder.rule('ArrayLiteral', w=1)
def _(m):
	""" ArrayLiteral: [ ElementList, Elision ] """
	s = '[%s, %s]' % (m.make('ElementList'), m.make('Elision'))
	return s

"""
ElementList: AssignmentExpression
ElementList: Elision AssignmentExpression
ElementList: SpreadElement
ElementList: Elision @SpreadElement
ElementList: ElementList, AssignmentExpression
ElementList: ElementList, Elision AssignmentExpression
ElementList: ElementList, SpreadElement
ElementList: ElementList, Elision SpreadElement
"""
@builder.rule('ElementList', w=1)
def _(m):
	""" ElementList: AssignmentExpression """
	return m.make('AssignmentExpression')

@builder.rule('ElementList', w=1)
def _(m):
	""" ElementList: Elision AssignmentExpression """
	return m.make('Elision')+' '+m.make('AssignmentExpression')

@builder.rule('ElementList', w=1)
def _(m):
	""" ElementList: SpreadElement """
	return m.make('SpreadElement')

@builder.rule('ElementList', w=1)
def _(m):
	""" ElementList: Elision SpreadElement """
	return m.make('Elision')+' '+m.make('SpreadElement')

@builder.rule('ElementList', w=1)
def _(m):
	""" ElementList: ElementList, AssignmentExpression """
	return m.make('ElementList')+', '+m.make('AssignmentExpression')

@builder.rule('ElementList', w=1)
def _(m):
	""" ElementList: ElementList, Elision AssignmentExpression """
	return m.make('ElementList')+', '+m.make('Elision')+' '+m.make('AssignmentExpression')

@builder.rule('ElementList', w=1)
def _(m):
	""" ElementList: ElementList, SpreadElement """
	return m.make('ElementList')+', '+m.make('SpreadElement')

@builder.rule('ElementList', w=1)
def _(m):
	""" ElementList: ElementList, Elision SpreadElement """
	return m.make('ElementList')+', '+m.make('Elision')+' '+m.make('SpreadElement')

"""
Elision: ,
Elision: Elision,

SpreadElement: ...AssignmentExpression
"""
@builder.rule('Elision', w=1)
def _(m):
	""" Elision: , """
	return ','

@builder.rule('Elision', w=1)
def _(m):
	""" Elision: Elision, """
	return m.make('Elision')+','

@builder.rule('SpreadElement', w=1)
def _(m):
	""" SpreadElement: ...@AssignmentExpression """
	return '...'+m.make('AssignmentExpression')

"""
#12.2.6 Object Initializer
ObjectLiteral: {}
ObjectLiteral: {PropertyDefinitionList}
ObjectLiteral: {PropertyDefinitionList,}
"""
@builder.rule('ObjectLiteral', w=1)
def _(m):
	""" ObjectLiteral: {} """
	return '{}'

@builder.rule('ObjectLiteral', w=1)
def _(m):
	""" ObjectLiteral: {@PropertyDefinitionList} """
	return '{%s}' % m.make('PropertyDefinitionList')

@builder.rule('ObjectLiteral', w=1)
def _(m):
	""" ObjectLiteral: {@PropertyDefinitionList,} """
	return '{%s,}' % m.make('PropertyDefinitionList')

"""
PropertyDefinitionList: PropertyDefinition
PropertyDefinitionList: PropertyDefinitionList, PropertyDefinition
"""
@builder.rule('PropertyDefinitionList', w=1)
def _(m):
	""" PropertyDefinitionList: PropertyDefinition """
	return m.make('PropertyDefinition')

@builder.rule('PropertyDefinitionList', w=1)
def _(m):
	""" PropertyDefinitionList: PropertyDefinitionList, PropertyDefinition """
	return '%s,%s' % (m.make('PropertyDefinitionList'), m.make('PropertyDefinition'))

"""
PropertyDefinition: IdentifierReference
PropertyDefinition: CoverInitializedName
PropertyDefinition: PropertyName: AssignmentExpression
PropertyDefinition: MethodDefinition
PropertyDefinition: ...AssignmentExpression
"""
#@builder.rule('PropertyDefinition', w=1)
def _(m):
	""" PropertyDefinition: IdentifierReference """
	return m.ref_Id()

#[TODO] safari and chrome not support well
#@builder.rule('PropertyDefinition', w=1)
def _(m):
	""" PropertyDefinition: CoverInitializedName """
	return m.make('CoverInitializedName')

@builder.rule('PropertyDefinition', w=1)
def _(m):
	""" PropertyDefinition: PropertyName: AssignmentExpression """
	return '%s: %s' % (m.make('PropertyName'), m.make('AssignmentExpression'))

#[TODO] where is MethodDefinition
@builder.rule('PropertyDefinition', w=1)
def _(m):
	""" PropertyDefinition: MethodDefinition """
	return m.make('MethodDefinition')

#@builder.rule('PropertyDefinition', w=1)
def _(m):
	""" PropertyDefinition: ...AssignmentExpression """
	return '...%s' % m.make('AssignmentExpression')

"""
PropertyName: LiteralPropertyName
PropertyName: ComputedPropertyName
"""
@builder.rule('PropertyName', w=1)
def _(m):
	""" PropertyName: LiteralPropertyName """
	return m.make('LiteralPropertyName')

@builder.rule('PropertyName', w=1)
def _(m):
	""" PropertyName: ComputedPropertyName """
	return m.make('ComputedPropertyName')

"""
LiteralPropertyName: IdentifierName
LiteralPropertyName: StringLiteral
LiteralPropertyName: NumericLiteral
"""
#[TODO]
@builder.rule('LiteralPropertyName', w=1)
def _(m):
	""" LiteralPropertyName: IdentifierName """
	return m.make('IdentifierName')

@builder.rule('LiteralPropertyName', w=1)
def _(m):
	""" LiteralPropertyName: StringLiteral """
	return m.make('StringLiteral')

@builder.rule('LiteralPropertyName', w=1)
def _(m):
	""" LiteralPropertyName: NumericLiteral """
	return m.make('NumericLiteral')
"""
@ComputedPropertyName: [@AssignmentExpression]
@CoverInitializedName: IdentifierReference @Initializer
@Initializer: = @AssignmentExpression
"""
@builder.rule('ComputedPropertyName', w=1)
def _(m):
	""" ComputedPropertyName: [ AssignmentExpression ] """
	return '[%s]' % m.make('AssignmentExpression')

@builder.rule('CoverInitializedName', w=1)
def _(m):
	""" CoverInitializedName: IdentifierReference Initializer """
	return '%s%s' %( m.ref_Id(), m.make('Initializer') )

@builder.rule('Initializer', w=1)
def _(m):
	""" Initializer: = AssignmentExpression """
	return '=%s' % m.make('AssignmentExpression')	
"""
#14.1 Function Definitions
@FunctionDeclaration: function BindingIdentifier(@FormalParameters){@FunctionBody}
@FunctionDeclaration: function(@FormalParameters){@FunctionBody}
"""
@builder.rule('FunctionDeclaration', w=1)
def _(m):
	""" @FunctionDeclaration: function BindingIdentifier(@FormalParameters){@FunctionBody} """
	s='function %s(%s){%s}'
	funcname = m.new_Id()
	m.scope_set_Id(n=funcname, t='function')
	m.scope_enter(tags=['function'])
	params = m.make('FormalParameters')
	funcbody = m.make('FunctionBody')
	m.scope_exit()
	return s % (funcname, params, funcbody)

#@builder.rule('FunctionDeclaration', w=1)
def _(m):
	""" @FunctionDeclaration: function (@FormalParameters){@FunctionBody} """
	s='function (%s){%s}'
	m.scope_enter(tags=['function'])
	params = m.make('FormalParameters')
	funcbody = m.make('FunctionBody')
	m.scope_exit()
	return s % (params, funcbody)

"""
@FunctionExpression: function (@FormalParameters){@FunctionBody}
@FunctionExpression: function BindingIdentifier(@FormalParameters){@FunctionBody}
"""
@builder.rule('FunctionExpression', w=1)
def _(m):
	""" @FunctionExpression: function (@FormalParameters){@FunctionBody} """
	s='function (%s){%s}'
	m.scope_enter(tags=['function'])
	params = m.make('FormalParameters')
	funcbody = m.make('FunctionBody')
	m.scope_exit()
	return s % (params, funcbody)

@builder.rule('FunctionExpression', w=1)
def _(m):
	""" @FunctionExpression: function BindingIdentifier(@FormalParameters){@FunctionBody} """
	s='function %s(%s){%s}'
	funcname = m.new_Id()
	m.scope_set_Id(n=funcname, t='function')
	m.scope_enter(tags=['function'])
	params = m.make('FormalParameters')
	funcbody = m.make('FunctionBody')
	m.scope_exit()
	return s % (funcname, params, funcbody)

"""
@UniqueFormalParameters: @FormalParameters

@FormalParameters: $empty()
@FormalParameters: @FunctionRestParameter
@FormalParameters: @FormalParameterList
@FormalParameters: @FormalParameterList,
@FormalParameters: @FormalParameterList, @FunctionRestParameter

@FormalParameterList: @FormalParameter
@FormalParameterList: @FormalParameterList, @FormalParameter

@FunctionRestParameter: @BindingRestElement

@FormalParameter: @BindingElement
"""
@builder.rule('UniqueFormalParameters', w=1)
def _(m):
	""" @UniqueFormalParameters: @FormalParameters """
	return m.make('FormalParameters')

#[TODO]
@builder.rule('FormalParameters', w=1)
def _(m):
	""" @FormalParameters:  """
	rnd = m.randint(0, 2)
	if rnd==0:
		return ''
	elif rnd == 1:
		m.scope_set_Id(n='p1', t='param')
		m.scope_set_Id(n='p2', t='param')
		return 'p1, p2'
	return ''
"""
@FunctionBody: @FunctionStatementList

@FunctionStatementList: $empty()
@FunctionStatementList: @StatementList
"""
@builder.rule('FunctionBody', w=1)
def _(m):
	""" @FunctionBody: @FunctionStatementList """
	return m.make('FunctionStatementList')

@builder.rule('FunctionStatementList', w=1)
def _(m):
	""" @FunctionStatementList: $empty() """
	return ''

@builder.rule('FunctionStatementList', w=1)
def _(m):
	""" @FunctionStatementList: @StatementList """
	return m.make('StatementList')

"""
#14.2 Arrow Function Definitions
ArrowFunction: ArrowParameters=>ConciseBody
"""
@builder.rule('ArrowFunction', w=1)
def _(m):
	""" ArrowFunction: ArrowParameters=>ConciseBody """
	s='%s=>%s'
	m.scope_enter(tags=['arrow_function'])
	params = m.make('ArrowParameters')
	funcbody = m.make('ConciseBody')
	m.scope_exit()
	return s % (params, funcbody)
"""
ArrowParameters: BindingIdentifier
ArrowParameters: (UniqueFormalParameters)
"""
@builder.rule('ArrowParameters', w=1)
def _(m):
	""" ArrowParameters: BindingIdentifier """
	m.scope_set_Id(n='p1', t='param')
	return 'p1'

@builder.rule('ArrowParameters', w=1)
def _(m):
	""" ArrowParameters: (UniqueFormalParameters) """
	return '(%s)' % m.make('UniqueFormalParameters')

"""
ConciseBody: AssignmentExpression
ConciseBody: { FunctionBody }
"""
@builder.rule('ConciseBody', w=1)
def _(m):
	""" ConciseBody: AssignmentExpression """
	return m.make('AssignmentExpression')

@builder.rule('ConciseBody', w=1)
def _(m):
	""" ConciseBody: FunctionBody """
	return '{%s}' % m.make('FunctionBody')

"""
#14.4 Generator Function Definitions
@GeneratorMethod: *PropertyName(@UniqueFormalParameters){@GeneratorBody}

@GeneratorDeclaration: function * (@FormalParameters){@GeneratorBody}
@GeneratorDeclaration: function * BindingIdentifier(@FormalParameters){@GeneratorBody}
"""

"""
@GeneratorExpression: function * (@FormalParameters){@GeneratorBody}
@GeneratorExpression: function * BindingIdentifier(@FormalParameters){@GeneratorBody}
"""
@builder.rule('GeneratorExpression', w=1)
def _(m):
	""" @GeneratorExpression: function * (@FormalParameters){@GeneratorBody} """
	s='function * (%s){%s}'
	m.scope_enter(tags=['function'])
	params = m.make('FormalParameters')
	funcbody = m.make('GeneratorBody')
	m.scope_exit()
	return s % (params, funcbody)

@builder.rule('GeneratorExpression', w=1)
def _(m):
	""" @GeneratorExpression: function * BindingIdentifier(@FormalParameters){@GeneratorBody} """
	s='function * %s(%s){%s}'
	funcname = m.new_Id()
	m.scope_set_Id(n=funcname, t='function')
	m.scope_enter(tags=['function'])
	params = m.make('FormalParameters')
	funcbody = m.make('GeneratorBody')
	m.scope_exit()
	return s % (funcname, params, funcbody)
"""
@GeneratorBody: @FunctionBody
"""
@builder.rule('GeneratorBody', w=1)
def _(m):
	""" @GeneratorBody: @FunctionBody """
	return m.make('FunctionBody')

"""
@YieldExpression: yield
@YieldExpression: yield @AssignmentExpression
@YieldExpression: yield * @AssignmentExpression
"""
@builder.rule('YieldExpression', w=1)
def _(m):
	""" @YieldExpression: yield """
	return 'yield'

@builder.rule('YieldExpression', w=1)
def _(m):
	""" @YieldExpression: yield @AssignmentExpression """
	return 'yield %s' % m.make('AssignmentExpression')

@builder.rule('YieldExpression', w=1)
def _(m):
	""" @YieldExpression: yield * @AssignmentExpression """
	return 'yield * %s' % m.make('AssignmentExpression')
"""
#14.6 Class Definitions
@ClassDeclaration: class BindingIdentifier @ClassTail
@ClassDeclaration: class @ClassTail
"""
@builder.rule('ClassDeclaration', w=1)
def _(m):
	""" @ClassDeclaration: class @ClassTail """
	tpl='class %s'
	t = m.make('ClassTail')
	return tpl % t

@builder.rule('ClassDeclaration', w=1)
def _(m):
	""" @ClassDeclaration: class BindingIdentifier @ClassTail """
	tpl='class %s %s'
	n = m.new_Id()
	m.scope_set_Id(n=n, t='class')
	t = m.make('ClassTail')
	return tpl % (n, t)

"""
@ClassExpression: class @ClassTail
@ClassExpression: class BindingIdentifier @ClassTail
"""
@builder.rule('ClassExpression', w=1)
def _(m):
	""" @ClassExpression: class @ClassTail """
	tpl='class %s'
	t = m.make('ClassTail')
	return tpl % t

@builder.rule('ClassExpression', w=1)
def _(m):
	""" @ClassExpression: class BindingIdentifier @ClassTail """
	tpl='class %s %s'
	n = m.new_Id()
	m.scope_set_Id(n=n, t='class')
	t = m.make('ClassTail')
	return tpl % (n, t)
"""
@ClassTail: {}
@ClassTail: {@ClassBody}
@ClassTail: @ClassHeritage{}
@ClassTail: @ClassHeritage{@ClassBody}
"""
@builder.rule('ClassTail', w=1)
def _(m):
	""" @ClassTail: {} """
	return '{ }'

@builder.rule('ClassTail', w=1)
def _(m):
	""" @ClassTail: {@ClassBody} """
	m.scope_enter(tags=['class'])
	body = m.make('ClassBody')
	m.scope_exit()
	return '{ %s }' % body

@builder.rule('ClassTail', w=1)
def _(m):
	""" @ClassTail: @ClassHeritage{} """
	h = m.make('ClassHeritage')
	return '%s{ }' % h

@builder.rule('ClassTail', w=1)
def _(m):
	""" @ClassTail: @ClassHeritage{@ClassBody} """
	m.scope_enter(tags=['class', 'derive_class'])
	h = m.make('ClassHeritage')
	body = m.make('ClassBody')
	m.scope_exit()
	return '%s{ %s }' % (h, body)
"""
@ClassHeritage: extends @LeftHandSideExpression 
"""
@builder.rule('ClassHeritage', w=1)
def _(m):
	""" hacked ClassHeritage: extends @LeftHandSideExpression  """
	#base = m.make('LeftHandSideExpression')
	base = m.make('BuiltInBaseClass')
	return 'extends %s' % base

"""
@ClassBody: @ClassElementList
"""
@builder.rule('ClassBody', w=1)
def _(m):
	""" @ClassBody: @ClassElementList """
	class_element_list = m.make('ClassElementList')
	return class_element_list

"""
@ClassElementList: @ClassElement 
@ClassElementList: @ClassElementList @ClassElement 

@ClassElement: @MethodDefinition 
@ClassElement: static @MethodDefinition 
@ClassElement: ;
"""

@builder.rule('ClassElementList', w=1)
def _(m):
	""" @ClassElementList: constructor(){} """
	m.scope_enter(tags=['function', 'method', 'constructor'])
	s = m.choice(['constructor(){ %s }', 'constructor(){ super(arguments); %s}'])
	stamtments = m.make('StatementList')
	m.scope_exit()
	return s % stamtments

"""
14.7Async Function Definitions
Syntax
AsyncFunctionDeclaration[Yield, Await, Default]:
async[no LineTerminator here]functionBindingIdentifier[?Yield, ?Await](FormalParameters[~Yield, +Await]){AsyncFunctionBody}
[+Default]async[no LineTerminator here]function(FormalParameters[~Yield, +Await]){AsyncFunctionBody}
AsyncFunctionExpression:
async[no LineTerminator here]function(FormalParameters[~Yield, +Await]){AsyncFunctionBody}
async[no LineTerminator here]functionBindingIdentifier[~Yield, +Await](FormalParameters[~Yield, +Await]){AsyncFunctionBody}
AsyncMethod[Yield, Await]:
async[no LineTerminator here]PropertyName[?Yield, ?Await](UniqueFormalParameters[~Yield, +Await]){AsyncFunctionBody}
AsyncFunctionBody: FunctionBody
AwaitExpression: await UnaryExpression
"""
@builder.rule('AsyncFunctionBody', w=1)
def _(m):
	""" AsyncFunctionBody: FunctionBody """
	return m.make('FunctionBody')

"""
#14.8 Async Arrow Function Definitions
Syntax
AsyncArrowFunction: async AsyncArrowBindingIdentifier=>AsyncConciseBody
AsyncArrowFunction: CoverCallExpressionAndAsyncArrowHead=>AsyncConciseBody
"""
@builder.rule('AsyncArrowFunction', w=1)
def _(m):
	""" AsyncArrowFunction: async AsyncArrowBindingIdentifier=>AsyncConciseBody """
	s='async %s=>%s'
	m.scope_enter(tags=['async_arrow_function'])
	params = m.make('AsyncArrowBindingIdentifier')
	funcbody = m.make('AsyncConciseBody')
	m.scope_exit()
	return s % (params, funcbody)

@builder.rule('AsyncArrowFunction', w=1)
def _(m):
	""" AsyncArrowFunction: AsyncArrowHead=>AsyncConciseBody """
	s='%s=>%s'
	m.scope_enter(tags=['async_arrow_function'])
	head = m.make('AsyncArrowHead')
	body = m.make('AsyncConciseBody')
	m.scope_exit()
	return s % (head, body)

"""
AsyncConciseBody: AssignmentExpression
AsyncConciseBody: {AsyncFunctionBody}
"""
@builder.rule('AsyncConciseBody', w=1)
def _(m):
	""" AsyncConciseBody: AssignmentExpression """
	return m.make('AssignmentExpression')

@builder.rule('AsyncConciseBody', w=1)
def _(m):
	""" AsyncConciseBody: {AsyncFunctionBody} """
	return '{ %s }' % m.make('AsyncFunctionBody')

"""
AsyncArrowBindingIdentifier: BindingIdentifier
CoverCallExpressionAndAsyncArrowHead: MemberExpression Arguments
AsyncArrowHead: async (UniqueFormalParameters)
"""
@builder.rule('AsyncArrowBindingIdentifier', w=1)
def _(m):
	""" AsyncArrowBindingIdentifier: BindingIdentifier """
	m.scope_set_Id(n='p1')
	return 'p1'

@builder.rule('CoverCallExpressionAndAsyncArrowHead', w=1)
def _(m):
	""" CoverCallExpressionAndAsyncArrowHead: MemberExpression Arguments """
	return '%s%s'%(m.make('MemberExpression'), m.make('Arguments'))

@builder.rule('AsyncArrowHead', w=1)
def _(m):
	""" AsyncArrowHead: async (UniqueFormalParameters) """
	return 'async (%s)'% m.make('UniqueFormalParameters')

"""
#12.3 Left-Hand-Side Expressions
@MemberExpression: @PrimaryExpression
@MemberExpression: @PrimaryExpression [ 0,1,2,3,4 ] # add add by expression
@MemberExpression: @PrimaryExpression [ 'prop' ] # add by expression
@MemberExpression: IdentifierName [ 0,1,2,3,4 ] # add add by expression
@MemberExpression: IdentifierName [ 'prop' ] # add by expression
@MemberExpression: @MemberExpression [ @Expression ]
@MemberExpression: @MemberExpression.IdentifierName
@MemberExpression: @MemberExpression @TemplateLiteral
@MemberExpression: @SuperProperty
@MemberExpression: @MetaProperty
@MemberExpression: new @MemberExpression @Arguments
"""

@builder.rule('MemberExpression', w=20)
def _(m):
	""" MemberExpression: PrimaryExpression """
	return m.make('PrimaryExpression')

@builder.rule('MemberExpression', w=20)
def _(m):
	""" MemberExpression: PrimaryExpression [ 0,1,2,3,4 ] # add add by expression """
	name = m.make('PrimaryExpression')
	idx = m.choice([0,1,2, 0xFFFF])
	return '%s[%d]' % (name, idx)

@builder.rule('MemberExpression', w=20)
def _(m):
	""" MemberExpression: PrimaryExpression [ 'prop' ] # add by expression """
	name = m.make('PrimaryExpression')
	prop = m.make('StringLiteral')
	return '%s[%s]' % (name, prop)

@builder.rule('MemberExpression', w=20)
def _(m):
	""" MemberExpression: IdentifierName [ 0,1,2,3,4 ] # add add by expression """
	name = m.ref_Id()
	idx = m.choice([0,1,2, 0xFFFF])
	return '%s[%d]' % (name, idx)

@builder.rule('MemberExpression', w=20)
def _(m):
	""" MemberExpression: IdentifierName [ 'prop' ] # add by expression """
	name = m.ref_Id()
	prop = m.make('StringLiteral')
	return '%s[%s]' % (name, prop)

@builder.rule('MemberExpression', w=1)
def _(m):
	""" MemberExpression: MemberExpression [ Expression] """
	s_me = m.make('MemberExpression')
	s_e = m.make('Expression')
	return '%s[%s]' % (s_me, s_e)

@builder.rule('MemberExpression', w=1)
def _(m):
	""" MemberExpression: MemberExpression.IdentifierName """
	s_me = m.make('MemberExpression')
	s_in = m.make('IdentifierName')
	return '%s[%s]' % (s_me, s_in)

@builder.rule('MemberExpression', w=1)
def _(m):
	""" MemberExpression: @MemberExpression @TemplateLiteral """
	s_me = m.make('MemberExpression')
	s_tl = m.make('TemplateLiteral')
	return '%s[%s]' % (s_me, s_tl)

@builder.rule('MemberExpression', w=1)
def _(m):
	""" MemberExpression: SuperProperty """
	if not (m.scope_under('class.method') or m.scope_under('objectliteral.method')):
		m.restart('SuperProperty should under scope class.method')
	return m.make('SuperProperty')

@builder.rule('MemberExpression', w=1)
def _(m):
	""" MemberExpression: MetaProperty """
	return m.make('MetaProperty')

@builder.rule('MemberExpression', w=1)
def _(m):
	""" MemberExpression: new @MemberExpression @Arguments """
	s_1 = m.make('MemberExpression')
	s_2 = m.make('Arguments')
	return 'new %s%s' % (s_1, s_2)

"""
@SuperProperty: super[@Expression]
@SuperProperty: super.IdentifierName
"""

@builder.rule('SuperProperty', w=1)
def _(m):
	""" SuperProperty: super[ Expression ] """
	s = m.make('Expression')
	return 'super[%s]' % s

@builder.rule('SuperProperty', w=1)
def _(m):
	""" SuperProperty: super.IdentifierName """
	s = m.make('IdentifierName')
	return 'super.%s' % s

"""
@MetaProperty: @NewTarget
@NewTarget: new.target
"""
@builder.rule('MetaProperty', w=1)
def _(m):
	""" MetaProperty: NewTarget """
	return m.make('NewTarget')

@builder.rule('NewTarget', w=1)
def _(m):
	""" NewTarget: new.target """
	if not m.scope_under('function'):
		m.restart('NewTarget not in function scope')
	#print('')
	#m.debug_show_scope_stack()
	#m.debug_show_AST()
	#print('')
	return 'new.target'

"""
@NewExpression: @MemberExpression
@NewExpression: new @NewExpression
"""
@builder.rule('NewExpression', w=1)
def _(m):
	""" NewExpression: MemberExpression """
	return m.make('MemberExpression')

@builder.rule('NewExpression', w=1)
def _(m):
	""" fixed BNF => NewExpression: new MemberExpression"""
	return 'new %s' % m.make('MemberExpression')

"""
@CallExpression: @BuiltInFunctionCall
@CallExpression: @CoverCallExpressionAndAsyncArrowHead
@CallExpression: @SuperCall
@CallExpression: @CallExpression @Arguments
@CallExpression: @CallExpression[@Expression]
@CallExpression: @CallExpression.IdentifierName
@CallExpression: @CallExpression @TemplateLiteral
"""
@builder.rule('CallExpression', w=50)
def _(m):
	""" CallExpression: BuiltInFunctionCall """
	return m.make_builtin_call()

@builder.rule('CallExpression', w=1)
def _(m):
	""" CallExpression: CoverCallExpressionAndAsyncArrowHead """
	return m.make('CoverCallExpressionAndAsyncArrowHead')

@builder.rule('CallExpression', w=1)
def _(m):
	""" CallExpression: SuperCall"""
	return m.make('SuperCall')

@builder.rule('CallExpression', w=1)
def _(m):
	""" CallExpression: CallExpression Arguments """
	s_1 = m.make('CallExpression')
	s_2 = m.make('Arguments')
	return '%s%s' % (s_1, s_2)

@builder.rule('CallExpression', w=1)
def _(m):
	""" CallExpression: CallExpression[ Expression ] """
	s_1 = m.make('CallExpression')
	s_2 = m.make('Expression')
	return '%s[%s]' % (s_1, s_2)

@builder.rule('CallExpression', w=1)
def _(m):
	""" CallExpression: CallExpression.IdentifierName """
	s_1 = m.make('CallExpression')
	s_2 = m.make('IdentifierName')
	return '%s.%s' % (s_1, s_2)

@builder.rule('CallExpression', w=1)
def _(m):
	""" CallExpression: CallExpression TemplateLiteral """
	s_1 = m.make('CallExpression')
	s_2 = m.make('TemplateLiteral')
	return '%s%s' % (s_1, s_2)

"""
@SuperCall: super @Arguments
"""
@builder.rule('SuperCall', w=1)
def _(m):
	""" SuperCall: super @Arguments """
	if not m.scope_under('derive_class.constructor'):
		#print('SuperCall should under scope derive_class.constructor')
		m.restart('SuperCall should under scope derive_class.constructor')
	s_1 = m.make('Arguments')
	return 'super %s' % s_1

"""
@Arguments: ()
@Arguments: (@ArgumentList)
@Arguments: (@ArgumentList,)

@ArgumentList: @AssignmentExpression
@ArgumentList: ...@AssignmentExpression
@ArgumentList: @ArgumentList, @AssignmentExpression
@ArgumentList: @ArgumentList, ...@AssignmentExpression
"""
@builder.rule('Arguments', w=1)
def _(m):
	""" fake Arguments """
	return '()'

@builder.rule('Arguments', w=1)
def _(m):
	""" fake Arguments """
	return '(%s)' % m.make('ArgumentList')

@builder.rule('Arguments', w=1)
def _(m):
	""" fake Arguments """
	return '(%s,)' % m.make('ArgumentList')

@builder.rule('ArgumentList', w=10)
def _(m):
	""" ArgumentList: @Hacked_ArgumentID"""
	count = m.randint(1, 6)
	args = [ m.make('Hacked_ArgumentID') for x in range(0, count) ]
	return ','.join(args)

@builder.rule('ArgumentList', w=1)
def _(m):
	""" ArgumentList: @Hacked_ArgumentID"""
	count = m.randint(1, 6)
	args = [ m.make('Hacked_ArgumentAE') for x in range(0, count) ]
	return ','.join(args)

@builder.rule('Hacked_ArgumentAE', w=1)
def _(m):
	""" Hacked_ArgumentAE: @AssignmentExpression"""
	return m.make('AssignmentExpression')

@builder.rule('Hacked_ArgumentAE', w=1)
def _(m):
	""" Hacked_ArgumentAE: ...@AssignmentExpression"""
	return '...%s' % m.make('AssignmentExpression')

@builder.rule('Hacked_ArgumentID', w=1)
def _(m):
	""" Hacked_ArgumentID: ID | ...ID """
	a = m.ref_Id()
	return m.choice(['%s' % a, '...%s' % a])
"""
@LeftHandSideExpression: @NewExpression
@LeftHandSideExpression: @CallExpression
"""

@builder.rule('LeftHandSideExpression', w=1)
def _(m):
	""" LeftHandSideExpression: NewExpression """
	return m.make('NewExpression')

@builder.rule('LeftHandSideExpression', w=1)
def _(m):
	""" LeftHandSideExpression: CallExpression """
	return m.make('CallExpression')

"""
#12.4 - 12.15
@UpdateExpression: @LeftHandSideExpression 
@UpdateExpression: @LeftHandSideExpression ++
@UpdateExpression: @LeftHandSideExpression --
@UpdateExpression: ++ @UnaryExpression 
@UpdateExpression: -- @UnaryExpression 
"""
@builder.rule('UpdateExpression', w=10)
def _(m):
	""" UpdateExpression: LeftHandSideExpression """
	return m.make('LeftHandSideExpression')

@builder.rule('UpdateExpression', w=1)
def _(m):
	""" UpdateExpression: LeftHandSideExpression ++ """
	return '%s ++' % m.make('LeftHandSideExpression')

@builder.rule('UpdateExpression', w=1)
def _(m):
	""" UpdateExpression: LeftHandSideExpression -- """
	return '%s --' % m.make('LeftHandSideExpression')

@builder.rule('UpdateExpression', w=1)
def _(m):
	""" UpdateExpression: ++ UnaryExpression """
	return '++ %s' % m.make('UnaryExpression')

@builder.rule('UpdateExpression', w=1)
def _(m):
	""" UpdateExpression: -- UnaryExpression """
	return '-- %s' % m.make('UnaryExpression')
"""
@UnaryExpression: @UpdateExpression 
@UnaryExpression: delete @UnaryExpression 
@UnaryExpression: void @UnaryExpression 
@UnaryExpression: typeof @UnaryExpression 
@UnaryExpression: + @UnaryExpression 
@UnaryExpression: - @UnaryExpression 
@UnaryExpression: ~ @UnaryExpression 
@UnaryExpression: ! @UnaryExpression 
@UnaryExpression: @Expression
"""
@builder.rule('UnaryExpression', w=10)
def _(m):
	""" UnaryExpression: UpdateExpression """
	return '%s' % m.make('UpdateExpression')

@builder.rule('UnaryExpression', w=1)
def _(m):
	""" UnaryExpression: delete UnaryExpression """
	return 'delete %s' % m.make('UnaryExpression')

@builder.rule('UnaryExpression', w=1)
def _(m):
	""" UnaryExpression: void UnaryExpression """
	return 'void %s' % m.make('UnaryExpression')

@builder.rule('UnaryExpression', w=1)
def _(m):
	""" UnaryExpression: typeof UnaryExpression """
	return 'typeof %s' % m.make('UnaryExpression')

@builder.rule('UnaryExpression', w=1)
def _(m):
	""" UnaryExpression: + UnaryExpression """
	return '+ %s' % m.make('UnaryExpression')

@builder.rule('UnaryExpression', w=1)
def _(m):
	""" UnaryExpression: - UnaryExpression """
	return '- %s' % m.make('UnaryExpression')

@builder.rule('UnaryExpression', w=1)
def _(m):
	""" UnaryExpression: ~ UnaryExpression """
	return '~ %s' % m.make('UnaryExpression')

@builder.rule('UnaryExpression', w=1)
def _(m):
	""" UnaryExpression: ! UnaryExpression """
	return '! %s' % m.make('UnaryExpression')

@builder.rule('UnaryExpression', w=1)
def _(m):
	""" UnaryExpression: Expression """
	return '%s' % m.make('Expression')

"""
@ExponentiationExpression: @UnaryExpression 
@ExponentiationExpression: @UpdateExpression ** @ExponentiationExpression 
"""
@builder.rule('ExponentiationExpression', w=10)
def _(m):
	""" ExponentiationExpression: UnaryExpression """
	return '%s' % m.make('UnaryExpression')

@builder.rule('ExponentiationExpression', w=1)
def _(m):
	""" ExponentiationExpression: UpdateExpression ** ExponentiationExpression """
	return '%s ** %s' % (m.make('UpdateExpression'), m.make('ExponentiationExpression'))
"""
@MultiplicativeExpression: @ExponentiationExpression 
@MultiplicativeExpression: @MultiplicativeExpression @MultiplicativeOperator @ExponentiationExpression 

@MultiplicativeOperator: $OneOf(all="*,/,%")
"""
@builder.rule('MultiplicativeExpression', w=10)
def _(m):
	""" MultiplicativeExpression: ExponentiationExpression """
	return '%s' % m.make('ExponentiationExpression')

@builder.rule('MultiplicativeExpression', w=1)
def _(m):
	""" MultiplicativeExpression: MultiplicativeExpression MultiplicativeOperator ExponentiationExpression """
	return '%s%s%s' % (m.make('MultiplicativeExpression'), m.make('MultiplicativeOperator'), m.make('ExponentiationExpression'))

@builder.rule('MultiplicativeOperator', w=1)
def _(m):
	""" MultiplicativeOperator: $OneOf(all="*,/,%") """
	return '%s' % m.choice(['*', '/', '%'])
"""
@AdditiveExpression: @MultiplicativeExpression 
@AdditiveExpression: @AdditiveExpression + @MultiplicativeExpression 
@AdditiveExpression: @AdditiveExpression - @MultiplicativeExpression 
"""
@builder.rule('AdditiveExpression', w=10)
def _(m):
	""" AdditiveExpression: MultiplicativeExpression """
	return '%s' % m.make('MultiplicativeExpression')

@builder.rule('AdditiveExpression', w=1)
def _(m):
	""" AdditiveExpression: AdditiveExpression + @MultiplicativeExpression """
	op = m.choice(['+', '-'])
	return '%s%s%s' % (m.make('AdditiveExpression'), op, m.make('MultiplicativeExpression'))

"""
@ShiftExpression: @AdditiveExpression 
@ShiftExpression: @ShiftExpression << @AdditiveExpression 
@ShiftExpression: @ShiftExpression >> @AdditiveExpression 
@ShiftExpression: @ShiftExpression >>> @AdditiveExpression 
"""
@builder.rule('ShiftExpression', w=10)
def _(m):
	""" ShiftExpression: AdditiveExpression """
	return '%s' % m.make('AdditiveExpression')

@builder.rule('ShiftExpression', w=1)
def _(m):
	""" ShiftExpression: ShiftExpression + @AdditiveExpression """
	op = m.choice(['<<', '>>', '>>>'])
	return '%s%s%s' % (m.make('ShiftExpression'), op, m.make('AdditiveExpression'))

"""
@RelationalExpression: @ShiftExpression 
@RelationalExpression: @RelationalExpression < @ShiftExpression 
@RelationalExpression: @RelationalExpression > @ShiftExpression 
@RelationalExpression: @RelationalExpression <= @ShiftExpression 
@RelationalExpression: @RelationalExpression >= @ShiftExpression 
@RelationalExpression: @RelationalExpression instanceof @ShiftExpression 
@RelationalExpression: @RelationalExpression in @ShiftExpression 
"""
@builder.rule('RelationalExpression', w=10)
def _(m):
	""" RelationalExpression: ShiftExpression """
	return '%s' % m.make('ShiftExpression')

@builder.rule('RelationalExpression', w=1)
def _(m):
	""" RelationalExpression: RelationalExpression + @ShiftExpression """
	op = m.choice(['<', '>', '<=', '>=', 'instanceof', 'in'])
	return '%s%s%s' % (m.make('RelationalExpression'), op, m.make('ShiftExpression'))

"""
@EqualityExpression: @RelationalExpression 
@EqualityExpression: @EqualityExpression == @RelationalExpression 
@EqualityExpression: @EqualityExpression != @RelationalExpression 
@EqualityExpression: @EqualityExpression === @RelationalExpression 
@EqualityExpression: @EqualityExpression !== @RelationalExpression 
"""
@builder.rule('EqualityExpression', w=10)
def _(m):
	""" EqualityExpression: RelationalExpression """
	return '%s' % m.make('RelationalExpression')

@builder.rule('EqualityExpression', w=1)
def _(m):
	""" EqualityExpression: EqualityExpression + @RelationalExpression """
	op = m.choice(['==', '!=', '===', '!=='])
	return '%s%s%s' % (m.make('EqualityExpression'), op, m.make('RelationalExpression'))

"""
@BitwiseExpression: @EqualityExpression 
@BitwiseExpression: @BitwiseExpression & @EqualityExpression 
@BitwiseExpression: @BitwiseExpression ^ @EqualityExpression 
@BitwiseExpression: @BitwiseExpression | @EqualityExpression 
"""
@builder.rule('BitwiseExpression', w=10)
def _(m):
	""" BitwiseExpression: EqualityExpression """
	return '%s' % m.make('EqualityExpression')

@builder.rule('BitwiseExpression', w=1)
def _(m):
	""" BitwiseExpression: BitwiseExpression + @EqualityExpression """
	op = m.choice(['&', '^', '|'])
	return '%s%s%s' % (m.make('BitwiseExpression'), op, m.make('EqualityExpression'))

"""
@LogicalExpression: @BitwiseExpression 
@LogicalExpression: @LogicalExpression && @BitwiseExpression 
@LogicalExpression: @LogicalExpression || @BitwiseExpression 
"""
@builder.rule('LogicalExpression', w=10)
def _(m):
	""" LogicalExpression: BitwiseExpression """
	return '%s' % m.make('BitwiseExpression')

@builder.rule('LogicalExpression', w=1)
def _(m):
	""" LogicalExpression: LogicalExpression + @BitwiseExpression """
	op = m.choice(['&&', '||'])
	return '%s%s%s' % (m.make('LogicalExpression'), op, m.make('BitwiseExpression'))

"""
@ConditionalExpression: @LogicalExpression 
@ConditionalExpression: @LogicalExpression ? @AssignmentExpression: @AssignmentExpression 
"""

@builder.rule('ConditionalExpression', w=10)
def _(m):
	""" ConditionalExpression: LogicalExpression """
	return '%s' % m.make('LogicalExpression')

@builder.rule('ConditionalExpression', w=1)
def _(m):
	""" ConditionalExpression: @LogicalExpression ? @AssignmentExpression: @AssignmentExpression """
	return '%s?%s:%s' % (m.make('LogicalExpression'), m.make('AssignmentExpression'), m.make('AssignmentExpression'))

"""
@AssignmentExpression: @ConditionalExpression 
@AssignmentExpression: @YieldExpression
@AssignmentExpression: @ArrowFunction 
@AssignmentExpression: @AsyncArrowFunction 
@AssignmentExpression: @LeftHandSideExpression = @AssignmentExpression 
@AssignmentExpression: @LeftHandSideExpression @AssignmentOperator @AssignmentExpression 
@AssignmentOperator: $OneOf(all="*=,/=,%=,+=,-=,<<=,>>=,>>>=,&=,^=,|=,**=")
"""
@builder.rule('AssignmentExpression', w=50)
def _(m):
	""" AssignmentExpression: LeftHandSideExpression """
	return m.make('LeftHandSideExpression')

@builder.rule('AssignmentExpression', w=1)
def _(m):
	""" AssignmentExpression: ConditionalExpression """
	return m.make('ConditionalExpression')

@builder.rule('AssignmentExpression', w=1)
def _(m):
	""" AssignmentExpression: ArrowFunction """
	return m.make('ArrowFunction')

@builder.rule('AssignmentExpression', w=1)
def _(m):
	""" AssignmentExpression: AsyncArrowFunction """
	return m.make('AsyncArrowFunction')

#[TODO] fix
@builder.rule('AssignmentExpression', w=1)
def _(m):
	""" AssignmentExpression: LeftHandSideExpression = AssignmentExpression  """
	name = m.new_Id()
	op = '='
	value = m.make('AssignmentExpression')
	m.scope_set_Id(n=name)
	return '%s%s%s' % (name, op, value)

#[TODO] fix
@builder.rule('AssignmentExpression', w=1)
def _(m):
	""" AssignmentExpression: LeftHandSideExpression AssignmentOperator AssignmentExpression """
	name = m.ref_Id()
	op = m.make('AssignmentOperator')
	value = m.make('AssignmentExpression')
	return '%s%s%s' % (name, op, value)

@builder.rule('AssignmentOperator', w=1)
def _(m):
	""" AssignmentOperator: $OneOf(all="*=,/=,%=,+=,-=,<<=,>>=,>>>=,&=,^=,|=,**=") """
	ops = ['*=','/=','%=','+=','-=','<<=','>>=','>>>=','&=','^=','|=','**=']
	return m.choice(ops)

"""
# 12.16Comma Operator ( , )
@Expression: @AssignmentExpression 
@Expression: @Expression, @AssignmentExpression 
"""

@builder.rule('Expression', w=10)
def _(m):
	""" Expression: AssignmentExpression """
	return m.make('AssignmentExpression')

@builder.rule('Expression', w=1)
def _(m):
	""" Expression: Expression, AssignmentExpression """
	return m.make('Expression') + ',' + m.make('AssignmentExpression')

@builder.rule('Expression', w=10)
def _(m):
	""" Expression: BuiltInExpression """
	return m.make_builtin()
