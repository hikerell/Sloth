from language import Builder
from language import Stage
from language import State
builder = Builder.get_builder()

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('FunctionDeclaration : `function` BindingIdentifier `(` FormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('FunctionDeclaration_Yield : `function` BindingIdentifier_Yield `(` FormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('FunctionDeclaration_Await : `function` BindingIdentifier_Await `(` FormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('FunctionDeclaration_Yield_Await : `function` BindingIdentifier_Yield_Await `(` FormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('FunctionDeclaration_Default : `function` BindingIdentifier `(` FormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('FunctionDeclaration_Yield_Default : `function` BindingIdentifier_Yield `(` FormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('FunctionDeclaration_Await_Default : `function` BindingIdentifier_Await `(` FormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('FunctionDeclaration_Yield_Await_Default : `function` BindingIdentifier_Yield_Await `(` FormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionDeclaration[Yield, Await, Default]  : [+Default] `function` `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('FunctionDeclaration_Default : `function` `(` FormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionDeclaration[Yield, Await, Default]  : [+Default] `function` `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('FunctionDeclaration_Yield_Default : `function` `(` FormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionDeclaration[Yield, Await, Default]  : [+Default] `function` `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('FunctionDeclaration_Await_Default : `function` `(` FormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionDeclaration[Yield, Await, Default]  : [+Default] `function` `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('FunctionDeclaration_Yield_Await_Default : `function` `(` FormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionExpression  : `function` BindingIdentifier[~Yield, ~Await]? `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('FunctionExpression : `function` `(` FormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionExpression  : `function` BindingIdentifier[~Yield, ~Await]? `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('FunctionExpression : `function` BindingIdentifier `(` FormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UniqueFormalParameters[Yield, Await]  : FormalParameters[?Yield, ?Await]
@builder.build('UniqueFormalParameters : FormalParameters')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UniqueFormalParameters[Yield, Await]  : FormalParameters[?Yield, ?Await]
@builder.build('UniqueFormalParameters_Yield : FormalParameters_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UniqueFormalParameters[Yield, Await]  : FormalParameters[?Yield, ?Await]
@builder.build('UniqueFormalParameters_Await : FormalParameters_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UniqueFormalParameters[Yield, Await]  : FormalParameters[?Yield, ?Await]
@builder.build('UniqueFormalParameters_Yield_Await : FormalParameters_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : ``
@builder.build('FormalParameters : ``')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : ``
@builder.build('FormalParameters_Yield : ``')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : ``
@builder.build('FormalParameters_Await : ``')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : ``
@builder.build('FormalParameters_Yield_Await : ``')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FunctionRestParameter[?Yield, ?Await]
@builder.build('FormalParameters : FunctionRestParameter')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FunctionRestParameter[?Yield, ?Await]
@builder.build('FormalParameters_Yield : FunctionRestParameter_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FunctionRestParameter[?Yield, ?Await]
@builder.build('FormalParameters_Await : FunctionRestParameter_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FunctionRestParameter[?Yield, ?Await]
@builder.build('FormalParameters_Yield_Await : FunctionRestParameter_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await]
@builder.build('FormalParameters : FormalParameterList')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await]
@builder.build('FormalParameters_Yield : FormalParameterList_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await]
@builder.build('FormalParameters_Await : FormalParameterList_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await]
@builder.build('FormalParameters_Yield_Await : FormalParameterList_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,`
@builder.build('FormalParameters : FormalParameterList `,`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,`
@builder.build('FormalParameters_Yield : FormalParameterList_Yield `,`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,`
@builder.build('FormalParameters_Await : FormalParameterList_Await `,`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,`
@builder.build('FormalParameters_Yield_Await : FormalParameterList_Yield_Await `,`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FunctionRestParameter[?Yield, ?Await]
@builder.build('FormalParameters : FormalParameterList `,` FunctionRestParameter')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FunctionRestParameter[?Yield, ?Await]
@builder.build('FormalParameters_Yield : FormalParameterList_Yield `,` FunctionRestParameter_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FunctionRestParameter[?Yield, ?Await]
@builder.build('FormalParameters_Await : FormalParameterList_Await `,` FunctionRestParameter_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FunctionRestParameter[?Yield, ?Await]
@builder.build('FormalParameters_Yield_Await : FormalParameterList_Yield_Await `,` FunctionRestParameter_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameterList[Yield, Await]  : FormalParameter[?Yield, ?Await]
@builder.build('FormalParameterList : FormalParameter')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameterList[Yield, Await]  : FormalParameter[?Yield, ?Await]
@builder.build('FormalParameterList_Yield : FormalParameter_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameterList[Yield, Await]  : FormalParameter[?Yield, ?Await]
@builder.build('FormalParameterList_Await : FormalParameter_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameterList[Yield, Await]  : FormalParameter[?Yield, ?Await]
@builder.build('FormalParameterList_Yield_Await : FormalParameter_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameterList[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FormalParameter[?Yield, ?Await]
@builder.build('FormalParameterList : FormalParameterList `,` FormalParameter')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameterList[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FormalParameter[?Yield, ?Await]
@builder.build('FormalParameterList_Yield : FormalParameterList_Yield `,` FormalParameter_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameterList[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FormalParameter[?Yield, ?Await]
@builder.build('FormalParameterList_Await : FormalParameterList_Await `,` FormalParameter_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameterList[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FormalParameter[?Yield, ?Await]
@builder.build('FormalParameterList_Yield_Await : FormalParameterList_Yield_Await `,` FormalParameter_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionRestParameter[Yield, Await]  : BindingRestElement[?Yield, ?Await]
@builder.build('FunctionRestParameter : BindingRestElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionRestParameter[Yield, Await]  : BindingRestElement[?Yield, ?Await]
@builder.build('FunctionRestParameter_Yield : BindingRestElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionRestParameter[Yield, Await]  : BindingRestElement[?Yield, ?Await]
@builder.build('FunctionRestParameter_Await : BindingRestElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionRestParameter[Yield, Await]  : BindingRestElement[?Yield, ?Await]
@builder.build('FunctionRestParameter_Yield_Await : BindingRestElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameter[Yield, Await]  : BindingElement[?Yield, ?Await]
@builder.build('FormalParameter : BindingElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameter[Yield, Await]  : BindingElement[?Yield, ?Await]
@builder.build('FormalParameter_Yield : BindingElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameter[Yield, Await]  : BindingElement[?Yield, ?Await]
@builder.build('FormalParameter_Await : BindingElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FormalParameter[Yield, Await]  : BindingElement[?Yield, ?Await]
@builder.build('FormalParameter_Yield_Await : BindingElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionBody[Yield, Await]  : FunctionStatementList[?Yield, ?Await]
#@builder.build('FunctionBody : FunctionStatementList')
@builder.build('FunctionBody : ``')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionBody[Yield, Await]  : FunctionStatementList[?Yield, ?Await]
#@builder.build('FunctionBody_Yield : FunctionStatementList_Yield')
@builder.build('FunctionBody_Yield : ``')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionBody[Yield, Await]  : FunctionStatementList[?Yield, ?Await]
#@builder.build('FunctionBody_Await : FunctionStatementList_Await')
@builder.build('FunctionBody_Await : ``')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionBody[Yield, Await]  : FunctionStatementList[?Yield, ?Await]
#@builder.build('FunctionBody_Yield_Await : FunctionStatementList_Yield_Await')
@builder.build('FunctionBody_Yield_Await : ``')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
@builder.build('FunctionStatementList : ``')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
@builder.build('FunctionStatementList : StatementList_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
@builder.build('FunctionStatementList_Yield : ``')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
@builder.build('FunctionStatementList_Yield : StatementList_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
@builder.build('FunctionStatementList_Await : ``')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
@builder.build('FunctionStatementList_Await : StatementList_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
@builder.build('FunctionStatementList_Yield_Await : ``')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
@builder.build('FunctionStatementList_Yield_Await : StatementList_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
@builder.build('ArrowFunction : ArrowParameters `=>` ConciseBody')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
@builder.build('ArrowFunction_In : ArrowParameters `=>` ConciseBody_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
@builder.build('ArrowFunction_Yield : ArrowParameters_Yield `=>` ConciseBody')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
@builder.build('ArrowFunction_In_Yield : ArrowParameters_Yield `=>` ConciseBody_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
@builder.build('ArrowFunction_Await : ArrowParameters_Await `=>` ConciseBody')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
@builder.build('ArrowFunction_In_Await : ArrowParameters_Await `=>` ConciseBody_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
@builder.build('ArrowFunction_Yield_Await : ArrowParameters_Yield_Await `=>` ConciseBody')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
@builder.build('ArrowFunction_In_Yield_Await : ArrowParameters_Yield_Await `=>` ConciseBody_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowParameters[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
@builder.build('ArrowParameters : BindingIdentifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowParameters[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
@builder.build('ArrowParameters_Yield : BindingIdentifier_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowParameters[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
@builder.build('ArrowParameters_Await : BindingIdentifier_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowParameters[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
@builder.build('ArrowParameters_Yield_Await : BindingIdentifier_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowParameters[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
@builder.build('ArrowParameters : CoverParenthesizedExpressionAndArrowParameterList')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowParameters[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
@builder.build('ArrowParameters_Yield : CoverParenthesizedExpressionAndArrowParameterList_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowParameters[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
@builder.build('ArrowParameters_Await : CoverParenthesizedExpressionAndArrowParameterList_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowParameters[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
@builder.build('ArrowParameters_Yield_Await : CoverParenthesizedExpressionAndArrowParameterList_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConciseBody[In]  :   AssignmentExpression[?In, ~Yield, ~Await]
@builder.build('ConciseBody : AssignmentExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConciseBody[In]  :   AssignmentExpression[?In, ~Yield, ~Await]
@builder.build('ConciseBody_In : AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConciseBody[In]  : `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('ConciseBody : `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConciseBody[In]  : `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('ConciseBody_In : `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowFormalParameters[Yield, Await]  : `(` UniqueFormalParameters[?Yield, ?Await] `)`
@builder.build('ArrowFormalParameters : `(` UniqueFormalParameters `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowFormalParameters[Yield, Await]  : `(` UniqueFormalParameters[?Yield, ?Await] `)`
@builder.build('ArrowFormalParameters_Yield : `(` UniqueFormalParameters_Yield `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowFormalParameters[Yield, Await]  : `(` UniqueFormalParameters[?Yield, ?Await] `)`
@builder.build('ArrowFormalParameters_Await : `(` UniqueFormalParameters_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrowFormalParameters[Yield, Await]  : `(` UniqueFormalParameters[?Yield, ?Await] `)`
@builder.build('ArrowFormalParameters_Yield_Await : `(` UniqueFormalParameters_Yield_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('MethodDefinition : PropertyName `(` UniqueFormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('MethodDefinition_Yield : PropertyName_Yield `(` UniqueFormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('MethodDefinition_Await : PropertyName_Await `(` UniqueFormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('MethodDefinition_Yield_Await : PropertyName_Yield_Await `(` UniqueFormalParameters `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : GeneratorMethod[?Yield, ?Await]
@builder.build('MethodDefinition : GeneratorMethod')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : GeneratorMethod[?Yield, ?Await]
@builder.build('MethodDefinition_Yield : GeneratorMethod_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : GeneratorMethod[?Yield, ?Await]
@builder.build('MethodDefinition_Await : GeneratorMethod_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : GeneratorMethod[?Yield, ?Await]
@builder.build('MethodDefinition_Yield_Await : GeneratorMethod_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : AsyncMethod[?Yield, ?Await]
@builder.build('MethodDefinition : AsyncMethod')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : AsyncMethod[?Yield, ?Await]
@builder.build('MethodDefinition_Yield : AsyncMethod_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : AsyncMethod[?Yield, ?Await]
@builder.build('MethodDefinition_Await : AsyncMethod_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : AsyncMethod[?Yield, ?Await]
@builder.build('MethodDefinition_Yield_Await : AsyncMethod_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : AsyncGeneratorMethod[?Yield, ?Await]
@builder.build('MethodDefinition : AsyncGeneratorMethod')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : AsyncGeneratorMethod[?Yield, ?Await]
@builder.build('MethodDefinition_Yield : AsyncGeneratorMethod_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : AsyncGeneratorMethod[?Yield, ?Await]
@builder.build('MethodDefinition_Await : AsyncGeneratorMethod_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : AsyncGeneratorMethod[?Yield, ?Await]
@builder.build('MethodDefinition_Yield_Await : AsyncGeneratorMethod_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : `get` PropertyName[?Yield, ?Await] `(` `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('MethodDefinition : `get` PropertyName `(` `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : `get` PropertyName[?Yield, ?Await] `(` `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('MethodDefinition_Yield : `get` PropertyName_Yield `(` `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : `get` PropertyName[?Yield, ?Await] `(` `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('MethodDefinition_Await : `get` PropertyName_Await `(` `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : `get` PropertyName[?Yield, ?Await] `(` `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('MethodDefinition_Yield_Await : `get` PropertyName_Yield_Await `(` `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : `set` PropertyName[?Yield, ?Await] `(` PropertySetParameterList `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('MethodDefinition : `set` PropertyName `(` PropertySetParameterList `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : `set` PropertyName[?Yield, ?Await] `(` PropertySetParameterList `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('MethodDefinition_Yield : `set` PropertyName_Yield `(` PropertySetParameterList `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : `set` PropertyName[?Yield, ?Await] `(` PropertySetParameterList `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('MethodDefinition_Await : `set` PropertyName_Await `(` PropertySetParameterList `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MethodDefinition[Yield, Await]  : `set` PropertyName[?Yield, ?Await] `(` PropertySetParameterList `)` `{` FunctionBody[~Yield, ~Await] `}`
@builder.build('MethodDefinition_Yield_Await : `set` PropertyName_Yield_Await `(` PropertySetParameterList `)` `{` FunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertySetParameterList  : FormalParameter[~Yield, ~Await]
@builder.build('PropertySetParameterList : FormalParameter')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorMethod[Yield, Await]  : `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorMethod : `*` PropertyName `(` UniqueFormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorMethod[Yield, Await]  : `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorMethod_Yield : `*` PropertyName_Yield `(` UniqueFormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorMethod[Yield, Await]  : `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorMethod_Await : `*` PropertyName_Await `(` UniqueFormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorMethod[Yield, Await]  : `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorMethod_Yield_Await : `*` PropertyName_Yield_Await `(` UniqueFormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorDeclaration : `function` `*` BindingIdentifier `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorDeclaration_Yield : `function` `*` BindingIdentifier_Yield `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorDeclaration_Await : `function` `*` BindingIdentifier_Await `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorDeclaration_Yield_Await : `function` `*` BindingIdentifier_Yield_Await `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorDeclaration_Default : `function` `*` BindingIdentifier `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorDeclaration_Yield_Default : `function` `*` BindingIdentifier_Yield `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorDeclaration_Await_Default : `function` `*` BindingIdentifier_Await `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorDeclaration_Yield_Await_Default : `function` `*` BindingIdentifier_Yield_Await `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorDeclaration[Yield, Await, Default]  : [+Default] `function` `*` `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorDeclaration_Default : `function` `*` `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorDeclaration[Yield, Await, Default]  : [+Default] `function` `*` `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorDeclaration_Yield_Default : `function` `*` `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorDeclaration[Yield, Await, Default]  : [+Default] `function` `*` `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorDeclaration_Await_Default : `function` `*` `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorDeclaration[Yield, Await, Default]  : [+Default] `function` `*` `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorDeclaration_Yield_Await_Default : `function` `*` `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorExpression  : `function` `*` BindingIdentifier[+Yield, ~Await]? `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorExpression : `function` `*` `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorExpression  : `function` `*` BindingIdentifier[+Yield, ~Await]? `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
@builder.build('GeneratorExpression : `function` `*` BindingIdentifier_Yield `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#GeneratorBody  : FunctionBody[+Yield, ~Await]
@builder.build('GeneratorBody : FunctionBody_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#YieldExpression[In, Await]  : `yield`
@builder.build('YieldExpression : `yield`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#YieldExpression[In, Await]  : `yield`
@builder.build('YieldExpression_In : `yield`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#YieldExpression[In, Await]  : `yield`
@builder.build('YieldExpression_Await : `yield`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#YieldExpression[In, Await]  : `yield`
@builder.build('YieldExpression_In_Await : `yield`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#YieldExpression[In, Await]  : `yield`  AssignmentExpression[?In, +Yield, ?Await]
@builder.build('YieldExpression : `yield` AssignmentExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#YieldExpression[In, Await]  : `yield`  AssignmentExpression[?In, +Yield, ?Await]
@builder.build('YieldExpression_In : `yield` AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#YieldExpression[In, Await]  : `yield`  AssignmentExpression[?In, +Yield, ?Await]
@builder.build('YieldExpression_Await : `yield` AssignmentExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#YieldExpression[In, Await]  : `yield`  AssignmentExpression[?In, +Yield, ?Await]
@builder.build('YieldExpression_In_Await : `yield` AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#YieldExpression[In, Await]  : `yield`  `*` AssignmentExpression[?In, +Yield, ?Await]
@builder.build('YieldExpression : `yield` `*` AssignmentExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#YieldExpression[In, Await]  : `yield`  `*` AssignmentExpression[?In, +Yield, ?Await]
@builder.build('YieldExpression_In : `yield` `*` AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#YieldExpression[In, Await]  : `yield`  `*` AssignmentExpression[?In, +Yield, ?Await]
@builder.build('YieldExpression_Await : `yield` `*` AssignmentExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#YieldExpression[In, Await]  : `yield`  `*` AssignmentExpression[?In, +Yield, ?Await]
@builder.build('YieldExpression_In_Await : `yield` `*` AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorMethod[Yield, Await]  : `async`  `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorMethod : `async` `*` PropertyName `(` UniqueFormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorMethod[Yield, Await]  : `async`  `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorMethod_Yield : `async` `*` PropertyName_Yield `(` UniqueFormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorMethod[Yield, Await]  : `async`  `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorMethod_Await : `async` `*` PropertyName_Await `(` UniqueFormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorMethod[Yield, Await]  : `async`  `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorMethod_Yield_Await : `async` `*` PropertyName_Yield_Await `(` UniqueFormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorDeclaration : `async` `function` `*` BindingIdentifier `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorDeclaration_Yield : `async` `function` `*` BindingIdentifier_Yield `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorDeclaration_Await : `async` `function` `*` BindingIdentifier_Await `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorDeclaration_Yield_Await : `async` `function` `*` BindingIdentifier_Yield_Await `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorDeclaration_Default : `async` `function` `*` BindingIdentifier `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorDeclaration_Yield_Default : `async` `function` `*` BindingIdentifier_Yield `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorDeclaration_Await_Default : `async` `function` `*` BindingIdentifier_Await `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorDeclaration_Yield_Await_Default : `async` `function` `*` BindingIdentifier_Yield_Await `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `*` `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorDeclaration_Default : `async` `function` `*` `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `*` `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorDeclaration_Yield_Default : `async` `function` `*` `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `*` `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorDeclaration_Await_Default : `async` `function` `*` `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `*` `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorDeclaration_Yield_Await_Default : `async` `function` `*` `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorExpression  : `async`  `function` `*` BindingIdentifier[+Yield, +Await]? `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorExpression : `async` `function` `*` `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorExpression  : `async`  `function` `*` BindingIdentifier[+Yield, +Await]? `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
@builder.build('AsyncGeneratorExpression : `async` `function` `*` BindingIdentifier_Yield_Await `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncGeneratorBody  : FunctionBody[+Yield, +Await]
@builder.build('AsyncGeneratorBody : FunctionBody_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
@builder.build('ClassDeclaration : `class` BindingIdentifier ClassTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
@builder.build('ClassDeclaration_Yield : `class` BindingIdentifier_Yield ClassTail_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
@builder.build('ClassDeclaration_Await : `class` BindingIdentifier_Await ClassTail_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
@builder.build('ClassDeclaration_Yield_Await : `class` BindingIdentifier_Yield_Await ClassTail_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
@builder.build('ClassDeclaration_Default : `class` BindingIdentifier ClassTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
@builder.build('ClassDeclaration_Yield_Default : `class` BindingIdentifier_Yield ClassTail_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
@builder.build('ClassDeclaration_Await_Default : `class` BindingIdentifier_Await ClassTail_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
@builder.build('ClassDeclaration_Yield_Await_Default : `class` BindingIdentifier_Yield_Await ClassTail_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassDeclaration[Yield, Await, Default]  : [+Default] `class` ClassTail[?Yield, ?Await]
@builder.build('ClassDeclaration_Default : `class` ClassTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassDeclaration[Yield, Await, Default]  : [+Default] `class` ClassTail[?Yield, ?Await]
@builder.build('ClassDeclaration_Yield_Default : `class` ClassTail_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassDeclaration[Yield, Await, Default]  : [+Default] `class` ClassTail[?Yield, ?Await]
@builder.build('ClassDeclaration_Await_Default : `class` ClassTail_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassDeclaration[Yield, Await, Default]  : [+Default] `class` ClassTail[?Yield, ?Await]
@builder.build('ClassDeclaration_Yield_Await_Default : `class` ClassTail_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
@builder.build('ClassExpression : `class` ClassTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
@builder.build('ClassExpression : `class` BindingIdentifier ClassTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
@builder.build('ClassExpression_Yield : `class` ClassTail_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
@builder.build('ClassExpression_Yield : `class` BindingIdentifier_Yield ClassTail_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
@builder.build('ClassExpression_Await : `class` ClassTail_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
@builder.build('ClassExpression_Await : `class` BindingIdentifier_Await ClassTail_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
@builder.build('ClassExpression_Yield_Await : `class` ClassTail_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
@builder.build('ClassExpression_Yield_Await : `class` BindingIdentifier_Yield_Await ClassTail_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail : `{` ClassBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail : ClassHeritage `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail : ClassHeritage `{` ClassBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail_Yield : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail_Yield : `{` ClassBody_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail_Yield : ClassHeritage_Yield `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail_Yield : ClassHeritage_Yield `{` ClassBody_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail_Await : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail_Await : `{` ClassBody_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail_Await : ClassHeritage_Await `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail_Await : ClassHeritage_Await `{` ClassBody_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail_Yield_Await : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail_Yield_Await : `{` ClassBody_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail_Yield_Await : ClassHeritage_Yield_Await `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
@builder.build('ClassTail_Yield_Await : ClassHeritage_Yield_Await `{` ClassBody_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassHeritage[Yield, Await]  : `extends` LeftHandSideExpression[?Yield, ?Await]
@builder.build('ClassHeritage : `extends` LeftHandSideExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassHeritage[Yield, Await]  : `extends` LeftHandSideExpression[?Yield, ?Await]
@builder.build('ClassHeritage_Yield : `extends` LeftHandSideExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassHeritage[Yield, Await]  : `extends` LeftHandSideExpression[?Yield, ?Await]
@builder.build('ClassHeritage_Await : `extends` LeftHandSideExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassHeritage[Yield, Await]  : `extends` LeftHandSideExpression[?Yield, ?Await]
@builder.build('ClassHeritage_Yield_Await : `extends` LeftHandSideExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassBody[Yield, Await]  : ClassElementList[?Yield, ?Await]
@builder.build('ClassBody : ClassElementList')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassBody[Yield, Await]  : ClassElementList[?Yield, ?Await]
@builder.build('ClassBody_Yield : ClassElementList_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassBody[Yield, Await]  : ClassElementList[?Yield, ?Await]
@builder.build('ClassBody_Await : ClassElementList_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassBody[Yield, Await]  : ClassElementList[?Yield, ?Await]
@builder.build('ClassBody_Yield_Await : ClassElementList_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElementList[Yield, Await]  : ClassElement[?Yield, ?Await]
@builder.build('ClassElementList : ClassElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElementList[Yield, Await]  : ClassElement[?Yield, ?Await]
@builder.build('ClassElementList_Yield : ClassElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElementList[Yield, Await]  : ClassElement[?Yield, ?Await]
@builder.build('ClassElementList_Await : ClassElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElementList[Yield, Await]  : ClassElement[?Yield, ?Await]
@builder.build('ClassElementList_Yield_Await : ClassElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElementList[Yield, Await]  : ClassElementList[?Yield, ?Await] ClassElement[?Yield, ?Await]
@builder.build('ClassElementList : ClassElementList ClassElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElementList[Yield, Await]  : ClassElementList[?Yield, ?Await] ClassElement[?Yield, ?Await]
@builder.build('ClassElementList_Yield : ClassElementList_Yield ClassElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElementList[Yield, Await]  : ClassElementList[?Yield, ?Await] ClassElement[?Yield, ?Await]
@builder.build('ClassElementList_Await : ClassElementList_Await ClassElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElementList[Yield, Await]  : ClassElementList[?Yield, ?Await] ClassElement[?Yield, ?Await]
@builder.build('ClassElementList_Yield_Await : ClassElementList_Yield_Await ClassElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElement[Yield, Await]  : MethodDefinition[?Yield, ?Await]
@builder.build('ClassElement : MethodDefinition')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElement[Yield, Await]  : MethodDefinition[?Yield, ?Await]
@builder.build('ClassElement_Yield : MethodDefinition_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElement[Yield, Await]  : MethodDefinition[?Yield, ?Await]
@builder.build('ClassElement_Await : MethodDefinition_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElement[Yield, Await]  : MethodDefinition[?Yield, ?Await]
@builder.build('ClassElement_Yield_Await : MethodDefinition_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElement[Yield, Await]  : `static` MethodDefinition[?Yield, ?Await]
@builder.build('ClassElement : `static` MethodDefinition')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElement[Yield, Await]  : `static` MethodDefinition[?Yield, ?Await]
@builder.build('ClassElement_Yield : `static` MethodDefinition_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElement[Yield, Await]  : `static` MethodDefinition[?Yield, ?Await]
@builder.build('ClassElement_Await : `static` MethodDefinition_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElement[Yield, Await]  : `static` MethodDefinition[?Yield, ?Await]
@builder.build('ClassElement_Yield_Await : `static` MethodDefinition_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElement[Yield, Await]  : `;`
@builder.build('ClassElement : `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElement[Yield, Await]  : `;`
@builder.build('ClassElement_Yield : `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElement[Yield, Await]  : `;`
@builder.build('ClassElement_Await : `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ClassElement[Yield, Await]  : `;`
@builder.build('ClassElement_Yield_Await : `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncFunctionDeclaration : `async` `function` BindingIdentifier `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncFunctionDeclaration_Yield : `async` `function` BindingIdentifier_Yield `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncFunctionDeclaration_Await : `async` `function` BindingIdentifier_Await `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncFunctionDeclaration_Yield_Await : `async` `function` BindingIdentifier_Yield_Await `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncFunctionDeclaration_Default : `async` `function` BindingIdentifier `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncFunctionDeclaration_Yield_Default : `async` `function` BindingIdentifier_Yield `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncFunctionDeclaration_Await_Default : `async` `function` BindingIdentifier_Await `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncFunctionDeclaration_Yield_Await_Default : `async` `function` BindingIdentifier_Yield_Await `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncFunctionDeclaration_Default : `async` `function` `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncFunctionDeclaration_Yield_Default : `async` `function` `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncFunctionDeclaration_Await_Default : `async` `function` `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncFunctionDeclaration_Yield_Await_Default : `async` `function` `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionExpression  : `async`  `function` `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncFunctionExpression : `async` `function` `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionExpression  : `async`  `function` BindingIdentifier[~Yield, +Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncFunctionExpression : `async` `function` BindingIdentifier_Await `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncMethod[Yield, Await]  : `async`  PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncMethod : `async` PropertyName `(` UniqueFormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncMethod[Yield, Await]  : `async`  PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncMethod_Yield : `async` PropertyName_Yield `(` UniqueFormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncMethod[Yield, Await]  : `async`  PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncMethod_Await : `async` PropertyName_Await `(` UniqueFormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncMethod[Yield, Await]  : `async`  PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
@builder.build('AsyncMethod_Yield_Await : `async` PropertyName_Yield_Await `(` UniqueFormalParameters_Await `)` `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncFunctionBody  : FunctionBody[~Yield, +Await]
@builder.build('AsyncFunctionBody : FunctionBody_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AwaitExpression[Yield]  : `await` UnaryExpression[?Yield, +Await]
@builder.build('AwaitExpression : `await` UnaryExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AwaitExpression[Yield]  : `await` UnaryExpression[?Yield, +Await]
@builder.build('AwaitExpression_Yield : `await` UnaryExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
@builder.build('AsyncArrowFunction : `async` AsyncArrowBindingIdentifier `=>` AsyncConciseBody')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
@builder.build('AsyncArrowFunction_In : `async` AsyncArrowBindingIdentifier `=>` AsyncConciseBody_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
@builder.build('AsyncArrowFunction_Yield : `async` AsyncArrowBindingIdentifier_Yield `=>` AsyncConciseBody')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
@builder.build('AsyncArrowFunction_In_Yield : `async` AsyncArrowBindingIdentifier_Yield `=>` AsyncConciseBody_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
@builder.build('AsyncArrowFunction_Await : `async` AsyncArrowBindingIdentifier `=>` AsyncConciseBody')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
@builder.build('AsyncArrowFunction_In_Await : `async` AsyncArrowBindingIdentifier `=>` AsyncConciseBody_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
@builder.build('AsyncArrowFunction_Yield_Await : `async` AsyncArrowBindingIdentifier_Yield `=>` AsyncConciseBody')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
@builder.build('AsyncArrowFunction_In_Yield_Await : `async` AsyncArrowBindingIdentifier_Yield `=>` AsyncConciseBody_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
@builder.build('AsyncArrowFunction : CoverCallExpressionAndAsyncArrowHead `=>` AsyncConciseBody')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
@builder.build('AsyncArrowFunction_In : CoverCallExpressionAndAsyncArrowHead `=>` AsyncConciseBody_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
@builder.build('AsyncArrowFunction_Yield : CoverCallExpressionAndAsyncArrowHead_Yield `=>` AsyncConciseBody')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
@builder.build('AsyncArrowFunction_In_Yield : CoverCallExpressionAndAsyncArrowHead_Yield `=>` AsyncConciseBody_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
@builder.build('AsyncArrowFunction_Await : CoverCallExpressionAndAsyncArrowHead_Await `=>` AsyncConciseBody')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
@builder.build('AsyncArrowFunction_In_Await : CoverCallExpressionAndAsyncArrowHead_Await `=>` AsyncConciseBody_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
@builder.build('AsyncArrowFunction_Yield_Await : CoverCallExpressionAndAsyncArrowHead_Yield_Await `=>` AsyncConciseBody')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
@builder.build('AsyncArrowFunction_In_Yield_Await : CoverCallExpressionAndAsyncArrowHead_Yield_Await `=>` AsyncConciseBody_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncConciseBody[In]  :   AssignmentExpression[?In, ~Yield, +Await]
@builder.build('AsyncConciseBody : AssignmentExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncConciseBody[In]  :   AssignmentExpression[?In, ~Yield, +Await]
@builder.build('AsyncConciseBody_In : AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncConciseBody[In]  : `{` AsyncFunctionBody `}`
@builder.build('AsyncConciseBody : `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncConciseBody[In]  : `{` AsyncFunctionBody `}`
@builder.build('AsyncConciseBody_In : `{` AsyncFunctionBody `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowBindingIdentifier[Yield]  : BindingIdentifier[?Yield, +Await]
@builder.build('AsyncArrowBindingIdentifier : BindingIdentifier_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowBindingIdentifier[Yield]  : BindingIdentifier[?Yield, +Await]
@builder.build('AsyncArrowBindingIdentifier_Yield : BindingIdentifier_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverCallExpressionAndAsyncArrowHead[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('CoverCallExpressionAndAsyncArrowHead : MemberExpression Arguments')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverCallExpressionAndAsyncArrowHead[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('CoverCallExpressionAndAsyncArrowHead_Yield : MemberExpression_Yield Arguments_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverCallExpressionAndAsyncArrowHead[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('CoverCallExpressionAndAsyncArrowHead_Await : MemberExpression_Await Arguments_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverCallExpressionAndAsyncArrowHead[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('CoverCallExpressionAndAsyncArrowHead_Yield_Await : MemberExpression_Yield_Await Arguments_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AsyncArrowHead  : `async`  ArrowFormalParameters[~Yield, +Await]
@builder.build('AsyncArrowHead : `async` ArrowFormalParameters_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

