from language import Builder
from language import Stage
from language import State
builder = Builder.get_builder()

#IdentifierReference[Yield, Await]  : Identifier
@builder.build('IdentifierReference : Identifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IdentifierReference[Yield, Await]  : Identifier
@builder.build('IdentifierReference_Yield : Identifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IdentifierReference[Yield, Await]  : Identifier
@builder.build('IdentifierReference_Await : Identifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IdentifierReference[Yield, Await]  : Identifier
@builder.build('IdentifierReference_Yield_Await : Identifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IdentifierReference[Yield, Await]  : [~Yield] `yield`
@builder.build('IdentifierReference : `yield`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IdentifierReference[Yield, Await]  : [~Yield] `yield`
@builder.build('IdentifierReference_Await : `yield`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IdentifierReference[Yield, Await]  : [~Await] `await`
@builder.build('IdentifierReference : `await`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IdentifierReference[Yield, Await]  : [~Await] `await`
@builder.build('IdentifierReference_Yield : `await`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingIdentifier[Yield, Await]  : Identifier
@builder.build('BindingIdentifier : Identifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingIdentifier[Yield, Await]  : Identifier
@builder.build('BindingIdentifier_Yield : Identifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingIdentifier[Yield, Await]  : Identifier
@builder.build('BindingIdentifier_Await : Identifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingIdentifier[Yield, Await]  : Identifier
@builder.build('BindingIdentifier_Yield_Await : Identifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingIdentifier[Yield, Await]  : `yield`
@builder.build('BindingIdentifier : `yield`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingIdentifier[Yield, Await]  : `yield`
@builder.build('BindingIdentifier_Yield : `yield`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingIdentifier[Yield, Await]  : `yield`
@builder.build('BindingIdentifier_Await : `yield`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingIdentifier[Yield, Await]  : `yield`
@builder.build('BindingIdentifier_Yield_Await : `yield`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingIdentifier[Yield, Await]  : `await`
@builder.build('BindingIdentifier : `await`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingIdentifier[Yield, Await]  : `await`
@builder.build('BindingIdentifier_Yield : `await`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingIdentifier[Yield, Await]  : `await`
@builder.build('BindingIdentifier_Await : `await`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingIdentifier[Yield, Await]  : `await`
@builder.build('BindingIdentifier_Yield_Await : `await`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelIdentifier[Yield, Await]  : Identifier
@builder.build('LabelIdentifier : Identifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelIdentifier[Yield, Await]  : Identifier
@builder.build('LabelIdentifier_Yield : Identifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelIdentifier[Yield, Await]  : Identifier
@builder.build('LabelIdentifier_Await : Identifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelIdentifier[Yield, Await]  : Identifier
@builder.build('LabelIdentifier_Yield_Await : Identifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelIdentifier[Yield, Await]  : [~Yield] `yield`
@builder.build('LabelIdentifier : `yield`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelIdentifier[Yield, Await]  : [~Yield] `yield`
@builder.build('LabelIdentifier_Await : `yield`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelIdentifier[Yield, Await]  : [~Await] `await`
@builder.build('LabelIdentifier : `await`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelIdentifier[Yield, Await]  : [~Await] `await`
@builder.build('LabelIdentifier_Yield : `await`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Identifier  : IdentifierName
@builder.build('Identifier : IdentifierName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : `this`
@builder.build('PrimaryExpression : `this`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : `this`
@builder.build('PrimaryExpression_Yield : `this`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : `this`
@builder.build('PrimaryExpression_Await : `this`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : `this`
@builder.build('PrimaryExpression_Yield_Await : `this`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : IdentifierReference[?Yield, ?Await]
@builder.build('PrimaryExpression : IdentifierReference')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : IdentifierReference[?Yield, ?Await]
@builder.build('PrimaryExpression_Yield : IdentifierReference_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : IdentifierReference[?Yield, ?Await]
@builder.build('PrimaryExpression_Await : IdentifierReference_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : IdentifierReference[?Yield, ?Await]
@builder.build('PrimaryExpression_Yield_Await : IdentifierReference_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : Literal
@builder.build('PrimaryExpression : Literal')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : Literal
@builder.build('PrimaryExpression_Yield : Literal')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : Literal
@builder.build('PrimaryExpression_Await : Literal')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : Literal
@builder.build('PrimaryExpression_Yield_Await : Literal')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : ArrayLiteral[?Yield, ?Await]
@builder.build('PrimaryExpression : ArrayLiteral')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : ArrayLiteral[?Yield, ?Await]
@builder.build('PrimaryExpression_Yield : ArrayLiteral_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : ArrayLiteral[?Yield, ?Await]
@builder.build('PrimaryExpression_Await : ArrayLiteral_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : ArrayLiteral[?Yield, ?Await]
@builder.build('PrimaryExpression_Yield_Await : ArrayLiteral_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : ObjectLiteral[?Yield, ?Await]
@builder.build('PrimaryExpression : ObjectLiteral')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : ObjectLiteral[?Yield, ?Await]
@builder.build('PrimaryExpression_Yield : ObjectLiteral_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : ObjectLiteral[?Yield, ?Await]
@builder.build('PrimaryExpression_Await : ObjectLiteral_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : ObjectLiteral[?Yield, ?Await]
@builder.build('PrimaryExpression_Yield_Await : ObjectLiteral_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : FunctionExpression
@builder.build('PrimaryExpression : FunctionExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : FunctionExpression
@builder.build('PrimaryExpression_Yield : FunctionExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : FunctionExpression
@builder.build('PrimaryExpression_Await : FunctionExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : FunctionExpression
@builder.build('PrimaryExpression_Yield_Await : FunctionExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : ClassExpression[?Yield, ?Await]
@builder.build('PrimaryExpression : ClassExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : ClassExpression[?Yield, ?Await]
@builder.build('PrimaryExpression_Yield : ClassExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : ClassExpression[?Yield, ?Await]
@builder.build('PrimaryExpression_Await : ClassExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : ClassExpression[?Yield, ?Await]
@builder.build('PrimaryExpression_Yield_Await : ClassExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : GeneratorExpression
@builder.build('PrimaryExpression : GeneratorExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : GeneratorExpression
@builder.build('PrimaryExpression_Yield : GeneratorExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : GeneratorExpression
@builder.build('PrimaryExpression_Await : GeneratorExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : GeneratorExpression
@builder.build('PrimaryExpression_Yield_Await : GeneratorExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : AsyncFunctionExpression
@builder.build('PrimaryExpression : AsyncFunctionExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : AsyncFunctionExpression
@builder.build('PrimaryExpression_Yield : AsyncFunctionExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : AsyncFunctionExpression
@builder.build('PrimaryExpression_Await : AsyncFunctionExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : AsyncFunctionExpression
@builder.build('PrimaryExpression_Yield_Await : AsyncFunctionExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : AsyncGeneratorExpression
@builder.build('PrimaryExpression : AsyncGeneratorExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : AsyncGeneratorExpression
@builder.build('PrimaryExpression_Yield : AsyncGeneratorExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : AsyncGeneratorExpression
@builder.build('PrimaryExpression_Await : AsyncGeneratorExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : AsyncGeneratorExpression
@builder.build('PrimaryExpression_Yield_Await : AsyncGeneratorExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : RegularExpressionLiteral
@builder.build('PrimaryExpression : RegularExpressionLiteral')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : RegularExpressionLiteral
@builder.build('PrimaryExpression_Yield : RegularExpressionLiteral')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : RegularExpressionLiteral
@builder.build('PrimaryExpression_Await : RegularExpressionLiteral')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : RegularExpressionLiteral
@builder.build('PrimaryExpression_Yield_Await : RegularExpressionLiteral')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : TemplateLiteral[?Yield, ?Await, ~Tagged]
@builder.build('PrimaryExpression : TemplateLiteral')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : TemplateLiteral[?Yield, ?Await, ~Tagged]
@builder.build('PrimaryExpression_Yield : TemplateLiteral_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : TemplateLiteral[?Yield, ?Await, ~Tagged]
@builder.build('PrimaryExpression_Await : TemplateLiteral_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : TemplateLiteral[?Yield, ?Await, ~Tagged]
@builder.build('PrimaryExpression_Yield_Await : TemplateLiteral_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
@builder.build('PrimaryExpression : CoverParenthesizedExpressionAndArrowParameterList')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
@builder.build('PrimaryExpression_Yield : CoverParenthesizedExpressionAndArrowParameterList_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
@builder.build('PrimaryExpression_Await : CoverParenthesizedExpressionAndArrowParameterList_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PrimaryExpression[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
@builder.build('PrimaryExpression_Yield_Await : CoverParenthesizedExpressionAndArrowParameterList_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList : `(` Expression_In `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Yield : `(` Expression_In_Yield `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Await : `(` Expression_In_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Yield_Await : `(` Expression_In_Yield_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList : `(` Expression_In `,` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Yield : `(` Expression_In_Yield `,` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Await : `(` Expression_In_Await `,` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Yield_Await : `(` Expression_In_Yield_Await `,` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList : `(` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Yield : `(` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Await : `(` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Yield_Await : `(` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingIdentifier[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList : `(` `...` BindingIdentifier `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingIdentifier[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Yield : `(` `...` BindingIdentifier_Yield `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingIdentifier[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Await : `(` `...` BindingIdentifier_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingIdentifier[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Yield_Await : `(` `...` BindingIdentifier_Yield_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingPattern[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList : `(` `...` BindingPattern `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingPattern[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Yield : `(` `...` BindingPattern_Yield `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingPattern[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Await : `(` `...` BindingPattern_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingPattern[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Yield_Await : `(` `...` BindingPattern_Yield_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingIdentifier[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList : `(` Expression_In `,` `...` BindingIdentifier `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingIdentifier[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Yield : `(` Expression_In_Yield `,` `...` BindingIdentifier_Yield `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingIdentifier[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Await : `(` Expression_In_Await `,` `...` BindingIdentifier_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingIdentifier[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Yield_Await : `(` Expression_In_Yield_Await `,` `...` BindingIdentifier_Yield_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingPattern[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList : `(` Expression_In `,` `...` BindingPattern `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingPattern[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Yield : `(` Expression_In_Yield `,` `...` BindingPattern_Yield `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingPattern[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Await : `(` Expression_In_Await `,` `...` BindingPattern_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingPattern[?Yield, ?Await] `)`
@builder.build('CoverParenthesizedExpressionAndArrowParameterList_Yield_Await : `(` Expression_In_Yield_Await `,` `...` BindingPattern_Yield_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ParenthesizedExpression[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
@builder.build('ParenthesizedExpression : `(` Expression_In `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ParenthesizedExpression[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
@builder.build('ParenthesizedExpression_Yield : `(` Expression_In_Yield `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ParenthesizedExpression[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
@builder.build('ParenthesizedExpression_Await : `(` Expression_In_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ParenthesizedExpression[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
@builder.build('ParenthesizedExpression_Yield_Await : `(` Expression_In_Yield_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Literal  : NullLiteral
@builder.build('Literal : NullLiteral')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Literal  : BooleanLiteral
@builder.build('Literal : BooleanLiteral')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Literal  : NumericLiteral
@builder.build('Literal : NumericLiteral')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Literal  : StringLiteral
@builder.build('Literal : StringLiteral')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
@builder.build('ArrayLiteral : `[` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
@builder.build('ArrayLiteral : `[` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
@builder.build('ArrayLiteral_Yield : `[` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
@builder.build('ArrayLiteral_Yield : `[` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
@builder.build('ArrayLiteral_Await : `[` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
@builder.build('ArrayLiteral_Await : `[` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
@builder.build('ArrayLiteral_Yield_Await : `[` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
@builder.build('ArrayLiteral_Yield_Await : `[` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `]`
@builder.build('ArrayLiteral : `[` ElementList `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `]`
@builder.build('ArrayLiteral_Yield : `[` ElementList_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `]`
@builder.build('ArrayLiteral_Await : `[` ElementList_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `]`
@builder.build('ArrayLiteral_Yield_Await : `[` ElementList_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
@builder.build('ArrayLiteral : `[` ElementList `,` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
@builder.build('ArrayLiteral : `[` ElementList `,` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
@builder.build('ArrayLiteral_Yield : `[` ElementList_Yield `,` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
@builder.build('ArrayLiteral_Yield : `[` ElementList_Yield `,` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
@builder.build('ArrayLiteral_Await : `[` ElementList_Await `,` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
@builder.build('ArrayLiteral_Await : `[` ElementList_Await `,` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
@builder.build('ArrayLiteral_Yield_Await : `[` ElementList_Yield_Await `,` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
@builder.build('ArrayLiteral_Yield_Await : `[` ElementList_Yield_Await `,` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList : AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList : Elision AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList_Yield : AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList_Yield : Elision AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList_Await : AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList_Await : Elision AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList_Yield_Await : AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList_Yield_Await : Elision AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList : SpreadElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList : Elision SpreadElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList_Yield : SpreadElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList_Yield : Elision SpreadElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList_Await : SpreadElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList_Await : Elision SpreadElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList_Yield_Await : SpreadElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList_Yield_Await : Elision SpreadElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList : ElementList `,` AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList : ElementList `,` Elision AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList_Yield : ElementList_Yield `,` AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList_Yield : ElementList_Yield `,` Elision AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList_Await : ElementList_Await `,` AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList_Await : ElementList_Await `,` Elision AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList_Yield_Await : ElementList_Yield_Await `,` AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ElementList_Yield_Await : ElementList_Yield_Await `,` Elision AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList : ElementList `,` SpreadElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList : ElementList `,` Elision SpreadElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList_Yield : ElementList_Yield `,` SpreadElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList_Yield : ElementList_Yield `,` Elision SpreadElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList_Await : ElementList_Await `,` SpreadElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList_Await : ElementList_Await `,` Elision SpreadElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList_Yield_Await : ElementList_Yield_Await `,` SpreadElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
@builder.build('ElementList_Yield_Await : ElementList_Yield_Await `,` Elision SpreadElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Elision  : `,`
@builder.build('Elision : `,`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Elision  : Elision `,`
@builder.build('Elision : Elision `,`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SpreadElement[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('SpreadElement : `...` AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SpreadElement[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('SpreadElement_Yield : `...` AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SpreadElement[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('SpreadElement_Await : `...` AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SpreadElement[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('SpreadElement_Yield_Await : `...` AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectLiteral[Yield, Await]  : `{` `}`
@builder.build('ObjectLiteral : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectLiteral[Yield, Await]  : `{` `}`
@builder.build('ObjectLiteral_Yield : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectLiteral[Yield, Await]  : `{` `}`
@builder.build('ObjectLiteral_Await : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectLiteral[Yield, Await]  : `{` `}`
@builder.build('ObjectLiteral_Yield_Await : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `}`
@builder.build('ObjectLiteral : `{` PropertyDefinitionList `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `}`
@builder.build('ObjectLiteral_Yield : `{` PropertyDefinitionList_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `}`
@builder.build('ObjectLiteral_Await : `{` PropertyDefinitionList_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `}`
@builder.build('ObjectLiteral_Yield_Await : `{` PropertyDefinitionList_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `,` `}`
@builder.build('ObjectLiteral : `{` PropertyDefinitionList `,` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `,` `}`
@builder.build('ObjectLiteral_Yield : `{` PropertyDefinitionList_Yield `,` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `,` `}`
@builder.build('ObjectLiteral_Await : `{` PropertyDefinitionList_Await `,` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `,` `}`
@builder.build('ObjectLiteral_Yield_Await : `{` PropertyDefinitionList_Yield_Await `,` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinitionList[Yield, Await]  : PropertyDefinition[?Yield, ?Await]
@builder.build('PropertyDefinitionList : PropertyDefinition')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinitionList[Yield, Await]  : PropertyDefinition[?Yield, ?Await]
@builder.build('PropertyDefinitionList_Yield : PropertyDefinition_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinitionList[Yield, Await]  : PropertyDefinition[?Yield, ?Await]
@builder.build('PropertyDefinitionList_Await : PropertyDefinition_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinitionList[Yield, Await]  : PropertyDefinition[?Yield, ?Await]
@builder.build('PropertyDefinitionList_Yield_Await : PropertyDefinition_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinitionList[Yield, Await]  : PropertyDefinitionList[?Yield, ?Await] `,` PropertyDefinition[?Yield, ?Await]
@builder.build('PropertyDefinitionList : PropertyDefinitionList `,` PropertyDefinition')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinitionList[Yield, Await]  : PropertyDefinitionList[?Yield, ?Await] `,` PropertyDefinition[?Yield, ?Await]
@builder.build('PropertyDefinitionList_Yield : PropertyDefinitionList_Yield `,` PropertyDefinition_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinitionList[Yield, Await]  : PropertyDefinitionList[?Yield, ?Await] `,` PropertyDefinition[?Yield, ?Await]
@builder.build('PropertyDefinitionList_Await : PropertyDefinitionList_Await `,` PropertyDefinition_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinitionList[Yield, Await]  : PropertyDefinitionList[?Yield, ?Await] `,` PropertyDefinition[?Yield, ?Await]
@builder.build('PropertyDefinitionList_Yield_Await : PropertyDefinitionList_Yield_Await `,` PropertyDefinition_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : IdentifierReference[?Yield, ?Await]
@builder.build('PropertyDefinition : IdentifierReference')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : IdentifierReference[?Yield, ?Await]
@builder.build('PropertyDefinition_Yield : IdentifierReference_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : IdentifierReference[?Yield, ?Await]
@builder.build('PropertyDefinition_Await : IdentifierReference_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : IdentifierReference[?Yield, ?Await]
@builder.build('PropertyDefinition_Yield_Await : IdentifierReference_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : CoverInitializedName[?Yield, ?Await]
@builder.build('PropertyDefinition : CoverInitializedName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : CoverInitializedName[?Yield, ?Await]
@builder.build('PropertyDefinition_Yield : CoverInitializedName_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : CoverInitializedName[?Yield, ?Await]
@builder.build('PropertyDefinition_Await : CoverInitializedName_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : CoverInitializedName[?Yield, ?Await]
@builder.build('PropertyDefinition_Yield_Await : CoverInitializedName_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('PropertyDefinition : PropertyName `:` AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('PropertyDefinition_Yield : PropertyName_Yield `:` AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('PropertyDefinition_Await : PropertyName_Await `:` AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('PropertyDefinition_Yield_Await : PropertyName_Yield_Await `:` AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : MethodDefinition[?Yield, ?Await]
@builder.build('PropertyDefinition : MethodDefinition')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : MethodDefinition[?Yield, ?Await]
@builder.build('PropertyDefinition_Yield : MethodDefinition_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : MethodDefinition[?Yield, ?Await]
@builder.build('PropertyDefinition_Await : MethodDefinition_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : MethodDefinition[?Yield, ?Await]
@builder.build('PropertyDefinition_Yield_Await : MethodDefinition_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('PropertyDefinition : `...` AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('PropertyDefinition_Yield : `...` AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('PropertyDefinition_Await : `...` AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyDefinition[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('PropertyDefinition_Yield_Await : `...` AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyName[Yield, Await]  : LiteralPropertyName
@builder.build('PropertyName : LiteralPropertyName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyName[Yield, Await]  : LiteralPropertyName
@builder.build('PropertyName_Yield : LiteralPropertyName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyName[Yield, Await]  : LiteralPropertyName
@builder.build('PropertyName_Await : LiteralPropertyName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyName[Yield, Await]  : LiteralPropertyName
@builder.build('PropertyName_Yield_Await : LiteralPropertyName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyName[Yield, Await]  : ComputedPropertyName[?Yield, ?Await]
@builder.build('PropertyName : ComputedPropertyName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyName[Yield, Await]  : ComputedPropertyName[?Yield, ?Await]
@builder.build('PropertyName_Yield : ComputedPropertyName_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyName[Yield, Await]  : ComputedPropertyName[?Yield, ?Await]
@builder.build('PropertyName_Await : ComputedPropertyName_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#PropertyName[Yield, Await]  : ComputedPropertyName[?Yield, ?Await]
@builder.build('PropertyName_Yield_Await : ComputedPropertyName_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LiteralPropertyName  : IdentifierName
@builder.build('LiteralPropertyName : IdentifierName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LiteralPropertyName  : StringLiteral
@builder.build('LiteralPropertyName : StringLiteral')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LiteralPropertyName  : NumericLiteral
@builder.build('LiteralPropertyName : NumericLiteral')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ComputedPropertyName[Yield, Await]  : `[` AssignmentExpression[+In, ?Yield, ?Await] `]`
@builder.build('ComputedPropertyName : `[` AssignmentExpression_In `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ComputedPropertyName[Yield, Await]  : `[` AssignmentExpression[+In, ?Yield, ?Await] `]`
@builder.build('ComputedPropertyName_Yield : `[` AssignmentExpression_In_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ComputedPropertyName[Yield, Await]  : `[` AssignmentExpression[+In, ?Yield, ?Await] `]`
@builder.build('ComputedPropertyName_Await : `[` AssignmentExpression_In_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ComputedPropertyName[Yield, Await]  : `[` AssignmentExpression[+In, ?Yield, ?Await] `]`
@builder.build('ComputedPropertyName_Yield_Await : `[` AssignmentExpression_In_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverInitializedName[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]
@builder.build('CoverInitializedName : IdentifierReference Initializer_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverInitializedName[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]
@builder.build('CoverInitializedName_Yield : IdentifierReference_Yield Initializer_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverInitializedName[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]
@builder.build('CoverInitializedName_Await : IdentifierReference_Await Initializer_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CoverInitializedName[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]
@builder.build('CoverInitializedName_Yield_Await : IdentifierReference_Yield_Await Initializer_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Initializer : `=` `@AssignmentExpression`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Initializer_In : `=` `@AssignmentExpression_In`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Initializer_Yield : `=` AssignmentExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Initializer_In_Yield : `=` AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Initializer_Await : `=` AssignmentExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Initializer_In_Await : `=` AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Initializer_Yield_Await : `=` AssignmentExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Initializer_In_Yield_Await : `=` AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
@builder.build('TemplateLiteral : NoSubstitutionTemplate')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
@builder.build('TemplateLiteral_Yield : NoSubstitutionTemplate')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
@builder.build('TemplateLiteral_Await : NoSubstitutionTemplate')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
@builder.build('TemplateLiteral_Yield_Await : NoSubstitutionTemplate')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
@builder.build('TemplateLiteral_Tagged : NoSubstitutionTemplate')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
@builder.build('TemplateLiteral_Yield_Tagged : NoSubstitutionTemplate')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
@builder.build('TemplateLiteral_Await_Tagged : NoSubstitutionTemplate')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
@builder.build('TemplateLiteral_Yield_Await_Tagged : NoSubstitutionTemplate')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
@builder.build('TemplateLiteral : SubstitutionTemplate')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
@builder.build('TemplateLiteral_Yield : SubstitutionTemplate_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
@builder.build('TemplateLiteral_Await : SubstitutionTemplate_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
@builder.build('TemplateLiteral_Yield_Await : SubstitutionTemplate_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
@builder.build('TemplateLiteral_Tagged : SubstitutionTemplate_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
@builder.build('TemplateLiteral_Yield_Tagged : SubstitutionTemplate_Yield_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
@builder.build('TemplateLiteral_Await_Tagged : SubstitutionTemplate_Await_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
@builder.build('TemplateLiteral_Yield_Await_Tagged : SubstitutionTemplate_Yield_Await_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
@builder.build('SubstitutionTemplate : TemplateHead Expression_In TemplateSpans')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
@builder.build('SubstitutionTemplate_Yield : TemplateHead Expression_In_Yield TemplateSpans_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
@builder.build('SubstitutionTemplate_Await : TemplateHead Expression_In_Await TemplateSpans_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
@builder.build('SubstitutionTemplate_Yield_Await : TemplateHead Expression_In_Yield_Await TemplateSpans_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
@builder.build('SubstitutionTemplate_Tagged : TemplateHead Expression_In TemplateSpans_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
@builder.build('SubstitutionTemplate_Yield_Tagged : TemplateHead Expression_In_Yield TemplateSpans_Yield_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
@builder.build('SubstitutionTemplate_Await_Tagged : TemplateHead Expression_In_Await TemplateSpans_Await_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
@builder.build('SubstitutionTemplate_Yield_Await_Tagged : TemplateHead Expression_In_Yield_Await TemplateSpans_Yield_Await_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
@builder.build('TemplateSpans : TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
@builder.build('TemplateSpans_Yield : TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
@builder.build('TemplateSpans_Await : TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
@builder.build('TemplateSpans_Yield_Await : TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
@builder.build('TemplateSpans_Tagged : TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
@builder.build('TemplateSpans_Yield_Tagged : TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
@builder.build('TemplateSpans_Await_Tagged : TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
@builder.build('TemplateSpans_Yield_Await_Tagged : TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
@builder.build('TemplateSpans : TemplateMiddleList TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
@builder.build('TemplateSpans_Yield : TemplateMiddleList_Yield TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
@builder.build('TemplateSpans_Await : TemplateMiddleList_Await TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
@builder.build('TemplateSpans_Yield_Await : TemplateMiddleList_Yield_Await TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
@builder.build('TemplateSpans_Tagged : TemplateMiddleList_Tagged TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
@builder.build('TemplateSpans_Yield_Tagged : TemplateMiddleList_Yield_Tagged TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
@builder.build('TemplateSpans_Await_Tagged : TemplateMiddleList_Await_Tagged TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
@builder.build('TemplateSpans_Yield_Await_Tagged : TemplateMiddleList_Yield_Await_Tagged TemplateTail')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList : TemplateMiddle Expression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList_Yield : TemplateMiddle Expression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList_Await : TemplateMiddle Expression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList_Yield_Await : TemplateMiddle Expression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList_Tagged : TemplateMiddle Expression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList_Yield_Tagged : TemplateMiddle Expression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList_Await_Tagged : TemplateMiddle Expression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList_Yield_Await_Tagged : TemplateMiddle Expression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList : TemplateMiddleList TemplateMiddle Expression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList_Yield : TemplateMiddleList_Yield TemplateMiddle Expression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList_Await : TemplateMiddleList_Await TemplateMiddle Expression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList_Yield_Await : TemplateMiddleList_Yield_Await TemplateMiddle Expression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList_Tagged : TemplateMiddleList_Tagged TemplateMiddle Expression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList_Yield_Tagged : TemplateMiddleList_Yield_Tagged TemplateMiddle Expression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList_Await_Tagged : TemplateMiddleList_Await_Tagged TemplateMiddle Expression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
@builder.build('TemplateMiddleList_Yield_Await_Tagged : TemplateMiddleList_Yield_Await_Tagged TemplateMiddle Expression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : PrimaryExpression[?Yield, ?Await]
@builder.build('MemberExpression : PrimaryExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : PrimaryExpression[?Yield, ?Await]
@builder.build('MemberExpression_Yield : PrimaryExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : PrimaryExpression[?Yield, ?Await]
@builder.build('MemberExpression_Await : PrimaryExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : PrimaryExpression[?Yield, ?Await]
@builder.build('MemberExpression_Yield_Await : PrimaryExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
@builder.build('MemberExpression : MemberExpression `[` Expression_In `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
@builder.build('MemberExpression_Yield : MemberExpression_Yield `[` Expression_In_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
@builder.build('MemberExpression_Await : MemberExpression_Await `[` Expression_In_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
@builder.build('MemberExpression_Yield_Await : MemberExpression_Yield_Await `[` Expression_In_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `.` IdentifierName
@builder.build('MemberExpression : MemberExpression `.` IdentifierName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `.` IdentifierName
@builder.build('MemberExpression_Yield : MemberExpression_Yield `.` IdentifierName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `.` IdentifierName
@builder.build('MemberExpression_Await : MemberExpression_Await `.` IdentifierName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `.` IdentifierName
@builder.build('MemberExpression_Yield_Await : MemberExpression_Yield_Await `.` IdentifierName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
@builder.build('MemberExpression : MemberExpression TemplateLiteral_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
@builder.build('MemberExpression_Yield : MemberExpression_Yield TemplateLiteral_Yield_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
@builder.build('MemberExpression_Await : MemberExpression_Await TemplateLiteral_Await_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
@builder.build('MemberExpression_Yield_Await : MemberExpression_Yield_Await TemplateLiteral_Yield_Await_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : SuperProperty[?Yield, ?Await]
@builder.build('MemberExpression : SuperProperty')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : SuperProperty[?Yield, ?Await]
@builder.build('MemberExpression_Yield : SuperProperty_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : SuperProperty[?Yield, ?Await]
@builder.build('MemberExpression_Await : SuperProperty_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : SuperProperty[?Yield, ?Await]
@builder.build('MemberExpression_Yield_Await : SuperProperty_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MetaProperty
@builder.build('MemberExpression : MetaProperty')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MetaProperty
@builder.build('MemberExpression_Yield : MetaProperty')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MetaProperty
@builder.build('MemberExpression_Await : MetaProperty')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : MetaProperty
@builder.build('MemberExpression_Yield_Await : MetaProperty')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : `new` MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('MemberExpression : `new` MemberExpression Arguments')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : `new` MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('MemberExpression_Yield : `new` MemberExpression_Yield Arguments_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : `new` MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('MemberExpression_Await : `new` MemberExpression_Await Arguments_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MemberExpression[Yield, Await]  : `new` MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('MemberExpression_Yield_Await : `new` MemberExpression_Yield_Await Arguments_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SuperProperty[Yield, Await]  : `super` `[` Expression[+In, ?Yield, ?Await] `]`
@builder.build('SuperProperty : `super` `[` Expression_In `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SuperProperty[Yield, Await]  : `super` `[` Expression[+In, ?Yield, ?Await] `]`
@builder.build('SuperProperty_Yield : `super` `[` Expression_In_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SuperProperty[Yield, Await]  : `super` `[` Expression[+In, ?Yield, ?Await] `]`
@builder.build('SuperProperty_Await : `super` `[` Expression_In_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SuperProperty[Yield, Await]  : `super` `[` Expression[+In, ?Yield, ?Await] `]`
@builder.build('SuperProperty_Yield_Await : `super` `[` Expression_In_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SuperProperty[Yield, Await]  : `super` `.` IdentifierName
@builder.build('SuperProperty : `super` `.` IdentifierName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SuperProperty[Yield, Await]  : `super` `.` IdentifierName
@builder.build('SuperProperty_Yield : `super` `.` IdentifierName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SuperProperty[Yield, Await]  : `super` `.` IdentifierName
@builder.build('SuperProperty_Await : `super` `.` IdentifierName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SuperProperty[Yield, Await]  : `super` `.` IdentifierName
@builder.build('SuperProperty_Yield_Await : `super` `.` IdentifierName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MetaProperty  : NewTarget
@builder.build('MetaProperty : NewTarget')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#NewTarget  : `new` `.` `target`
@builder.build('NewTarget : `new` `.` `target`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#NewExpression[Yield, Await]  : MemberExpression[?Yield, ?Await]
@builder.build('NewExpression : MemberExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#NewExpression[Yield, Await]  : MemberExpression[?Yield, ?Await]
@builder.build('NewExpression_Yield : MemberExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#NewExpression[Yield, Await]  : MemberExpression[?Yield, ?Await]
@builder.build('NewExpression_Await : MemberExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#NewExpression[Yield, Await]  : MemberExpression[?Yield, ?Await]
@builder.build('NewExpression_Yield_Await : MemberExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#NewExpression[Yield, Await]  : `new` NewExpression[?Yield, ?Await]
@builder.build('NewExpression : `new` NewExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#NewExpression[Yield, Await]  : `new` NewExpression[?Yield, ?Await]
@builder.build('NewExpression_Yield : `new` NewExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#NewExpression[Yield, Await]  : `new` NewExpression[?Yield, ?Await]
@builder.build('NewExpression_Await : `new` NewExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#NewExpression[Yield, Await]  : `new` NewExpression[?Yield, ?Await]
@builder.build('NewExpression_Yield_Await : `new` NewExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await] #callcover
@builder.build('CallExpression : CoverCallExpressionAndAsyncArrowHead')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await] #callcover
@builder.build('CallExpression_Yield : CoverCallExpressionAndAsyncArrowHead_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await] #callcover
@builder.build('CallExpression_Await : CoverCallExpressionAndAsyncArrowHead_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await] #callcover
@builder.build('CallExpression_Yield_Await : CoverCallExpressionAndAsyncArrowHead_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : SuperCall[?Yield, ?Await]
@builder.build('CallExpression : SuperCall')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : SuperCall[?Yield, ?Await]
@builder.build('CallExpression_Yield : SuperCall_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : SuperCall[?Yield, ?Await]
@builder.build('CallExpression_Await : SuperCall_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : SuperCall[?Yield, ?Await]
@builder.build('CallExpression_Yield_Await : SuperCall_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('CallExpression : CallExpression Arguments')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('CallExpression_Yield : CallExpression_Yield Arguments_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('CallExpression_Await : CallExpression_Await Arguments_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('CallExpression_Yield_Await : CallExpression_Yield_Await Arguments_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
@builder.build('CallExpression : CallExpression `[` Expression_In `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
@builder.build('CallExpression_Yield : CallExpression_Yield `[` Expression_In_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
@builder.build('CallExpression_Await : CallExpression_Await `[` Expression_In_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
@builder.build('CallExpression_Yield_Await : CallExpression_Yield_Await `[` Expression_In_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `.` IdentifierName
@builder.build('CallExpression : CallExpression `.` IdentifierName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `.` IdentifierName
@builder.build('CallExpression_Yield : CallExpression_Yield `.` IdentifierName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `.` IdentifierName
@builder.build('CallExpression_Await : CallExpression_Await `.` IdentifierName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `.` IdentifierName
@builder.build('CallExpression_Yield_Await : CallExpression_Yield_Await `.` IdentifierName')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
@builder.build('CallExpression : CallExpression TemplateLiteral_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
@builder.build('CallExpression_Yield : CallExpression_Yield TemplateLiteral_Yield_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
@builder.build('CallExpression_Await : CallExpression_Await TemplateLiteral_Await_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
@builder.build('CallExpression_Yield_Await : CallExpression_Yield_Await TemplateLiteral_Yield_Await_Tagged')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SuperCall[Yield, Await]  : `super` Arguments[?Yield, ?Await]
@builder.build('SuperCall : `super` Arguments')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SuperCall[Yield, Await]  : `super` Arguments[?Yield, ?Await]
@builder.build('SuperCall_Yield : `super` Arguments_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SuperCall[Yield, Await]  : `super` Arguments[?Yield, ?Await]
@builder.build('SuperCall_Await : `super` Arguments_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SuperCall[Yield, Await]  : `super` Arguments[?Yield, ?Await]
@builder.build('SuperCall_Yield_Await : `super` Arguments_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Arguments[Yield, Await]  : `(` `)`
@builder.build('Arguments : `(` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Arguments[Yield, Await]  : `(` `)`
@builder.build('Arguments_Yield : `(` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Arguments[Yield, Await]  : `(` `)`
@builder.build('Arguments_Await : `(` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Arguments[Yield, Await]  : `(` `)`
@builder.build('Arguments_Yield_Await : `(` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `)`
@builder.build('Arguments : `(` ArgumentList `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `)`
@builder.build('Arguments_Yield : `(` ArgumentList_Yield `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `)`
@builder.build('Arguments_Await : `(` ArgumentList_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `)`
@builder.build('Arguments_Yield_Await : `(` ArgumentList_Yield_Await `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `,` `)`
@builder.build('Arguments : `(` ArgumentList `,` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `,` `)`
@builder.build('Arguments_Yield : `(` ArgumentList_Yield `,` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `,` `)`
@builder.build('Arguments_Await : `(` ArgumentList_Await `,` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `,` `)`
@builder.build('Arguments_Yield_Await : `(` ArgumentList_Yield_Await `,` `)`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList : AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList_Yield : AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList_Await : AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList_Yield_Await : AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList : `...` AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList_Yield : `...` AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList_Await : `...` AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList_Yield_Await : `...` AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList : ArgumentList `,` AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList_Yield : ArgumentList_Yield `,` AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList_Await : ArgumentList_Await `,` AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList_Yield_Await : ArgumentList_Yield_Await `,` AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList : ArgumentList `,` `...` AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList_Yield : ArgumentList_Yield `,` `...` AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList_Await : ArgumentList_Await `,` `...` AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` `...` AssignmentExpression[+In, ?Yield, ?Await]
@builder.build('ArgumentList_Yield_Await : ArgumentList_Yield_Await `,` `...` AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LeftHandSideExpression[Yield, Await]  : NewExpression[?Yield, ?Await]
@builder.build('LeftHandSideExpression : NewExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LeftHandSideExpression[Yield, Await]  : NewExpression[?Yield, ?Await]
@builder.build('LeftHandSideExpression_Yield : NewExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LeftHandSideExpression[Yield, Await]  : NewExpression[?Yield, ?Await]
@builder.build('LeftHandSideExpression_Await : NewExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LeftHandSideExpression[Yield, Await]  : NewExpression[?Yield, ?Await]
@builder.build('LeftHandSideExpression_Yield_Await : NewExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LeftHandSideExpression[Yield, Await]  : CallExpression[?Yield, ?Await]
@builder.build('LeftHandSideExpression : CallExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LeftHandSideExpression[Yield, Await]  : CallExpression[?Yield, ?Await]
@builder.build('LeftHandSideExpression_Yield : CallExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LeftHandSideExpression[Yield, Await]  : CallExpression[?Yield, ?Await]
@builder.build('LeftHandSideExpression_Await : CallExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LeftHandSideExpression[Yield, Await]  : CallExpression[?Yield, ?Await]
@builder.build('LeftHandSideExpression_Yield_Await : CallExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallMemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('CallMemberExpression : MemberExpression Arguments')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallMemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('CallMemberExpression_Yield : MemberExpression_Yield Arguments_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallMemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('CallMemberExpression_Await : MemberExpression_Await Arguments_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CallMemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
@builder.build('CallMemberExpression_Yield_Await : MemberExpression_Yield_Await Arguments_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
@builder.build('UpdateExpression : LeftHandSideExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
@builder.build('UpdateExpression_Yield : LeftHandSideExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
@builder.build('UpdateExpression_Await : LeftHandSideExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
@builder.build('UpdateExpression_Yield_Await : LeftHandSideExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `++`
@builder.build('UpdateExpression : LeftHandSideExpression `++`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `++`
@builder.build('UpdateExpression_Yield : LeftHandSideExpression_Yield `++`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `++`
@builder.build('UpdateExpression_Await : LeftHandSideExpression_Await `++`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `++`
@builder.build('UpdateExpression_Yield_Await : LeftHandSideExpression_Yield_Await `++`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `--`
@builder.build('UpdateExpression : LeftHandSideExpression `--`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `--`
@builder.build('UpdateExpression_Yield : LeftHandSideExpression_Yield `--`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `--`
@builder.build('UpdateExpression_Await : LeftHandSideExpression_Await `--`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `--`
@builder.build('UpdateExpression_Yield_Await : LeftHandSideExpression_Yield_Await `--`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : `++` UnaryExpression[?Yield, ?Await]
@builder.build('UpdateExpression : `++` UnaryExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : `++` UnaryExpression[?Yield, ?Await]
@builder.build('UpdateExpression_Yield : `++` UnaryExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : `++` UnaryExpression[?Yield, ?Await]
@builder.build('UpdateExpression_Await : `++` UnaryExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : `++` UnaryExpression[?Yield, ?Await]
@builder.build('UpdateExpression_Yield_Await : `++` UnaryExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : `--` UnaryExpression[?Yield, ?Await]
@builder.build('UpdateExpression : `--` UnaryExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : `--` UnaryExpression[?Yield, ?Await]
@builder.build('UpdateExpression_Yield : `--` UnaryExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : `--` UnaryExpression[?Yield, ?Await]
@builder.build('UpdateExpression_Await : `--` UnaryExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UpdateExpression[Yield, Await]  : `--` UnaryExpression[?Yield, ?Await]
@builder.build('UpdateExpression_Yield_Await : `--` UnaryExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await]
@builder.build('UnaryExpression : UpdateExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield : UpdateExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Await : UpdateExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield_Await : UpdateExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `delete` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression : `delete` UnaryExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `delete` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield : `delete` UnaryExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `delete` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Await : `delete` UnaryExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `delete` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield_Await : `delete` UnaryExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `void` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression : `void` UnaryExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `void` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield : `void` UnaryExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `void` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Await : `void` UnaryExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `void` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield_Await : `void` UnaryExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `typeof` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression : `typeof` UnaryExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `typeof` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield : `typeof` UnaryExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `typeof` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Await : `typeof` UnaryExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `typeof` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield_Await : `typeof` UnaryExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `+` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression : `+` UnaryExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `+` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield : `+` UnaryExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `+` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Await : `+` UnaryExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `+` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield_Await : `+` UnaryExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `-` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression : `-` UnaryExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `-` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield : `-` UnaryExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `-` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Await : `-` UnaryExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `-` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield_Await : `-` UnaryExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `~` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression : `~` UnaryExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `~` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield : `~` UnaryExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `~` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Await : `~` UnaryExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `~` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield_Await : `~` UnaryExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `!` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression : `!` UnaryExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `!` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield : `!` UnaryExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `!` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Await : `!` UnaryExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : `!` UnaryExpression[?Yield, ?Await]
@builder.build('UnaryExpression_Yield_Await : `!` UnaryExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : [+Await] AwaitExpression[?Yield]
@builder.build('UnaryExpression_Await : AwaitExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#UnaryExpression[Yield, Await]  : [+Await] AwaitExpression[?Yield]
@builder.build('UnaryExpression_Yield_Await : AwaitExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ExponentiationExpression[Yield, Await]  : UnaryExpression[?Yield, ?Await]
@builder.build('ExponentiationExpression : UnaryExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ExponentiationExpression[Yield, Await]  : UnaryExpression[?Yield, ?Await]
@builder.build('ExponentiationExpression_Yield : UnaryExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ExponentiationExpression[Yield, Await]  : UnaryExpression[?Yield, ?Await]
@builder.build('ExponentiationExpression_Await : UnaryExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ExponentiationExpression[Yield, Await]  : UnaryExpression[?Yield, ?Await]
@builder.build('ExponentiationExpression_Yield_Await : UnaryExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ExponentiationExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await] `**` ExponentiationExpression[?Yield, ?Await]
@builder.build('ExponentiationExpression : UpdateExpression `**` ExponentiationExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ExponentiationExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await] `**` ExponentiationExpression[?Yield, ?Await]
@builder.build('ExponentiationExpression_Yield : UpdateExpression_Yield `**` ExponentiationExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ExponentiationExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await] `**` ExponentiationExpression[?Yield, ?Await]
@builder.build('ExponentiationExpression_Await : UpdateExpression_Await `**` ExponentiationExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ExponentiationExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await] `**` ExponentiationExpression[?Yield, ?Await]
@builder.build('ExponentiationExpression_Yield_Await : UpdateExpression_Yield_Await `**` ExponentiationExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MultiplicativeExpression[Yield, Await]  : ExponentiationExpression[?Yield, ?Await]
@builder.build('MultiplicativeExpression : ExponentiationExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MultiplicativeExpression[Yield, Await]  : ExponentiationExpression[?Yield, ?Await]
@builder.build('MultiplicativeExpression_Yield : ExponentiationExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MultiplicativeExpression[Yield, Await]  : ExponentiationExpression[?Yield, ?Await]
@builder.build('MultiplicativeExpression_Await : ExponentiationExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MultiplicativeExpression[Yield, Await]  : ExponentiationExpression[?Yield, ?Await]
@builder.build('MultiplicativeExpression_Yield_Await : ExponentiationExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MultiplicativeExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await] MultiplicativeOperator ExponentiationExpression[?Yield, ?Await]
@builder.build('MultiplicativeExpression : MultiplicativeExpression MultiplicativeOperator ExponentiationExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MultiplicativeExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await] MultiplicativeOperator ExponentiationExpression[?Yield, ?Await]
@builder.build('MultiplicativeExpression_Yield : MultiplicativeExpression_Yield MultiplicativeOperator ExponentiationExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MultiplicativeExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await] MultiplicativeOperator ExponentiationExpression[?Yield, ?Await]
@builder.build('MultiplicativeExpression_Await : MultiplicativeExpression_Await MultiplicativeOperator ExponentiationExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MultiplicativeExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await] MultiplicativeOperator ExponentiationExpression[?Yield, ?Await]
@builder.build('MultiplicativeExpression_Yield_Await : MultiplicativeExpression_Yield_Await MultiplicativeOperator ExponentiationExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MultiplicativeOperator : one of `*` `/` `%`
@builder.build('MultiplicativeOperator : `*`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MultiplicativeOperator : one of `*` `/` `%`
@builder.build('MultiplicativeOperator : `/`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#MultiplicativeOperator : one of `*` `/` `%`
@builder.build('MultiplicativeOperator : `%`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AdditiveExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await]
@builder.build('AdditiveExpression : MultiplicativeExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AdditiveExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await]
@builder.build('AdditiveExpression_Yield : MultiplicativeExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AdditiveExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await]
@builder.build('AdditiveExpression_Await : MultiplicativeExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AdditiveExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await]
@builder.build('AdditiveExpression_Yield_Await : MultiplicativeExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `+` MultiplicativeExpression[?Yield, ?Await]
@builder.build('AdditiveExpression : AdditiveExpression `+` MultiplicativeExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `+` MultiplicativeExpression[?Yield, ?Await]
@builder.build('AdditiveExpression_Yield : AdditiveExpression_Yield `+` MultiplicativeExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `+` MultiplicativeExpression[?Yield, ?Await]
@builder.build('AdditiveExpression_Await : AdditiveExpression_Await `+` MultiplicativeExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `+` MultiplicativeExpression[?Yield, ?Await]
@builder.build('AdditiveExpression_Yield_Await : AdditiveExpression_Yield_Await `+` MultiplicativeExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `-` MultiplicativeExpression[?Yield, ?Await]
@builder.build('AdditiveExpression : AdditiveExpression `-` MultiplicativeExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `-` MultiplicativeExpression[?Yield, ?Await]
@builder.build('AdditiveExpression_Yield : AdditiveExpression_Yield `-` MultiplicativeExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `-` MultiplicativeExpression[?Yield, ?Await]
@builder.build('AdditiveExpression_Await : AdditiveExpression_Await `-` MultiplicativeExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `-` MultiplicativeExpression[?Yield, ?Await]
@builder.build('AdditiveExpression_Yield_Await : AdditiveExpression_Yield_Await `-` MultiplicativeExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression : AdditiveExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression_Yield : AdditiveExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression_Await : AdditiveExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression_Yield_Await : AdditiveExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `<<` AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression : ShiftExpression `<<` AdditiveExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `<<` AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression_Yield : ShiftExpression_Yield `<<` AdditiveExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `<<` AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression_Await : ShiftExpression_Await `<<` AdditiveExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `<<` AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression_Yield_Await : ShiftExpression_Yield_Await `<<` AdditiveExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>` AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression : ShiftExpression `>>` AdditiveExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>` AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression_Yield : ShiftExpression_Yield `>>` AdditiveExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>` AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression_Await : ShiftExpression_Await `>>` AdditiveExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>` AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression_Yield_Await : ShiftExpression_Yield_Await `>>` AdditiveExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>>` AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression : ShiftExpression `>>>` AdditiveExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>>` AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression_Yield : ShiftExpression_Yield `>>>` AdditiveExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>>` AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression_Await : ShiftExpression_Await `>>>` AdditiveExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>>` AdditiveExpression[?Yield, ?Await]
@builder.build('ShiftExpression_Yield_Await : ShiftExpression_Yield_Await `>>>` AdditiveExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression : ShiftExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In : ShiftExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Yield : ShiftExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Yield : ShiftExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Await : ShiftExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Await : ShiftExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Yield_Await : ShiftExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Yield_Await : ShiftExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression : RelationalExpression `<` ShiftExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In : RelationalExpression_In `<` ShiftExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Yield : RelationalExpression_Yield `<` ShiftExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Yield : RelationalExpression_In_Yield `<` ShiftExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Await : RelationalExpression_Await `<` ShiftExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Await : RelationalExpression_In_Await `<` ShiftExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Yield_Await : RelationalExpression_Yield_Await `<` ShiftExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Yield_Await : RelationalExpression_In_Yield_Await `<` ShiftExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression : RelationalExpression `>` ShiftExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In : RelationalExpression_In `>` ShiftExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Yield : RelationalExpression_Yield `>` ShiftExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Yield : RelationalExpression_In_Yield `>` ShiftExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Await : RelationalExpression_Await `>` ShiftExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Await : RelationalExpression_In_Await `>` ShiftExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Yield_Await : RelationalExpression_Yield_Await `>` ShiftExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Yield_Await : RelationalExpression_In_Yield_Await `>` ShiftExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression : RelationalExpression `<=` ShiftExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In : RelationalExpression_In `<=` ShiftExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Yield : RelationalExpression_Yield `<=` ShiftExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Yield : RelationalExpression_In_Yield `<=` ShiftExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Await : RelationalExpression_Await `<=` ShiftExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Await : RelationalExpression_In_Await `<=` ShiftExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Yield_Await : RelationalExpression_Yield_Await `<=` ShiftExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Yield_Await : RelationalExpression_In_Yield_Await `<=` ShiftExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression : RelationalExpression `>=` ShiftExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In : RelationalExpression_In `>=` ShiftExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Yield : RelationalExpression_Yield `>=` ShiftExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Yield : RelationalExpression_In_Yield `>=` ShiftExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Await : RelationalExpression_Await `>=` ShiftExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Await : RelationalExpression_In_Await `>=` ShiftExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Yield_Await : RelationalExpression_Yield_Await `>=` ShiftExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Yield_Await : RelationalExpression_In_Yield_Await `>=` ShiftExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression : RelationalExpression `instanceof` ShiftExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In : RelationalExpression_In `instanceof` ShiftExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Yield : RelationalExpression_Yield `instanceof` ShiftExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Yield : RelationalExpression_In_Yield `instanceof` ShiftExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Await : RelationalExpression_Await `instanceof` ShiftExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Await : RelationalExpression_In_Await `instanceof` ShiftExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_Yield_Await : RelationalExpression_Yield_Await `instanceof` ShiftExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Yield_Await : RelationalExpression_In_Yield_Await `instanceof` ShiftExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : [+In] RelationalExpression[+In, ?Yield, ?Await] `in` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In : RelationalExpression_In `in` ShiftExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : [+In] RelationalExpression[+In, ?Yield, ?Await] `in` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Yield : RelationalExpression_In_Yield `in` ShiftExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : [+In] RelationalExpression[+In, ?Yield, ?Await] `in` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Await : RelationalExpression_In_Await `in` ShiftExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#RelationalExpression[In, Yield, Await]  : [+In] RelationalExpression[+In, ?Yield, ?Await] `in` ShiftExpression[?Yield, ?Await]
@builder.build('RelationalExpression_In_Yield_Await : RelationalExpression_In_Yield_Await `in` ShiftExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression : RelationalExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In : RelationalExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Yield : RelationalExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Yield : RelationalExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Await : RelationalExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Await : RelationalExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Yield_Await : RelationalExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Yield_Await : RelationalExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression : EqualityExpression `==` RelationalExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In : EqualityExpression_In `==` RelationalExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Yield : EqualityExpression_Yield `==` RelationalExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Yield : EqualityExpression_In_Yield `==` RelationalExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Await : EqualityExpression_Await `==` RelationalExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Await : EqualityExpression_In_Await `==` RelationalExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Yield_Await : EqualityExpression_Yield_Await `==` RelationalExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Yield_Await : EqualityExpression_In_Yield_Await `==` RelationalExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression : EqualityExpression `!=` RelationalExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In : EqualityExpression_In `!=` RelationalExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Yield : EqualityExpression_Yield `!=` RelationalExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Yield : EqualityExpression_In_Yield `!=` RelationalExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Await : EqualityExpression_Await `!=` RelationalExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Await : EqualityExpression_In_Await `!=` RelationalExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Yield_Await : EqualityExpression_Yield_Await `!=` RelationalExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Yield_Await : EqualityExpression_In_Yield_Await `!=` RelationalExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression : EqualityExpression `===` RelationalExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In : EqualityExpression_In `===` RelationalExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Yield : EqualityExpression_Yield `===` RelationalExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Yield : EqualityExpression_In_Yield `===` RelationalExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Await : EqualityExpression_Await `===` RelationalExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Await : EqualityExpression_In_Await `===` RelationalExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Yield_Await : EqualityExpression_Yield_Await `===` RelationalExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Yield_Await : EqualityExpression_In_Yield_Await `===` RelationalExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression : EqualityExpression `!==` RelationalExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In : EqualityExpression_In `!==` RelationalExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Yield : EqualityExpression_Yield `!==` RelationalExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Yield : EqualityExpression_In_Yield `!==` RelationalExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Await : EqualityExpression_Await `!==` RelationalExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Await : EqualityExpression_In_Await `!==` RelationalExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_Yield_Await : EqualityExpression_Yield_Await `!==` RelationalExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
@builder.build('EqualityExpression_In_Yield_Await : EqualityExpression_In_Yield_Await `!==` RelationalExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression : EqualityExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression_In : EqualityExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression_Yield : EqualityExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression_In_Yield : EqualityExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression_Await : EqualityExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression_In_Await : EqualityExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression_Yield_Await : EqualityExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression_In_Yield_Await : EqualityExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression : BitwiseANDExpression `&` EqualityExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression_In : BitwiseANDExpression_In `&` EqualityExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression_Yield : BitwiseANDExpression_Yield `&` EqualityExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression_In_Yield : BitwiseANDExpression_In_Yield `&` EqualityExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression_Await : BitwiseANDExpression_Await `&` EqualityExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression_In_Await : BitwiseANDExpression_In_Await `&` EqualityExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression_Yield_Await : BitwiseANDExpression_Yield_Await `&` EqualityExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseANDExpression_In_Yield_Await : BitwiseANDExpression_In_Yield_Await `&` EqualityExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression : BitwiseANDExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression_In : BitwiseANDExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression_Yield : BitwiseANDExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression_In_Yield : BitwiseANDExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression_Await : BitwiseANDExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression_In_Await : BitwiseANDExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression_Yield_Await : BitwiseANDExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression_In_Yield_Await : BitwiseANDExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression : BitwiseXORExpression `^` BitwiseANDExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression_In : BitwiseXORExpression_In `^` BitwiseANDExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression_Yield : BitwiseXORExpression_Yield `^` BitwiseANDExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression_In_Yield : BitwiseXORExpression_In_Yield `^` BitwiseANDExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression_Await : BitwiseXORExpression_Await `^` BitwiseANDExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression_In_Await : BitwiseXORExpression_In_Await `^` BitwiseANDExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression_Yield_Await : BitwiseXORExpression_Yield_Await `^` BitwiseANDExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseXORExpression_In_Yield_Await : BitwiseXORExpression_In_Yield_Await `^` BitwiseANDExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression : BitwiseXORExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression_In : BitwiseXORExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression_Yield : BitwiseXORExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression_In_Yield : BitwiseXORExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression_Await : BitwiseXORExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression_In_Await : BitwiseXORExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression_Yield_Await : BitwiseXORExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression_In_Yield_Await : BitwiseXORExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression : BitwiseORExpression `|` BitwiseXORExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression_In : BitwiseORExpression_In `|` BitwiseXORExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression_Yield : BitwiseORExpression_Yield `|` BitwiseXORExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression_In_Yield : BitwiseORExpression_In_Yield `|` BitwiseXORExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression_Await : BitwiseORExpression_Await `|` BitwiseXORExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression_In_Await : BitwiseORExpression_In_Await `|` BitwiseXORExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression_Yield_Await : BitwiseORExpression_Yield_Await `|` BitwiseXORExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
@builder.build('BitwiseORExpression_In_Yield_Await : BitwiseORExpression_In_Yield_Await `|` BitwiseXORExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression : BitwiseORExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression_In : BitwiseORExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression_Yield : BitwiseORExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression_In_Yield : BitwiseORExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression_Await : BitwiseORExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression_In_Await : BitwiseORExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression_Yield_Await : BitwiseORExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression_In_Yield_Await : BitwiseORExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression : LogicalANDExpression `&&` BitwiseORExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression_In : LogicalANDExpression_In `&&` BitwiseORExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression_Yield : LogicalANDExpression_Yield `&&` BitwiseORExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression_In_Yield : LogicalANDExpression_In_Yield `&&` BitwiseORExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression_Await : LogicalANDExpression_Await `&&` BitwiseORExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression_In_Await : LogicalANDExpression_In_Await `&&` BitwiseORExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression_Yield_Await : LogicalANDExpression_Yield_Await `&&` BitwiseORExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
@builder.build('LogicalANDExpression_In_Yield_Await : LogicalANDExpression_In_Yield_Await `&&` BitwiseORExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression : LogicalANDExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression_In : LogicalANDExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression_Yield : LogicalANDExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression_In_Yield : LogicalANDExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression_Await : LogicalANDExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression_In_Await : LogicalANDExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression_Yield_Await : LogicalANDExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression_In_Yield_Await : LogicalANDExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression : LogicalORExpression `||` LogicalANDExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression_In : LogicalORExpression_In `||` LogicalANDExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression_Yield : LogicalORExpression_Yield `||` LogicalANDExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression_In_Yield : LogicalORExpression_In_Yield `||` LogicalANDExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression_Await : LogicalORExpression_Await `||` LogicalANDExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression_In_Await : LogicalORExpression_In_Await `||` LogicalANDExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression_Yield_Await : LogicalORExpression_Yield_Await `||` LogicalANDExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
@builder.build('LogicalORExpression_In_Yield_Await : LogicalORExpression_In_Yield_Await `||` LogicalANDExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression : LogicalORExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression_In : LogicalORExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression_Yield : LogicalORExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression_In_Yield : LogicalORExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression_Await : LogicalORExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression_In_Await : LogicalORExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression_Yield_Await : LogicalORExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression_In_Yield_Await : LogicalORExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression : LogicalORExpression `?` AssignmentExpression_In `:` AssignmentExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression_In : LogicalORExpression_In `?` AssignmentExpression_In `:` AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression_Yield : LogicalORExpression_Yield `?` AssignmentExpression_In_Yield `:` AssignmentExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression_In_Yield : LogicalORExpression_In_Yield `?` AssignmentExpression_In_Yield `:` AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression_Await : LogicalORExpression_Await `?` AssignmentExpression_In_Await `:` AssignmentExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression_In_Await : LogicalORExpression_In_Await `?` AssignmentExpression_In_Await `:` AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression_Yield_Await : LogicalORExpression_Yield_Await `?` AssignmentExpression_In_Yield_Await `:` AssignmentExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('ConditionalExpression_In_Yield_Await : LogicalORExpression_In_Yield_Await `?` AssignmentExpression_In_Yield_Await `:` AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression : ConditionalExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In : ConditionalExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_Yield : ConditionalExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In_Yield : ConditionalExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_Await : ConditionalExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In_Await : ConditionalExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_Yield_Await : ConditionalExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In_Yield_Await : ConditionalExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : [+Yield] YieldExpression[?In, ?Await]
@builder.build('AssignmentExpression_Yield : YieldExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : [+Yield] YieldExpression[?In, ?Await]
@builder.build('AssignmentExpression_In_Yield : YieldExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : [+Yield] YieldExpression[?In, ?Await]
@builder.build('AssignmentExpression_Yield_Await : YieldExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : [+Yield] YieldExpression[?In, ?Await]
@builder.build('AssignmentExpression_In_Yield_Await : YieldExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression : ArrowFunction')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In : ArrowFunction_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_Yield : ArrowFunction_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In_Yield : ArrowFunction_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_Await : ArrowFunction_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In_Await : ArrowFunction_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_Yield_Await : ArrowFunction_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In_Yield_Await : ArrowFunction_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression : AsyncArrowFunction')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In : AsyncArrowFunction_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_Yield : AsyncArrowFunction_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In_Yield : AsyncArrowFunction_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_Await : AsyncArrowFunction_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In_Await : AsyncArrowFunction_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_Yield_Await : AsyncArrowFunction_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In_Yield_Await : AsyncArrowFunction_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
@builder.build('AssignmentExpression : LeftHandSideExpression `=` AssignmentExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
@builder.build('AssignmentExpression_In : LeftHandSideExpression `=` AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
@builder.build('AssignmentExpression_Yield : LeftHandSideExpression_Yield `=` AssignmentExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
@builder.build('AssignmentExpression_In_Yield : LeftHandSideExpression_Yield `=` AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
@builder.build('AssignmentExpression_Await : LeftHandSideExpression_Await `=` AssignmentExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
@builder.build('AssignmentExpression_In_Await : LeftHandSideExpression_Await `=` AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
@builder.build('AssignmentExpression_Yield_Await : LeftHandSideExpression_Yield_Await `=` AssignmentExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
@builder.build('AssignmentExpression_In_Yield_Await : LeftHandSideExpression_Yield_Await `=` AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression : LeftHandSideExpression AssignmentOperator AssignmentExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In : LeftHandSideExpression AssignmentOperator AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_Yield : LeftHandSideExpression_Yield AssignmentOperator AssignmentExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In_Yield : LeftHandSideExpression_Yield AssignmentOperator AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_Await : LeftHandSideExpression_Await AssignmentOperator AssignmentExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In_Await : LeftHandSideExpression_Await AssignmentOperator AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_Yield_Await : LeftHandSideExpression_Yield_Await AssignmentOperator AssignmentExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('AssignmentExpression_In_Yield_Await : LeftHandSideExpression_Yield_Await AssignmentOperator AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
@builder.build('AssignmentOperator : `*=`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
@builder.build('AssignmentOperator : `/=`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
@builder.build('AssignmentOperator : `%=`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
@builder.build('AssignmentOperator : `+=`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
@builder.build('AssignmentOperator : `-=`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
@builder.build('AssignmentOperator : `<<=`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
@builder.build('AssignmentOperator : `>>=`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
@builder.build('AssignmentOperator : `>>>=`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
@builder.build('AssignmentOperator : `&=`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
@builder.build('AssignmentOperator : `^=`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
@builder.build('AssignmentOperator : `|=`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
@builder.build('AssignmentOperator : `**=`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPattern[Yield, Await]  : ObjectAssignmentPattern[?Yield, ?Await]
@builder.build('AssignmentPattern : ObjectAssignmentPattern')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPattern[Yield, Await]  : ObjectAssignmentPattern[?Yield, ?Await]
@builder.build('AssignmentPattern_Yield : ObjectAssignmentPattern_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPattern[Yield, Await]  : ObjectAssignmentPattern[?Yield, ?Await]
@builder.build('AssignmentPattern_Await : ObjectAssignmentPattern_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPattern[Yield, Await]  : ObjectAssignmentPattern[?Yield, ?Await]
@builder.build('AssignmentPattern_Yield_Await : ObjectAssignmentPattern_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPattern[Yield, Await]  : ArrayAssignmentPattern[?Yield, ?Await]
@builder.build('AssignmentPattern : ArrayAssignmentPattern')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPattern[Yield, Await]  : ArrayAssignmentPattern[?Yield, ?Await]
@builder.build('AssignmentPattern_Yield : ArrayAssignmentPattern_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPattern[Yield, Await]  : ArrayAssignmentPattern[?Yield, ?Await]
@builder.build('AssignmentPattern_Await : ArrayAssignmentPattern_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPattern[Yield, Await]  : ArrayAssignmentPattern[?Yield, ?Await]
@builder.build('AssignmentPattern_Yield_Await : ArrayAssignmentPattern_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` `}`
@builder.build('ObjectAssignmentPattern : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` `}`
@builder.build('ObjectAssignmentPattern_Yield : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` `}`
@builder.build('ObjectAssignmentPattern_Await : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` `}`
@builder.build('ObjectAssignmentPattern_Yield_Await : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentRestProperty[?Yield, ?Await] `}`
@builder.build('ObjectAssignmentPattern : `{` AssignmentRestProperty `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentRestProperty[?Yield, ?Await] `}`
@builder.build('ObjectAssignmentPattern_Yield : `{` AssignmentRestProperty_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentRestProperty[?Yield, ?Await] `}`
@builder.build('ObjectAssignmentPattern_Await : `{` AssignmentRestProperty_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentRestProperty[?Yield, ?Await] `}`
@builder.build('ObjectAssignmentPattern_Yield_Await : `{` AssignmentRestProperty_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `}`
@builder.build('ObjectAssignmentPattern : `{` AssignmentPropertyList `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `}`
@builder.build('ObjectAssignmentPattern_Yield : `{` AssignmentPropertyList_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `}`
@builder.build('ObjectAssignmentPattern_Await : `{` AssignmentPropertyList_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `}`
@builder.build('ObjectAssignmentPattern_Yield_Await : `{` AssignmentPropertyList_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectAssignmentPattern : `{` AssignmentPropertyList `,` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectAssignmentPattern : `{` AssignmentPropertyList `,` AssignmentRestProperty `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectAssignmentPattern_Yield : `{` AssignmentPropertyList_Yield `,` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectAssignmentPattern_Yield : `{` AssignmentPropertyList_Yield `,` AssignmentRestProperty_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectAssignmentPattern_Await : `{` AssignmentPropertyList_Await `,` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectAssignmentPattern_Await : `{` AssignmentPropertyList_Await `,` AssignmentRestProperty_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectAssignmentPattern_Yield_Await : `{` AssignmentPropertyList_Yield_Await `,` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectAssignmentPattern_Yield_Await : `{` AssignmentPropertyList_Yield_Await `,` AssignmentRestProperty_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern : `[` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern : `[` AssignmentRestElement `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern : `[` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern : `[` Elision AssignmentRestElement `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield : `[` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield : `[` AssignmentRestElement_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield : `[` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield : `[` Elision AssignmentRestElement_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Await : `[` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Await : `[` AssignmentRestElement_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Await : `[` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Await : `[` Elision AssignmentRestElement_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield_Await : `[` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield_Await : `[` AssignmentRestElement_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield_Await : `[` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield_Await : `[` Elision AssignmentRestElement_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `]`
@builder.build('ArrayAssignmentPattern : `[` AssignmentElementList `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `]`
@builder.build('ArrayAssignmentPattern_Yield : `[` AssignmentElementList_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `]`
@builder.build('ArrayAssignmentPattern_Await : `[` AssignmentElementList_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `]`
@builder.build('ArrayAssignmentPattern_Yield_Await : `[` AssignmentElementList_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern : `[` AssignmentElementList `,` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern : `[` AssignmentElementList `,` AssignmentRestElement `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern : `[` AssignmentElementList `,` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern : `[` AssignmentElementList `,` Elision AssignmentRestElement `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield : `[` AssignmentElementList_Yield `,` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield : `[` AssignmentElementList_Yield `,` AssignmentRestElement_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield : `[` AssignmentElementList_Yield `,` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield : `[` AssignmentElementList_Yield `,` Elision AssignmentRestElement_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Await : `[` AssignmentElementList_Await `,` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Await : `[` AssignmentElementList_Await `,` AssignmentRestElement_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Await : `[` AssignmentElementList_Await `,` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Await : `[` AssignmentElementList_Await `,` Elision AssignmentRestElement_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield_Await : `[` AssignmentElementList_Yield_Await `,` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield_Await : `[` AssignmentElementList_Yield_Await `,` AssignmentRestElement_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield_Await : `[` AssignmentElementList_Yield_Await `,` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayAssignmentPattern_Yield_Await : `[` AssignmentElementList_Yield_Await `,` Elision AssignmentRestElement_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentRestProperty[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
@builder.build('AssignmentRestProperty : `...` DestructuringAssignmentTarget')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentRestProperty[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
@builder.build('AssignmentRestProperty_Yield : `...` DestructuringAssignmentTarget_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentRestProperty[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
@builder.build('AssignmentRestProperty_Await : `...` DestructuringAssignmentTarget_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentRestProperty[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
@builder.build('AssignmentRestProperty_Yield_Await : `...` DestructuringAssignmentTarget_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPropertyList[Yield, Await]  : AssignmentProperty[?Yield, ?Await]
@builder.build('AssignmentPropertyList : AssignmentProperty')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPropertyList[Yield, Await]  : AssignmentProperty[?Yield, ?Await]
@builder.build('AssignmentPropertyList_Yield : AssignmentProperty_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPropertyList[Yield, Await]  : AssignmentProperty[?Yield, ?Await]
@builder.build('AssignmentPropertyList_Await : AssignmentProperty_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPropertyList[Yield, Await]  : AssignmentProperty[?Yield, ?Await]
@builder.build('AssignmentPropertyList_Yield_Await : AssignmentProperty_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPropertyList[Yield, Await]  : AssignmentPropertyList[?Yield, ?Await] `,` AssignmentProperty[?Yield, ?Await]
@builder.build('AssignmentPropertyList : AssignmentPropertyList `,` AssignmentProperty')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPropertyList[Yield, Await]  : AssignmentPropertyList[?Yield, ?Await] `,` AssignmentProperty[?Yield, ?Await]
@builder.build('AssignmentPropertyList_Yield : AssignmentPropertyList_Yield `,` AssignmentProperty_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPropertyList[Yield, Await]  : AssignmentPropertyList[?Yield, ?Await] `,` AssignmentProperty[?Yield, ?Await]
@builder.build('AssignmentPropertyList_Await : AssignmentPropertyList_Await `,` AssignmentProperty_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentPropertyList[Yield, Await]  : AssignmentPropertyList[?Yield, ?Await] `,` AssignmentProperty[?Yield, ?Await]
@builder.build('AssignmentPropertyList_Yield_Await : AssignmentPropertyList_Yield_Await `,` AssignmentProperty_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElementList[Yield, Await]  : AssignmentElisionElement[?Yield, ?Await]
@builder.build('AssignmentElementList : AssignmentElisionElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElementList[Yield, Await]  : AssignmentElisionElement[?Yield, ?Await]
@builder.build('AssignmentElementList_Yield : AssignmentElisionElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElementList[Yield, Await]  : AssignmentElisionElement[?Yield, ?Await]
@builder.build('AssignmentElementList_Await : AssignmentElisionElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElementList[Yield, Await]  : AssignmentElisionElement[?Yield, ?Await]
@builder.build('AssignmentElementList_Yield_Await : AssignmentElisionElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElementList[Yield, Await]  : AssignmentElementList[?Yield, ?Await] `,` AssignmentElisionElement[?Yield, ?Await]
@builder.build('AssignmentElementList : AssignmentElementList `,` AssignmentElisionElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElementList[Yield, Await]  : AssignmentElementList[?Yield, ?Await] `,` AssignmentElisionElement[?Yield, ?Await]
@builder.build('AssignmentElementList_Yield : AssignmentElementList_Yield `,` AssignmentElisionElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElementList[Yield, Await]  : AssignmentElementList[?Yield, ?Await] `,` AssignmentElisionElement[?Yield, ?Await]
@builder.build('AssignmentElementList_Await : AssignmentElementList_Await `,` AssignmentElisionElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElementList[Yield, Await]  : AssignmentElementList[?Yield, ?Await] `,` AssignmentElisionElement[?Yield, ?Await]
@builder.build('AssignmentElementList_Yield_Await : AssignmentElementList_Yield_Await `,` AssignmentElisionElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
@builder.build('AssignmentElisionElement : AssignmentElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
@builder.build('AssignmentElisionElement : Elision AssignmentElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
@builder.build('AssignmentElisionElement_Yield : AssignmentElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
@builder.build('AssignmentElisionElement_Yield : Elision AssignmentElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
@builder.build('AssignmentElisionElement_Await : AssignmentElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
@builder.build('AssignmentElisionElement_Await : Elision AssignmentElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
@builder.build('AssignmentElisionElement_Yield_Await : AssignmentElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
@builder.build('AssignmentElisionElement_Yield_Await : Elision AssignmentElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentProperty : IdentifierReference')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentProperty : IdentifierReference Initializer_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentProperty_Yield : IdentifierReference_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentProperty_Yield : IdentifierReference_Yield Initializer_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentProperty_Await : IdentifierReference_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentProperty_Await : IdentifierReference_Await Initializer_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentProperty_Yield_Await : IdentifierReference_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentProperty_Yield_Await : IdentifierReference_Yield_Await Initializer_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentProperty[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentElement[?Yield, ?Await]
@builder.build('AssignmentProperty : PropertyName `:` AssignmentElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentProperty[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentElement[?Yield, ?Await]
@builder.build('AssignmentProperty_Yield : PropertyName_Yield `:` AssignmentElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentProperty[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentElement[?Yield, ?Await]
@builder.build('AssignmentProperty_Await : PropertyName_Await `:` AssignmentElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentProperty[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentElement[?Yield, ?Await]
@builder.build('AssignmentProperty_Yield_Await : PropertyName_Yield_Await `:` AssignmentElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentElement : DestructuringAssignmentTarget')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentElement : DestructuringAssignmentTarget Initializer_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentElement_Yield : DestructuringAssignmentTarget_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentElement_Yield : DestructuringAssignmentTarget_Yield Initializer_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentElement_Await : DestructuringAssignmentTarget_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentElement_Await : DestructuringAssignmentTarget_Await Initializer_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentElement_Yield_Await : DestructuringAssignmentTarget_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('AssignmentElement_Yield_Await : DestructuringAssignmentTarget_Yield_Await Initializer_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentRestElement[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
@builder.build('AssignmentRestElement : `...` DestructuringAssignmentTarget')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentRestElement[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
@builder.build('AssignmentRestElement_Yield : `...` DestructuringAssignmentTarget_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentRestElement[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
@builder.build('AssignmentRestElement_Await : `...` DestructuringAssignmentTarget_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#AssignmentRestElement[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
@builder.build('AssignmentRestElement_Yield_Await : `...` DestructuringAssignmentTarget_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DestructuringAssignmentTarget[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
@builder.build('DestructuringAssignmentTarget : LeftHandSideExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DestructuringAssignmentTarget[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
@builder.build('DestructuringAssignmentTarget_Yield : LeftHandSideExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DestructuringAssignmentTarget[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
@builder.build('DestructuringAssignmentTarget_Await : LeftHandSideExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DestructuringAssignmentTarget[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
@builder.build('DestructuringAssignmentTarget_Yield_Await : LeftHandSideExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression : AssignmentExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression_In : AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression_Yield : AssignmentExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression_In_Yield : AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression_Await : AssignmentExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression_In_Await : AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression_Yield_Await : AssignmentExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression_In_Yield_Await : AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression : Expression `,` AssignmentExpression')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression_In : Expression_In `,` AssignmentExpression_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression_Yield : Expression_Yield `,` AssignmentExpression_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression_In_Yield : Expression_In_Yield `,` AssignmentExpression_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression_Await : Expression_Await `,` AssignmentExpression_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression_In_Await : Expression_In_Await `,` AssignmentExpression_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression_Yield_Await : Expression_Yield_Await `,` AssignmentExpression_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
@builder.build('Expression_In_Yield_Await : Expression_In_Yield_Await `,` AssignmentExpression_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

