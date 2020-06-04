from language import Builder
builder = Builder.get_builder()

#IdentifierReference[Yield, Await]  : Identifier
builder.r(w=1, d='IdentifierReference : Identifier')

#IdentifierReference[Yield, Await]  : Identifier
builder.r(w=1, d='IdentifierReference_Yield : Identifier')

#IdentifierReference[Yield, Await]  : Identifier
builder.r(w=1, d='IdentifierReference_Await : Identifier')

#IdentifierReference[Yield, Await]  : Identifier
builder.r(w=1, d='IdentifierReference_Yield_Await : Identifier')

#IdentifierReference[Yield, Await]  : [~Yield] `yield`
builder.r(w=1, d='IdentifierReference : `yield`')

#IdentifierReference[Yield, Await]  : [~Yield] `yield`
builder.r(w=1, d='IdentifierReference_Await : `yield`')

#IdentifierReference[Yield, Await]  : [~Await] `await`
builder.r(w=1, d='IdentifierReference : `await`')

#IdentifierReference[Yield, Await]  : [~Await] `await`
builder.r(w=1, d='IdentifierReference_Yield : `await`')

#BindingIdentifier[Yield, Await]  : Identifier
builder.r(w=1, d='BindingIdentifier : Identifier')

#BindingIdentifier[Yield, Await]  : Identifier
builder.r(w=1, d='BindingIdentifier_Yield : Identifier')

#BindingIdentifier[Yield, Await]  : Identifier
builder.r(w=1, d='BindingIdentifier_Await : Identifier')

#BindingIdentifier[Yield, Await]  : Identifier
builder.r(w=1, d='BindingIdentifier_Yield_Await : Identifier')

#BindingIdentifier[Yield, Await]  : `yield`
#builder.r(w=1, d='BindingIdentifier : `yield`')

#BindingIdentifier[Yield, Await]  : `yield`
#builder.r(w=1, d='BindingIdentifier_Yield : `yield`')

#BindingIdentifier[Yield, Await]  : `yield`
#builder.r(w=1, d='BindingIdentifier_Await : `yield`')

#BindingIdentifier[Yield, Await]  : `yield`
#builder.r(w=1, d='BindingIdentifier_Yield_Await : `yield`')

#BindingIdentifier[Yield, Await]  : `await`
#builder.r(w=1, d='BindingIdentifier : `await`')

#BindingIdentifier[Yield, Await]  : `await`
#builder.r(w=1, d='BindingIdentifier_Yield : `await`')

#BindingIdentifier[Yield, Await]  : `await`
#builder.r(w=1, d='BindingIdentifier_Await : `await`')

#BindingIdentifier[Yield, Await]  : `await`
#builder.r(w=1, d='BindingIdentifier_Yield_Await : `await`')

#LabelIdentifier[Yield, Await]  : Identifier
builder.r(w=1, d='LabelIdentifier : Identifier')

#LabelIdentifier[Yield, Await]  : Identifier
builder.r(w=1, d='LabelIdentifier_Yield : Identifier')

#LabelIdentifier[Yield, Await]  : Identifier
builder.r(w=1, d='LabelIdentifier_Await : Identifier')

#LabelIdentifier[Yield, Await]  : Identifier
builder.r(w=1, d='LabelIdentifier_Yield_Await : Identifier')

#LabelIdentifier[Yield, Await]  : [~Yield] `yield`
#builder.r(w=1, d='LabelIdentifier : `yield`')

#LabelIdentifier[Yield, Await]  : [~Yield] `yield`
#builder.r(w=1, d='LabelIdentifier_Await : `yield`')

#LabelIdentifier[Yield, Await]  : [~Await] `await`
#builder.r(w=1, d='LabelIdentifier : `await`')

#LabelIdentifier[Yield, Await]  : [~Await] `await`
#builder.r(w=1, d='LabelIdentifier_Yield : `await`')

#Identifier  : IdentifierName
builder.r(w=1, d='Identifier : IdentifierName')

#PrimaryExpression[Yield, Await]  : `this`
builder.r(w=1, d='PrimaryExpression : `this`')

#PrimaryExpression[Yield, Await]  : `this`
builder.r(w=1, d='PrimaryExpression_Yield : `this`')

#PrimaryExpression[Yield, Await]  : `this`
builder.r(w=1, d='PrimaryExpression_Await : `this`')

#PrimaryExpression[Yield, Await]  : `this`
builder.r(w=1, d='PrimaryExpression_Yield_Await : `this`')

#PrimaryExpression[Yield, Await]  : IdentifierReference[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression : IdentifierReference')

#PrimaryExpression[Yield, Await]  : IdentifierReference[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression_Yield : IdentifierReference_Yield')

#PrimaryExpression[Yield, Await]  : IdentifierReference[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression_Await : IdentifierReference_Await')

#PrimaryExpression[Yield, Await]  : IdentifierReference[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression_Yield_Await : IdentifierReference_Yield_Await')

#PrimaryExpression[Yield, Await]  : Literal
builder.r(w=1, d='PrimaryExpression : Literal')

#PrimaryExpression[Yield, Await]  : Literal
builder.r(w=1, d='PrimaryExpression_Yield : Literal')

#PrimaryExpression[Yield, Await]  : Literal
builder.r(w=1, d='PrimaryExpression_Await : Literal')

#PrimaryExpression[Yield, Await]  : Literal
builder.r(w=1, d='PrimaryExpression_Yield_Await : Literal')

#PrimaryExpression[Yield, Await]  : ArrayLiteral[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression : ArrayLiteral')

#PrimaryExpression[Yield, Await]  : ArrayLiteral[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression_Yield : ArrayLiteral_Yield')

#PrimaryExpression[Yield, Await]  : ArrayLiteral[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression_Await : ArrayLiteral_Await')

#PrimaryExpression[Yield, Await]  : ArrayLiteral[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression_Yield_Await : ArrayLiteral_Yield_Await')

#PrimaryExpression[Yield, Await]  : ObjectLiteral[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression : ObjectLiteral')

#PrimaryExpression[Yield, Await]  : ObjectLiteral[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression_Yield : ObjectLiteral_Yield')

#PrimaryExpression[Yield, Await]  : ObjectLiteral[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression_Await : ObjectLiteral_Await')

#PrimaryExpression[Yield, Await]  : ObjectLiteral[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression_Yield_Await : ObjectLiteral_Yield_Await')

#PrimaryExpression[Yield, Await]  : FunctionExpression
builder.r(w=1, d='PrimaryExpression : FunctionExpression')

#PrimaryExpression[Yield, Await]  : FunctionExpression
builder.r(w=1, d='PrimaryExpression_Yield : FunctionExpression')

#PrimaryExpression[Yield, Await]  : FunctionExpression
builder.r(w=1, d='PrimaryExpression_Await : FunctionExpression')

#PrimaryExpression[Yield, Await]  : FunctionExpression
builder.r(w=1, d='PrimaryExpression_Yield_Await : FunctionExpression')

#PrimaryExpression[Yield, Await]  : ClassExpression[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression : ClassExpression')

#PrimaryExpression[Yield, Await]  : ClassExpression[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression_Yield : ClassExpression_Yield')

#PrimaryExpression[Yield, Await]  : ClassExpression[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression_Await : ClassExpression_Await')

#PrimaryExpression[Yield, Await]  : ClassExpression[?Yield, ?Await]
builder.r(w=1, d='PrimaryExpression_Yield_Await : ClassExpression_Yield_Await')

#PrimaryExpression[Yield, Await]  : GeneratorExpression
builder.r(w=1, d='PrimaryExpression : GeneratorExpression')

#PrimaryExpression[Yield, Await]  : GeneratorExpression
builder.r(w=1, d='PrimaryExpression_Yield : GeneratorExpression')

#PrimaryExpression[Yield, Await]  : GeneratorExpression
builder.r(w=1, d='PrimaryExpression_Await : GeneratorExpression')

#PrimaryExpression[Yield, Await]  : GeneratorExpression
builder.r(w=1, d='PrimaryExpression_Yield_Await : GeneratorExpression')

#PrimaryExpression[Yield, Await]  : AsyncFunctionExpression
builder.r(w=1, d='PrimaryExpression : AsyncFunctionExpression')

#PrimaryExpression[Yield, Await]  : AsyncFunctionExpression
builder.r(w=1, d='PrimaryExpression_Yield : AsyncFunctionExpression')

#PrimaryExpression[Yield, Await]  : AsyncFunctionExpression
builder.r(w=1, d='PrimaryExpression_Await : AsyncFunctionExpression')

#PrimaryExpression[Yield, Await]  : AsyncFunctionExpression
builder.r(w=1, d='PrimaryExpression_Yield_Await : AsyncFunctionExpression')

#PrimaryExpression[Yield, Await]  : AsyncGeneratorExpression
builder.r(w=1, d='PrimaryExpression : AsyncGeneratorExpression')

#PrimaryExpression[Yield, Await]  : AsyncGeneratorExpression
builder.r(w=1, d='PrimaryExpression_Yield : AsyncGeneratorExpression')

#PrimaryExpression[Yield, Await]  : AsyncGeneratorExpression
builder.r(w=1, d='PrimaryExpression_Await : AsyncGeneratorExpression')

#PrimaryExpression[Yield, Await]  : AsyncGeneratorExpression
builder.r(w=1, d='PrimaryExpression_Yield_Await : AsyncGeneratorExpression')

#PrimaryExpression[Yield, Await]  : RegularExpressionLiteral
builder.r(w=1, d='PrimaryExpression : RegularExpressionLiteral')

#PrimaryExpression[Yield, Await]  : RegularExpressionLiteral
builder.r(w=1, d='PrimaryExpression_Yield : RegularExpressionLiteral')

#PrimaryExpression[Yield, Await]  : RegularExpressionLiteral
builder.r(w=1, d='PrimaryExpression_Await : RegularExpressionLiteral')

#PrimaryExpression[Yield, Await]  : RegularExpressionLiteral
builder.r(w=1, d='PrimaryExpression_Yield_Await : RegularExpressionLiteral')

#PrimaryExpression[Yield, Await]  : TemplateLiteral[?Yield, ?Await, ~Tagged]
builder.r(w=1, d='PrimaryExpression : TemplateLiteral')

#PrimaryExpression[Yield, Await]  : TemplateLiteral[?Yield, ?Await, ~Tagged]
builder.r(w=1, d='PrimaryExpression_Yield : TemplateLiteral_Yield')

#PrimaryExpression[Yield, Await]  : TemplateLiteral[?Yield, ?Await, ~Tagged]
builder.r(w=1, d='PrimaryExpression_Await : TemplateLiteral_Await')

#PrimaryExpression[Yield, Await]  : TemplateLiteral[?Yield, ?Await, ~Tagged]
builder.r(w=1, d='PrimaryExpression_Yield_Await : TemplateLiteral_Yield_Await')

#PrimaryExpression[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
builder.r(w=1, d='PrimaryExpression : CoverParenthesizedExpressionAndArrowParameterList')

#PrimaryExpression[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
builder.r(w=1, d='PrimaryExpression_Yield : CoverParenthesizedExpressionAndArrowParameterList_Yield')

#PrimaryExpression[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
builder.r(w=1, d='PrimaryExpression_Await : CoverParenthesizedExpressionAndArrowParameterList_Await')

#PrimaryExpression[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
builder.r(w=1, d='PrimaryExpression_Yield_Await : CoverParenthesizedExpressionAndArrowParameterList_Yield_Await')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList : `(` Expression_In `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Yield : `(` Expression_In_Yield `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Await : `(` Expression_In_Await `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Yield_Await : `(` Expression_In_Yield_Await `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList : `(` Expression_In `,` `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Yield : `(` Expression_In_Yield `,` `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Await : `(` Expression_In_Await `,` `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Yield_Await : `(` Expression_In_Yield_Await `,` `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList : `(` `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Yield : `(` `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Await : `(` `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Yield_Await : `(` `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingIdentifier[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList : `(` `...` BindingIdentifier `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingIdentifier[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Yield : `(` `...` BindingIdentifier_Yield `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingIdentifier[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Await : `(` `...` BindingIdentifier_Await `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingIdentifier[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Yield_Await : `(` `...` BindingIdentifier_Yield_Await `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingPattern[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList : `(` `...` BindingPattern `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingPattern[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Yield : `(` `...` BindingPattern_Yield `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingPattern[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Await : `(` `...` BindingPattern_Await `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` `...` BindingPattern[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Yield_Await : `(` `...` BindingPattern_Yield_Await `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingIdentifier[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList : `(` Expression_In `,` `...` BindingIdentifier `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingIdentifier[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Yield : `(` Expression_In_Yield `,` `...` BindingIdentifier_Yield `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingIdentifier[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Await : `(` Expression_In_Await `,` `...` BindingIdentifier_Await `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingIdentifier[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Yield_Await : `(` Expression_In_Yield_Await `,` `...` BindingIdentifier_Yield_Await `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingPattern[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList : `(` Expression_In `,` `...` BindingPattern `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingPattern[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Yield : `(` Expression_In_Yield `,` `...` BindingPattern_Yield `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingPattern[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Await : `(` Expression_In_Await `,` `...` BindingPattern_Await `)`')

#CoverParenthesizedExpressionAndArrowParameterList[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `,` `...` BindingPattern[?Yield, ?Await] `)`
builder.r(w=1, d='CoverParenthesizedExpressionAndArrowParameterList_Yield_Await : `(` Expression_In_Yield_Await `,` `...` BindingPattern_Yield_Await `)`')

#ParenthesizedExpression[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
builder.r(w=1, d='ParenthesizedExpression : `(` Expression_In `)`')

#ParenthesizedExpression[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
builder.r(w=1, d='ParenthesizedExpression_Yield : `(` Expression_In_Yield `)`')

#ParenthesizedExpression[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
builder.r(w=1, d='ParenthesizedExpression_Await : `(` Expression_In_Await `)`')

#ParenthesizedExpression[Yield, Await]  : `(` Expression[+In, ?Yield, ?Await] `)`
builder.r(w=1, d='ParenthesizedExpression_Yield_Await : `(` Expression_In_Yield_Await `)`')

#Literal  : NullLiteral
builder.r(w=1, d='Literal : NullLiteral')

#Literal  : BooleanLiteral
builder.r(w=1, d='Literal : BooleanLiteral')

#Literal  : NumericLiteral
builder.r(w=1, d='Literal : NumericLiteral')

#Literal  : StringLiteral
builder.r(w=1, d='Literal : StringLiteral')

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
builder.r(w=1, d='ArrayLiteral : `[` `]`')

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
builder.r(w=1, d='ArrayLiteral : `[` Elision `]`')

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
builder.r(w=1, d='ArrayLiteral_Yield : `[` `]`')

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
builder.r(w=1, d='ArrayLiteral_Yield : `[` Elision `]`')

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
builder.r(w=1, d='ArrayLiteral_Await : `[` `]`')

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
builder.r(w=1, d='ArrayLiteral_Await : `[` Elision `]`')

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
builder.r(w=1, d='ArrayLiteral_Yield_Await : `[` `]`')

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
builder.r(w=1, d='ArrayLiteral_Yield_Await : `[` Elision `]`')

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `]`
builder.r(w=1, d='ArrayLiteral : `[` ElementList `]`')

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `]`
builder.r(w=1, d='ArrayLiteral_Yield : `[` ElementList_Yield `]`')

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `]`
builder.r(w=1, d='ArrayLiteral_Await : `[` ElementList_Await `]`')

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `]`
builder.r(w=1, d='ArrayLiteral_Yield_Await : `[` ElementList_Yield_Await `]`')

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
builder.r(w=1, d='ArrayLiteral : `[` ElementList `,` `]`')

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
builder.r(w=1, d='ArrayLiteral : `[` ElementList `,` Elision `]`')

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
builder.r(w=1, d='ArrayLiteral_Yield : `[` ElementList_Yield `,` `]`')

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
builder.r(w=1, d='ArrayLiteral_Yield : `[` ElementList_Yield `,` Elision `]`')

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
builder.r(w=1, d='ArrayLiteral_Await : `[` ElementList_Await `,` `]`')

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
builder.r(w=1, d='ArrayLiteral_Await : `[` ElementList_Await `,` Elision `]`')

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
builder.r(w=1, d='ArrayLiteral_Yield_Await : `[` ElementList_Yield_Await `,` `]`')

#ArrayLiteral[Yield, Await]  : `[` ElementList[?Yield, ?Await] `,` Elision? `]`
builder.r(w=1, d='ArrayLiteral_Yield_Await : `[` ElementList_Yield_Await `,` Elision `]`')

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList : AssignmentExpression_In')

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList : Elision AssignmentExpression_In')

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield : AssignmentExpression_In_Yield')

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield : Elision AssignmentExpression_In_Yield')

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList_Await : AssignmentExpression_In_Await')

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList_Await : Elision AssignmentExpression_In_Await')

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield_Await : AssignmentExpression_In_Yield_Await')

#ElementList[Yield, Await]  : Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield_Await : Elision AssignmentExpression_In_Yield_Await')

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList : SpreadElement')

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList : Elision SpreadElement')

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield : SpreadElement_Yield')

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield : Elision SpreadElement_Yield')

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList_Await : SpreadElement_Await')

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList_Await : Elision SpreadElement_Await')

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield_Await : SpreadElement_Yield_Await')

#ElementList[Yield, Await]  : Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield_Await : Elision SpreadElement_Yield_Await')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList : ElementList `,` AssignmentExpression_In')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList : ElementList `,` Elision AssignmentExpression_In')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield : ElementList_Yield `,` AssignmentExpression_In_Yield')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield : ElementList_Yield `,` Elision AssignmentExpression_In_Yield')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList_Await : ElementList_Await `,` AssignmentExpression_In_Await')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList_Await : ElementList_Await `,` Elision AssignmentExpression_In_Await')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield_Await : ElementList_Yield_Await `,` AssignmentExpression_In_Yield_Await')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield_Await : ElementList_Yield_Await `,` Elision AssignmentExpression_In_Yield_Await')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList : ElementList `,` SpreadElement')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList : ElementList `,` Elision SpreadElement')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield : ElementList_Yield `,` SpreadElement_Yield')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield : ElementList_Yield `,` Elision SpreadElement_Yield')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList_Await : ElementList_Await `,` SpreadElement_Await')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList_Await : ElementList_Await `,` Elision SpreadElement_Await')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield_Await : ElementList_Yield_Await `,` SpreadElement_Yield_Await')

#ElementList[Yield, Await]  : ElementList[?Yield, ?Await] `,` Elision? SpreadElement[?Yield, ?Await]
builder.r(w=1, d='ElementList_Yield_Await : ElementList_Yield_Await `,` Elision SpreadElement_Yield_Await')

#Elision  : `,`
builder.r(w=1, d='Elision : `,`')

#Elision  : Elision `,`
builder.r(w=1, d='Elision : Elision `,`')

#SpreadElement[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='SpreadElement : `...` AssignmentExpression_In')

#SpreadElement[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='SpreadElement_Yield : `...` AssignmentExpression_In_Yield')

#SpreadElement[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='SpreadElement_Await : `...` AssignmentExpression_In_Await')

#SpreadElement[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='SpreadElement_Yield_Await : `...` AssignmentExpression_In_Yield_Await')

#ObjectLiteral[Yield, Await]  : `{` `}`
builder.r(w=1, d='ObjectLiteral : `{` `}`')

#ObjectLiteral[Yield, Await]  : `{` `}`
builder.r(w=1, d='ObjectLiteral_Yield : `{` `}`')

#ObjectLiteral[Yield, Await]  : `{` `}`
builder.r(w=1, d='ObjectLiteral_Await : `{` `}`')

#ObjectLiteral[Yield, Await]  : `{` `}`
builder.r(w=1, d='ObjectLiteral_Yield_Await : `{` `}`')

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `}`
builder.r(w=1, d='ObjectLiteral : `{` PropertyDefinitionList `}`')

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `}`
builder.r(w=1, d='ObjectLiteral_Yield : `{` PropertyDefinitionList_Yield `}`')

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `}`
builder.r(w=1, d='ObjectLiteral_Await : `{` PropertyDefinitionList_Await `}`')

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `}`
builder.r(w=1, d='ObjectLiteral_Yield_Await : `{` PropertyDefinitionList_Yield_Await `}`')

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `,` `}`
builder.r(w=1, d='ObjectLiteral : `{` PropertyDefinitionList `,` `}`')

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `,` `}`
builder.r(w=1, d='ObjectLiteral_Yield : `{` PropertyDefinitionList_Yield `,` `}`')

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `,` `}`
builder.r(w=1, d='ObjectLiteral_Await : `{` PropertyDefinitionList_Await `,` `}`')

#ObjectLiteral[Yield, Await]  : `{` PropertyDefinitionList[?Yield, ?Await] `,` `}`
builder.r(w=1, d='ObjectLiteral_Yield_Await : `{` PropertyDefinitionList_Yield_Await `,` `}`')

#PropertyDefinitionList[Yield, Await]  : PropertyDefinition[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinitionList : PropertyDefinition')

#PropertyDefinitionList[Yield, Await]  : PropertyDefinition[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinitionList_Yield : PropertyDefinition_Yield')

#PropertyDefinitionList[Yield, Await]  : PropertyDefinition[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinitionList_Await : PropertyDefinition_Await')

#PropertyDefinitionList[Yield, Await]  : PropertyDefinition[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinitionList_Yield_Await : PropertyDefinition_Yield_Await')

#PropertyDefinitionList[Yield, Await]  : PropertyDefinitionList[?Yield, ?Await] `,` PropertyDefinition[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinitionList : PropertyDefinitionList `,` PropertyDefinition')

#PropertyDefinitionList[Yield, Await]  : PropertyDefinitionList[?Yield, ?Await] `,` PropertyDefinition[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinitionList_Yield : PropertyDefinitionList_Yield `,` PropertyDefinition_Yield')

#PropertyDefinitionList[Yield, Await]  : PropertyDefinitionList[?Yield, ?Await] `,` PropertyDefinition[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinitionList_Await : PropertyDefinitionList_Await `,` PropertyDefinition_Await')

#PropertyDefinitionList[Yield, Await]  : PropertyDefinitionList[?Yield, ?Await] `,` PropertyDefinition[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinitionList_Yield_Await : PropertyDefinitionList_Yield_Await `,` PropertyDefinition_Yield_Await')

#PropertyDefinition[Yield, Await]  : IdentifierReference[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition : IdentifierReference')

#PropertyDefinition[Yield, Await]  : IdentifierReference[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Yield : IdentifierReference_Yield')

#PropertyDefinition[Yield, Await]  : IdentifierReference[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Await : IdentifierReference_Await')

#PropertyDefinition[Yield, Await]  : IdentifierReference[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Yield_Await : IdentifierReference_Yield_Await')

#PropertyDefinition[Yield, Await]  : CoverInitializedName[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition : CoverInitializedName')

#PropertyDefinition[Yield, Await]  : CoverInitializedName[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Yield : CoverInitializedName_Yield')

#PropertyDefinition[Yield, Await]  : CoverInitializedName[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Await : CoverInitializedName_Await')

#PropertyDefinition[Yield, Await]  : CoverInitializedName[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Yield_Await : CoverInitializedName_Yield_Await')

#PropertyDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition : PropertyName `:` AssignmentExpression_In')

#PropertyDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Yield : PropertyName_Yield `:` AssignmentExpression_In_Yield')

#PropertyDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Await : PropertyName_Await `:` AssignmentExpression_In_Await')

#PropertyDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Yield_Await : PropertyName_Yield_Await `:` AssignmentExpression_In_Yield_Await')

#PropertyDefinition[Yield, Await]  : MethodDefinition[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition : MethodDefinition')

#PropertyDefinition[Yield, Await]  : MethodDefinition[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Yield : MethodDefinition_Yield')

#PropertyDefinition[Yield, Await]  : MethodDefinition[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Await : MethodDefinition_Await')

#PropertyDefinition[Yield, Await]  : MethodDefinition[?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Yield_Await : MethodDefinition_Yield_Await')

#PropertyDefinition[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition : `...` AssignmentExpression_In')

#PropertyDefinition[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Yield : `...` AssignmentExpression_In_Yield')

#PropertyDefinition[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Await : `...` AssignmentExpression_In_Await')

#PropertyDefinition[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='PropertyDefinition_Yield_Await : `...` AssignmentExpression_In_Yield_Await')

#PropertyName[Yield, Await]  : LiteralPropertyName
builder.r(w=1, d='PropertyName : LiteralPropertyName')

#PropertyName[Yield, Await]  : LiteralPropertyName
builder.r(w=1, d='PropertyName_Yield : LiteralPropertyName')

#PropertyName[Yield, Await]  : LiteralPropertyName
builder.r(w=1, d='PropertyName_Await : LiteralPropertyName')

#PropertyName[Yield, Await]  : LiteralPropertyName
builder.r(w=1, d='PropertyName_Yield_Await : LiteralPropertyName')

#PropertyName[Yield, Await]  : ComputedPropertyName[?Yield, ?Await]
builder.r(w=1, d='PropertyName : ComputedPropertyName')

#PropertyName[Yield, Await]  : ComputedPropertyName[?Yield, ?Await]
builder.r(w=1, d='PropertyName_Yield : ComputedPropertyName_Yield')

#PropertyName[Yield, Await]  : ComputedPropertyName[?Yield, ?Await]
builder.r(w=1, d='PropertyName_Await : ComputedPropertyName_Await')

#PropertyName[Yield, Await]  : ComputedPropertyName[?Yield, ?Await]
builder.r(w=1, d='PropertyName_Yield_Await : ComputedPropertyName_Yield_Await')

#LiteralPropertyName  : IdentifierName
builder.r(w=1, d='LiteralPropertyName : IdentifierName')

#LiteralPropertyName  : StringLiteral
builder.r(w=1, d='LiteralPropertyName : StringLiteral')

#LiteralPropertyName  : NumericLiteral
builder.r(w=1, d='LiteralPropertyName : NumericLiteral')

#ComputedPropertyName[Yield, Await]  : `[` AssignmentExpression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='ComputedPropertyName : `[` AssignmentExpression_In `]`')

#ComputedPropertyName[Yield, Await]  : `[` AssignmentExpression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='ComputedPropertyName_Yield : `[` AssignmentExpression_In_Yield `]`')

#ComputedPropertyName[Yield, Await]  : `[` AssignmentExpression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='ComputedPropertyName_Await : `[` AssignmentExpression_In_Await `]`')

#ComputedPropertyName[Yield, Await]  : `[` AssignmentExpression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='ComputedPropertyName_Yield_Await : `[` AssignmentExpression_In_Yield_Await `]`')

#CoverInitializedName[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]
builder.r(w=1, d='CoverInitializedName : IdentifierReference Initializer_In')

#CoverInitializedName[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]
builder.r(w=1, d='CoverInitializedName_Yield : IdentifierReference_Yield Initializer_In_Yield')

#CoverInitializedName[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]
builder.r(w=1, d='CoverInitializedName_Await : IdentifierReference_Await Initializer_In_Await')

#CoverInitializedName[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]
builder.r(w=1, d='CoverInitializedName_Yield_Await : IdentifierReference_Yield_Await Initializer_In_Yield_Await')

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Initializer : `=` AssignmentExpression')

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Initializer_In : `=` AssignmentExpression_In')

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Initializer_Yield : `=` AssignmentExpression_Yield')

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Initializer_In_Yield : `=` AssignmentExpression_In_Yield')

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Initializer_Await : `=` AssignmentExpression_Await')

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Initializer_In_Await : `=` AssignmentExpression_In_Await')

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Initializer_Yield_Await : `=` AssignmentExpression_Yield_Await')

#Initializer[In, Yield, Await]  : `=` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Initializer_In_Yield_Await : `=` AssignmentExpression_In_Yield_Await')

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
builder.r(w=1, d='TemplateLiteral : NoSubstitutionTemplate')

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
builder.r(w=1, d='TemplateLiteral_Yield : NoSubstitutionTemplate')

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
builder.r(w=1, d='TemplateLiteral_Await : NoSubstitutionTemplate')

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
builder.r(w=1, d='TemplateLiteral_Yield_Await : NoSubstitutionTemplate')

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
builder.r(w=1, d='TemplateLiteral_Tagged : NoSubstitutionTemplate')

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
builder.r(w=1, d='TemplateLiteral_Yield_Tagged : NoSubstitutionTemplate')

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
builder.r(w=1, d='TemplateLiteral_Await_Tagged : NoSubstitutionTemplate')

#TemplateLiteral[Yield, Await, Tagged]  : NoSubstitutionTemplate
builder.r(w=1, d='TemplateLiteral_Yield_Await_Tagged : NoSubstitutionTemplate')

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='TemplateLiteral : SubstitutionTemplate')

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='TemplateLiteral_Yield : SubstitutionTemplate_Yield')

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='TemplateLiteral_Await : SubstitutionTemplate_Await')

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='TemplateLiteral_Yield_Await : SubstitutionTemplate_Yield_Await')

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='TemplateLiteral_Tagged : SubstitutionTemplate_Tagged')

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='TemplateLiteral_Yield_Tagged : SubstitutionTemplate_Yield_Tagged')

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='TemplateLiteral_Await_Tagged : SubstitutionTemplate_Await_Tagged')

#TemplateLiteral[Yield, Await, Tagged]  : SubstitutionTemplate[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='TemplateLiteral_Yield_Await_Tagged : SubstitutionTemplate_Yield_Await_Tagged')

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='SubstitutionTemplate : TemplateHead Expression_In TemplateSpans')

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='SubstitutionTemplate_Yield : TemplateHead Expression_In_Yield TemplateSpans_Yield')

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='SubstitutionTemplate_Await : TemplateHead Expression_In_Await TemplateSpans_Await')

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='SubstitutionTemplate_Yield_Await : TemplateHead Expression_In_Yield_Await TemplateSpans_Yield_Await')

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='SubstitutionTemplate_Tagged : TemplateHead Expression_In TemplateSpans_Tagged')

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='SubstitutionTemplate_Yield_Tagged : TemplateHead Expression_In_Yield TemplateSpans_Yield_Tagged')

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='SubstitutionTemplate_Await_Tagged : TemplateHead Expression_In_Await TemplateSpans_Await_Tagged')

#SubstitutionTemplate[Yield, Await, Tagged]  : TemplateHead Expression[+In, ?Yield, ?Await] TemplateSpans[?Yield, ?Await, ?Tagged]
builder.r(w=1, d='SubstitutionTemplate_Yield_Await_Tagged : TemplateHead Expression_In_Yield_Await TemplateSpans_Yield_Await_Tagged')

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
builder.r(w=1, d='TemplateSpans : TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
builder.r(w=1, d='TemplateSpans_Yield : TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
builder.r(w=1, d='TemplateSpans_Await : TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
builder.r(w=1, d='TemplateSpans_Yield_Await : TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
builder.r(w=1, d='TemplateSpans_Tagged : TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
builder.r(w=1, d='TemplateSpans_Yield_Tagged : TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
builder.r(w=1, d='TemplateSpans_Await_Tagged : TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateTail
builder.r(w=1, d='TemplateSpans_Yield_Await_Tagged : TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
builder.r(w=1, d='TemplateSpans : TemplateMiddleList TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
builder.r(w=1, d='TemplateSpans_Yield : TemplateMiddleList_Yield TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
builder.r(w=1, d='TemplateSpans_Await : TemplateMiddleList_Await TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
builder.r(w=1, d='TemplateSpans_Yield_Await : TemplateMiddleList_Yield_Await TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
builder.r(w=1, d='TemplateSpans_Tagged : TemplateMiddleList_Tagged TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
builder.r(w=1, d='TemplateSpans_Yield_Tagged : TemplateMiddleList_Yield_Tagged TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
builder.r(w=1, d='TemplateSpans_Await_Tagged : TemplateMiddleList_Await_Tagged TemplateTail')

#TemplateSpans[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateTail
builder.r(w=1, d='TemplateSpans_Yield_Await_Tagged : TemplateMiddleList_Yield_Await_Tagged TemplateTail')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList : TemplateMiddle Expression_In')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList_Yield : TemplateMiddle Expression_In_Yield')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList_Await : TemplateMiddle Expression_In_Await')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList_Yield_Await : TemplateMiddle Expression_In_Yield_Await')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList_Tagged : TemplateMiddle Expression_In')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList_Yield_Tagged : TemplateMiddle Expression_In_Yield')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList_Await_Tagged : TemplateMiddle Expression_In_Await')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList_Yield_Await_Tagged : TemplateMiddle Expression_In_Yield_Await')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList : TemplateMiddleList TemplateMiddle Expression_In')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList_Yield : TemplateMiddleList_Yield TemplateMiddle Expression_In_Yield')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList_Await : TemplateMiddleList_Await TemplateMiddle Expression_In_Await')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList_Yield_Await : TemplateMiddleList_Yield_Await TemplateMiddle Expression_In_Yield_Await')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList_Tagged : TemplateMiddleList_Tagged TemplateMiddle Expression_In')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList_Yield_Tagged : TemplateMiddleList_Yield_Tagged TemplateMiddle Expression_In_Yield')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList_Await_Tagged : TemplateMiddleList_Await_Tagged TemplateMiddle Expression_In_Await')

#TemplateMiddleList[Yield, Await, Tagged]  : TemplateMiddleList[?Yield, ?Await, ?Tagged] TemplateMiddle Expression[+In, ?Yield, ?Await]
builder.r(w=1, d='TemplateMiddleList_Yield_Await_Tagged : TemplateMiddleList_Yield_Await_Tagged TemplateMiddle Expression_In_Yield_Await')

#MemberExpression[Yield, Await]  : PrimaryExpression[?Yield, ?Await]
builder.r(w=1, d='MemberExpression : PrimaryExpression')

#MemberExpression[Yield, Await]  : PrimaryExpression[?Yield, ?Await]
builder.r(w=1, d='MemberExpression_Yield : PrimaryExpression_Yield')

#MemberExpression[Yield, Await]  : PrimaryExpression[?Yield, ?Await]
builder.r(w=1, d='MemberExpression_Await : PrimaryExpression_Await')

#MemberExpression[Yield, Await]  : PrimaryExpression[?Yield, ?Await]
builder.r(w=1, d='MemberExpression_Yield_Await : PrimaryExpression_Yield_Await')

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='MemberExpression : MemberExpression `[` Expression_In `]`')

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='MemberExpression_Yield : MemberExpression_Yield `[` Expression_In_Yield `]`')

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='MemberExpression_Await : MemberExpression_Await `[` Expression_In_Await `]`')

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='MemberExpression_Yield_Await : MemberExpression_Yield_Await `[` Expression_In_Yield_Await `]`')

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `.` IdentifierName
builder.r(w=1, d='MemberExpression : MemberExpression `.` IdentifierName')

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `.` IdentifierName
builder.r(w=1, d='MemberExpression_Yield : MemberExpression_Yield `.` IdentifierName')

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `.` IdentifierName
builder.r(w=1, d='MemberExpression_Await : MemberExpression_Await `.` IdentifierName')

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] `.` IdentifierName
builder.r(w=1, d='MemberExpression_Yield_Await : MemberExpression_Yield_Await `.` IdentifierName')

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
builder.r(w=1, d='MemberExpression : MemberExpression TemplateLiteral_Tagged')

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
builder.r(w=1, d='MemberExpression_Yield : MemberExpression_Yield TemplateLiteral_Yield_Tagged')

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
builder.r(w=1, d='MemberExpression_Await : MemberExpression_Await TemplateLiteral_Await_Tagged')

#MemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
builder.r(w=1, d='MemberExpression_Yield_Await : MemberExpression_Yield_Await TemplateLiteral_Yield_Await_Tagged')

#MemberExpression[Yield, Await]  : SuperProperty[?Yield, ?Await]
builder.r(w=1, d='MemberExpression : SuperProperty')

#MemberExpression[Yield, Await]  : SuperProperty[?Yield, ?Await]
builder.r(w=1, d='MemberExpression_Yield : SuperProperty_Yield')

#MemberExpression[Yield, Await]  : SuperProperty[?Yield, ?Await]
builder.r(w=1, d='MemberExpression_Await : SuperProperty_Await')

#MemberExpression[Yield, Await]  : SuperProperty[?Yield, ?Await]
builder.r(w=1, d='MemberExpression_Yield_Await : SuperProperty_Yield_Await')

#MemberExpression[Yield, Await]  : MetaProperty
builder.r(w=1, d='MemberExpression : MetaProperty')

#MemberExpression[Yield, Await]  : MetaProperty
builder.r(w=1, d='MemberExpression_Yield : MetaProperty')

#MemberExpression[Yield, Await]  : MetaProperty
builder.r(w=1, d='MemberExpression_Await : MetaProperty')

#MemberExpression[Yield, Await]  : MetaProperty
builder.r(w=1, d='MemberExpression_Yield_Await : MetaProperty')

#MemberExpression[Yield, Await]  : `new` MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='MemberExpression : `new` MemberExpression Arguments')

#MemberExpression[Yield, Await]  : `new` MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='MemberExpression_Yield : `new` MemberExpression_Yield Arguments_Yield')

#MemberExpression[Yield, Await]  : `new` MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='MemberExpression_Await : `new` MemberExpression_Await Arguments_Await')

#MemberExpression[Yield, Await]  : `new` MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='MemberExpression_Yield_Await : `new` MemberExpression_Yield_Await Arguments_Yield_Await')

#SuperProperty[Yield, Await]  : `super` `[` Expression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='SuperProperty : `super` `[` Expression_In `]`')

#SuperProperty[Yield, Await]  : `super` `[` Expression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='SuperProperty_Yield : `super` `[` Expression_In_Yield `]`')

#SuperProperty[Yield, Await]  : `super` `[` Expression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='SuperProperty_Await : `super` `[` Expression_In_Await `]`')

#SuperProperty[Yield, Await]  : `super` `[` Expression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='SuperProperty_Yield_Await : `super` `[` Expression_In_Yield_Await `]`')

#SuperProperty[Yield, Await]  : `super` `.` IdentifierName
builder.r(w=1, d='SuperProperty : `super` `.` IdentifierName')

#SuperProperty[Yield, Await]  : `super` `.` IdentifierName
builder.r(w=1, d='SuperProperty_Yield : `super` `.` IdentifierName')

#SuperProperty[Yield, Await]  : `super` `.` IdentifierName
builder.r(w=1, d='SuperProperty_Await : `super` `.` IdentifierName')

#SuperProperty[Yield, Await]  : `super` `.` IdentifierName
builder.r(w=1, d='SuperProperty_Yield_Await : `super` `.` IdentifierName')

#MetaProperty  : NewTarget
builder.r(w=1, d='MetaProperty : NewTarget')

#NewTarget  : `new` `.` `target`
builder.r(w=1, d='NewTarget : `new` `.` `target`')

#NewExpression[Yield, Await]  : MemberExpression[?Yield, ?Await]
builder.r(w=1, d='NewExpression : MemberExpression')

#NewExpression[Yield, Await]  : MemberExpression[?Yield, ?Await]
builder.r(w=1, d='NewExpression_Yield : MemberExpression_Yield')

#NewExpression[Yield, Await]  : MemberExpression[?Yield, ?Await]
builder.r(w=1, d='NewExpression_Await : MemberExpression_Await')

#NewExpression[Yield, Await]  : MemberExpression[?Yield, ?Await]
builder.r(w=1, d='NewExpression_Yield_Await : MemberExpression_Yield_Await')

#NewExpression[Yield, Await]  : `new` NewExpression[?Yield, ?Await]
builder.r(w=1, d='NewExpression : `new` NewExpression')

#NewExpression[Yield, Await]  : `new` NewExpression[?Yield, ?Await]
builder.r(w=1, d='NewExpression_Yield : `new` NewExpression_Yield')

#NewExpression[Yield, Await]  : `new` NewExpression[?Yield, ?Await]
builder.r(w=1, d='NewExpression_Await : `new` NewExpression_Await')

#NewExpression[Yield, Await]  : `new` NewExpression[?Yield, ?Await]
builder.r(w=1, d='NewExpression_Yield_Await : `new` NewExpression_Yield_Await')

#CallExpression[Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await] #callcover
builder.r(w=1, d='CallExpression : CoverCallExpressionAndAsyncArrowHead')

#CallExpression[Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await] #callcover
builder.r(w=1, d='CallExpression_Yield : CoverCallExpressionAndAsyncArrowHead_Yield')

#CallExpression[Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await] #callcover
builder.r(w=1, d='CallExpression_Await : CoverCallExpressionAndAsyncArrowHead_Await')

#CallExpression[Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await] #callcover
builder.r(w=1, d='CallExpression_Yield_Await : CoverCallExpressionAndAsyncArrowHead_Yield_Await')

#CallExpression[Yield, Await]  : SuperCall[?Yield, ?Await]
builder.r(w=1, d='CallExpression : SuperCall')

#CallExpression[Yield, Await]  : SuperCall[?Yield, ?Await]
builder.r(w=1, d='CallExpression_Yield : SuperCall_Yield')

#CallExpression[Yield, Await]  : SuperCall[?Yield, ?Await]
builder.r(w=1, d='CallExpression_Await : SuperCall_Await')

#CallExpression[Yield, Await]  : SuperCall[?Yield, ?Await]
builder.r(w=1, d='CallExpression_Yield_Await : SuperCall_Yield_Await')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='CallExpression : CallExpression Arguments')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='CallExpression_Yield : CallExpression_Yield Arguments_Yield')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='CallExpression_Await : CallExpression_Await Arguments_Await')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='CallExpression_Yield_Await : CallExpression_Yield_Await Arguments_Yield_Await')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='CallExpression : CallExpression `[` Expression_In `]`')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='CallExpression_Yield : CallExpression_Yield `[` Expression_In_Yield `]`')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='CallExpression_Await : CallExpression_Await `[` Expression_In_Await `]`')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `[` Expression[+In, ?Yield, ?Await] `]`
builder.r(w=1, d='CallExpression_Yield_Await : CallExpression_Yield_Await `[` Expression_In_Yield_Await `]`')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `.` IdentifierName
builder.r(w=1, d='CallExpression : CallExpression `.` IdentifierName')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `.` IdentifierName
builder.r(w=1, d='CallExpression_Yield : CallExpression_Yield `.` IdentifierName')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `.` IdentifierName
builder.r(w=1, d='CallExpression_Await : CallExpression_Await `.` IdentifierName')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] `.` IdentifierName
builder.r(w=1, d='CallExpression_Yield_Await : CallExpression_Yield_Await `.` IdentifierName')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
builder.r(w=1, d='CallExpression : CallExpression TemplateLiteral_Tagged')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
builder.r(w=1, d='CallExpression_Yield : CallExpression_Yield TemplateLiteral_Yield_Tagged')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
builder.r(w=1, d='CallExpression_Await : CallExpression_Await TemplateLiteral_Await_Tagged')

#CallExpression[Yield, Await]  : CallExpression[?Yield, ?Await] TemplateLiteral[?Yield, ?Await, +Tagged]
builder.r(w=1, d='CallExpression_Yield_Await : CallExpression_Yield_Await TemplateLiteral_Yield_Await_Tagged')

#SuperCall[Yield, Await]  : `super` Arguments[?Yield, ?Await]
builder.r(w=1, d='SuperCall : `super` Arguments')

#SuperCall[Yield, Await]  : `super` Arguments[?Yield, ?Await]
builder.r(w=1, d='SuperCall_Yield : `super` Arguments_Yield')

#SuperCall[Yield, Await]  : `super` Arguments[?Yield, ?Await]
builder.r(w=1, d='SuperCall_Await : `super` Arguments_Await')

#SuperCall[Yield, Await]  : `super` Arguments[?Yield, ?Await]
builder.r(w=1, d='SuperCall_Yield_Await : `super` Arguments_Yield_Await')

#Arguments[Yield, Await]  : `(` `)`
builder.r(w=1, d='Arguments : `(` `)`')

#Arguments[Yield, Await]  : `(` `)`
builder.r(w=1, d='Arguments_Yield : `(` `)`')

#Arguments[Yield, Await]  : `(` `)`
builder.r(w=1, d='Arguments_Await : `(` `)`')

#Arguments[Yield, Await]  : `(` `)`
builder.r(w=1, d='Arguments_Yield_Await : `(` `)`')

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `)`
builder.r(w=1, d='Arguments : `(` ArgumentList `)`')

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `)`
builder.r(w=1, d='Arguments_Yield : `(` ArgumentList_Yield `)`')

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `)`
builder.r(w=1, d='Arguments_Await : `(` ArgumentList_Await `)`')

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `)`
builder.r(w=1, d='Arguments_Yield_Await : `(` ArgumentList_Yield_Await `)`')

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `,` `)`
builder.r(w=1, d='Arguments : `(` ArgumentList `,` `)`')

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `,` `)`
builder.r(w=1, d='Arguments_Yield : `(` ArgumentList_Yield `,` `)`')

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `,` `)`
builder.r(w=1, d='Arguments_Await : `(` ArgumentList_Await `,` `)`')

#Arguments[Yield, Await]  : `(` ArgumentList[?Yield, ?Await] `,` `)`
builder.r(w=1, d='Arguments_Yield_Await : `(` ArgumentList_Yield_Await `,` `)`')

#ArgumentList[Yield, Await]  : AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList : AssignmentExpression_In')

#ArgumentList[Yield, Await]  : AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList_Yield : AssignmentExpression_In_Yield')

#ArgumentList[Yield, Await]  : AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList_Await : AssignmentExpression_In_Await')

#ArgumentList[Yield, Await]  : AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList_Yield_Await : AssignmentExpression_In_Yield_Await')

#ArgumentList[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList : `...` AssignmentExpression_In')

#ArgumentList[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList_Yield : `...` AssignmentExpression_In_Yield')

#ArgumentList[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList_Await : `...` AssignmentExpression_In_Await')

#ArgumentList[Yield, Await]  : `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList_Yield_Await : `...` AssignmentExpression_In_Yield_Await')

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList : ArgumentList `,` AssignmentExpression_In')

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList_Yield : ArgumentList_Yield `,` AssignmentExpression_In_Yield')

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList_Await : ArgumentList_Await `,` AssignmentExpression_In_Await')

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList_Yield_Await : ArgumentList_Yield_Await `,` AssignmentExpression_In_Yield_Await')

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList : ArgumentList `,` `...` AssignmentExpression_In')

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList_Yield : ArgumentList_Yield `,` `...` AssignmentExpression_In_Yield')

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList_Await : ArgumentList_Await `,` `...` AssignmentExpression_In_Await')

#ArgumentList[Yield, Await]  : ArgumentList[?Yield, ?Await] `,` `...` AssignmentExpression[+In, ?Yield, ?Await]
builder.r(w=1, d='ArgumentList_Yield_Await : ArgumentList_Yield_Await `,` `...` AssignmentExpression_In_Yield_Await')

#LeftHandSideExpression[Yield, Await]  : NewExpression[?Yield, ?Await]
builder.r(w=1, d='LeftHandSideExpression : NewExpression')

#LeftHandSideExpression[Yield, Await]  : NewExpression[?Yield, ?Await]
builder.r(w=1, d='LeftHandSideExpression_Yield : NewExpression_Yield')

#LeftHandSideExpression[Yield, Await]  : NewExpression[?Yield, ?Await]
builder.r(w=1, d='LeftHandSideExpression_Await : NewExpression_Await')

#LeftHandSideExpression[Yield, Await]  : NewExpression[?Yield, ?Await]
builder.r(w=1, d='LeftHandSideExpression_Yield_Await : NewExpression_Yield_Await')

#LeftHandSideExpression[Yield, Await]  : CallExpression[?Yield, ?Await]
builder.r(w=1, d='LeftHandSideExpression : CallExpression')

#LeftHandSideExpression[Yield, Await]  : CallExpression[?Yield, ?Await]
builder.r(w=1, d='LeftHandSideExpression_Yield : CallExpression_Yield')

#LeftHandSideExpression[Yield, Await]  : CallExpression[?Yield, ?Await]
builder.r(w=1, d='LeftHandSideExpression_Await : CallExpression_Await')

#LeftHandSideExpression[Yield, Await]  : CallExpression[?Yield, ?Await]
builder.r(w=1, d='LeftHandSideExpression_Yield_Await : CallExpression_Yield_Await')

#CallMemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='CallMemberExpression : MemberExpression Arguments')

#CallMemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='CallMemberExpression_Yield : MemberExpression_Yield Arguments_Yield')

#CallMemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='CallMemberExpression_Await : MemberExpression_Await Arguments_Await')

#CallMemberExpression[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='CallMemberExpression_Yield_Await : MemberExpression_Yield_Await Arguments_Yield_Await')

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
builder.r(w=1, d='UpdateExpression : LeftHandSideExpression')

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
builder.r(w=1, d='UpdateExpression_Yield : LeftHandSideExpression_Yield')

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
builder.r(w=1, d='UpdateExpression_Await : LeftHandSideExpression_Await')

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
builder.r(w=1, d='UpdateExpression_Yield_Await : LeftHandSideExpression_Yield_Await')

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `++`
builder.r(w=1, d='UpdateExpression : LeftHandSideExpression `++`')

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `++`
builder.r(w=1, d='UpdateExpression_Yield : LeftHandSideExpression_Yield `++`')

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `++`
builder.r(w=1, d='UpdateExpression_Await : LeftHandSideExpression_Await `++`')

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `++`
builder.r(w=1, d='UpdateExpression_Yield_Await : LeftHandSideExpression_Yield_Await `++`')

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `--`
builder.r(w=1, d='UpdateExpression : LeftHandSideExpression `--`')

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `--`
builder.r(w=1, d='UpdateExpression_Yield : LeftHandSideExpression_Yield `--`')

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `--`
builder.r(w=1, d='UpdateExpression_Await : LeftHandSideExpression_Await `--`')

#UpdateExpression[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]  `--`
builder.r(w=1, d='UpdateExpression_Yield_Await : LeftHandSideExpression_Yield_Await `--`')

#UpdateExpression[Yield, Await]  : `++` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UpdateExpression : `++` UnaryExpression')

#UpdateExpression[Yield, Await]  : `++` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UpdateExpression_Yield : `++` UnaryExpression_Yield')

#UpdateExpression[Yield, Await]  : `++` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UpdateExpression_Await : `++` UnaryExpression_Await')

#UpdateExpression[Yield, Await]  : `++` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UpdateExpression_Yield_Await : `++` UnaryExpression_Yield_Await')

#UpdateExpression[Yield, Await]  : `--` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UpdateExpression : `--` UnaryExpression')

#UpdateExpression[Yield, Await]  : `--` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UpdateExpression_Yield : `--` UnaryExpression_Yield')

#UpdateExpression[Yield, Await]  : `--` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UpdateExpression_Await : `--` UnaryExpression_Await')

#UpdateExpression[Yield, Await]  : `--` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UpdateExpression_Yield_Await : `--` UnaryExpression_Yield_Await')

#UnaryExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression : UpdateExpression')

#UnaryExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield : UpdateExpression_Yield')

#UnaryExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Await : UpdateExpression_Await')

#UnaryExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield_Await : UpdateExpression_Yield_Await')

#UnaryExpression[Yield, Await]  : `delete` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression : `delete` UnaryExpression')

#UnaryExpression[Yield, Await]  : `delete` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield : `delete` UnaryExpression_Yield')

#UnaryExpression[Yield, Await]  : `delete` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Await : `delete` UnaryExpression_Await')

#UnaryExpression[Yield, Await]  : `delete` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield_Await : `delete` UnaryExpression_Yield_Await')

#UnaryExpression[Yield, Await]  : `void` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression : `void` UnaryExpression')

#UnaryExpression[Yield, Await]  : `void` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield : `void` UnaryExpression_Yield')

#UnaryExpression[Yield, Await]  : `void` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Await : `void` UnaryExpression_Await')

#UnaryExpression[Yield, Await]  : `void` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield_Await : `void` UnaryExpression_Yield_Await')

#UnaryExpression[Yield, Await]  : `typeof` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression : `typeof` UnaryExpression')

#UnaryExpression[Yield, Await]  : `typeof` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield : `typeof` UnaryExpression_Yield')

#UnaryExpression[Yield, Await]  : `typeof` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Await : `typeof` UnaryExpression_Await')

#UnaryExpression[Yield, Await]  : `typeof` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield_Await : `typeof` UnaryExpression_Yield_Await')

#UnaryExpression[Yield, Await]  : `+` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression : `+` UnaryExpression')

#UnaryExpression[Yield, Await]  : `+` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield : `+` UnaryExpression_Yield')

#UnaryExpression[Yield, Await]  : `+` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Await : `+` UnaryExpression_Await')

#UnaryExpression[Yield, Await]  : `+` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield_Await : `+` UnaryExpression_Yield_Await')

#UnaryExpression[Yield, Await]  : `-` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression : `-` UnaryExpression')

#UnaryExpression[Yield, Await]  : `-` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield : `-` UnaryExpression_Yield')

#UnaryExpression[Yield, Await]  : `-` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Await : `-` UnaryExpression_Await')

#UnaryExpression[Yield, Await]  : `-` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield_Await : `-` UnaryExpression_Yield_Await')

#UnaryExpression[Yield, Await]  : `~` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression : `~` UnaryExpression')

#UnaryExpression[Yield, Await]  : `~` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield : `~` UnaryExpression_Yield')

#UnaryExpression[Yield, Await]  : `~` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Await : `~` UnaryExpression_Await')

#UnaryExpression[Yield, Await]  : `~` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield_Await : `~` UnaryExpression_Yield_Await')

#UnaryExpression[Yield, Await]  : `!` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression : `!` UnaryExpression')

#UnaryExpression[Yield, Await]  : `!` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield : `!` UnaryExpression_Yield')

#UnaryExpression[Yield, Await]  : `!` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Await : `!` UnaryExpression_Await')

#UnaryExpression[Yield, Await]  : `!` UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='UnaryExpression_Yield_Await : `!` UnaryExpression_Yield_Await')

#UnaryExpression[Yield, Await]  : [+Await] AwaitExpression[?Yield]
builder.r(w=1, d='UnaryExpression_Await : AwaitExpression')

#UnaryExpression[Yield, Await]  : [+Await] AwaitExpression[?Yield]
builder.r(w=1, d='UnaryExpression_Yield_Await : AwaitExpression_Yield')

#ExponentiationExpression[Yield, Await]  : UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='ExponentiationExpression : UnaryExpression')

#ExponentiationExpression[Yield, Await]  : UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='ExponentiationExpression_Yield : UnaryExpression_Yield')

#ExponentiationExpression[Yield, Await]  : UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='ExponentiationExpression_Await : UnaryExpression_Await')

#ExponentiationExpression[Yield, Await]  : UnaryExpression[?Yield, ?Await]
builder.r(w=1, d='ExponentiationExpression_Yield_Await : UnaryExpression_Yield_Await')

#ExponentiationExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await] `**` ExponentiationExpression[?Yield, ?Await]
builder.r(w=1, d='ExponentiationExpression : UpdateExpression `**` ExponentiationExpression')

#ExponentiationExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await] `**` ExponentiationExpression[?Yield, ?Await]
builder.r(w=1, d='ExponentiationExpression_Yield : UpdateExpression_Yield `**` ExponentiationExpression_Yield')

#ExponentiationExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await] `**` ExponentiationExpression[?Yield, ?Await]
builder.r(w=1, d='ExponentiationExpression_Await : UpdateExpression_Await `**` ExponentiationExpression_Await')

#ExponentiationExpression[Yield, Await]  : UpdateExpression[?Yield, ?Await] `**` ExponentiationExpression[?Yield, ?Await]
builder.r(w=1, d='ExponentiationExpression_Yield_Await : UpdateExpression_Yield_Await `**` ExponentiationExpression_Yield_Await')

#MultiplicativeExpression[Yield, Await]  : ExponentiationExpression[?Yield, ?Await]
builder.r(w=1, d='MultiplicativeExpression : ExponentiationExpression')

#MultiplicativeExpression[Yield, Await]  : ExponentiationExpression[?Yield, ?Await]
builder.r(w=1, d='MultiplicativeExpression_Yield : ExponentiationExpression_Yield')

#MultiplicativeExpression[Yield, Await]  : ExponentiationExpression[?Yield, ?Await]
builder.r(w=1, d='MultiplicativeExpression_Await : ExponentiationExpression_Await')

#MultiplicativeExpression[Yield, Await]  : ExponentiationExpression[?Yield, ?Await]
builder.r(w=1, d='MultiplicativeExpression_Yield_Await : ExponentiationExpression_Yield_Await')

#MultiplicativeExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await] MultiplicativeOperator ExponentiationExpression[?Yield, ?Await]
builder.r(w=1, d='MultiplicativeExpression : MultiplicativeExpression MultiplicativeOperator ExponentiationExpression')

#MultiplicativeExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await] MultiplicativeOperator ExponentiationExpression[?Yield, ?Await]
builder.r(w=1, d='MultiplicativeExpression_Yield : MultiplicativeExpression_Yield MultiplicativeOperator ExponentiationExpression_Yield')

#MultiplicativeExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await] MultiplicativeOperator ExponentiationExpression[?Yield, ?Await]
builder.r(w=1, d='MultiplicativeExpression_Await : MultiplicativeExpression_Await MultiplicativeOperator ExponentiationExpression_Await')

#MultiplicativeExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await] MultiplicativeOperator ExponentiationExpression[?Yield, ?Await]
builder.r(w=1, d='MultiplicativeExpression_Yield_Await : MultiplicativeExpression_Yield_Await MultiplicativeOperator ExponentiationExpression_Yield_Await')

#MultiplicativeOperator : one of `*` `/` `%`
builder.r(w=1, d='MultiplicativeOperator : `*`')

#MultiplicativeOperator : one of `*` `/` `%`
builder.r(w=1, d='MultiplicativeOperator : `/`')

#MultiplicativeOperator : one of `*` `/` `%`
builder.r(w=1, d='MultiplicativeOperator : `%`')

#AdditiveExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await]
builder.r(w=1, d='AdditiveExpression : MultiplicativeExpression')

#AdditiveExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await]
builder.r(w=1, d='AdditiveExpression_Yield : MultiplicativeExpression_Yield')

#AdditiveExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await]
builder.r(w=1, d='AdditiveExpression_Await : MultiplicativeExpression_Await')

#AdditiveExpression[Yield, Await]  : MultiplicativeExpression[?Yield, ?Await]
builder.r(w=1, d='AdditiveExpression_Yield_Await : MultiplicativeExpression_Yield_Await')

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `+` MultiplicativeExpression[?Yield, ?Await]
builder.r(w=1, d='AdditiveExpression : AdditiveExpression `+` MultiplicativeExpression')

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `+` MultiplicativeExpression[?Yield, ?Await]
builder.r(w=1, d='AdditiveExpression_Yield : AdditiveExpression_Yield `+` MultiplicativeExpression_Yield')

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `+` MultiplicativeExpression[?Yield, ?Await]
builder.r(w=1, d='AdditiveExpression_Await : AdditiveExpression_Await `+` MultiplicativeExpression_Await')

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `+` MultiplicativeExpression[?Yield, ?Await]
builder.r(w=1, d='AdditiveExpression_Yield_Await : AdditiveExpression_Yield_Await `+` MultiplicativeExpression_Yield_Await')

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `-` MultiplicativeExpression[?Yield, ?Await]
builder.r(w=1, d='AdditiveExpression : AdditiveExpression `-` MultiplicativeExpression')

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `-` MultiplicativeExpression[?Yield, ?Await]
builder.r(w=1, d='AdditiveExpression_Yield : AdditiveExpression_Yield `-` MultiplicativeExpression_Yield')

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `-` MultiplicativeExpression[?Yield, ?Await]
builder.r(w=1, d='AdditiveExpression_Await : AdditiveExpression_Await `-` MultiplicativeExpression_Await')

#AdditiveExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await] `-` MultiplicativeExpression[?Yield, ?Await]
builder.r(w=1, d='AdditiveExpression_Yield_Await : AdditiveExpression_Yield_Await `-` MultiplicativeExpression_Yield_Await')

#ShiftExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression : AdditiveExpression')

#ShiftExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression_Yield : AdditiveExpression_Yield')

#ShiftExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression_Await : AdditiveExpression_Await')

#ShiftExpression[Yield, Await]  : AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression_Yield_Await : AdditiveExpression_Yield_Await')

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `<<` AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression : ShiftExpression `<<` AdditiveExpression')

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `<<` AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression_Yield : ShiftExpression_Yield `<<` AdditiveExpression_Yield')

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `<<` AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression_Await : ShiftExpression_Await `<<` AdditiveExpression_Await')

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `<<` AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression_Yield_Await : ShiftExpression_Yield_Await `<<` AdditiveExpression_Yield_Await')

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>` AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression : ShiftExpression `>>` AdditiveExpression')

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>` AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression_Yield : ShiftExpression_Yield `>>` AdditiveExpression_Yield')

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>` AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression_Await : ShiftExpression_Await `>>` AdditiveExpression_Await')

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>` AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression_Yield_Await : ShiftExpression_Yield_Await `>>` AdditiveExpression_Yield_Await')

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>>` AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression : ShiftExpression `>>>` AdditiveExpression')

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>>` AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression_Yield : ShiftExpression_Yield `>>>` AdditiveExpression_Yield')

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>>` AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression_Await : ShiftExpression_Await `>>>` AdditiveExpression_Await')

#ShiftExpression[Yield, Await]  : ShiftExpression[?Yield, ?Await] `>>>` AdditiveExpression[?Yield, ?Await]
builder.r(w=1, d='ShiftExpression_Yield_Await : ShiftExpression_Yield_Await `>>>` AdditiveExpression_Yield_Await')

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression : ShiftExpression')

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In : ShiftExpression')

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Yield : ShiftExpression_Yield')

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Yield : ShiftExpression_Yield')

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Await : ShiftExpression_Await')

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Await : ShiftExpression_Await')

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Yield_Await : ShiftExpression_Yield_Await')

#RelationalExpression[In, Yield, Await]  : ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Yield_Await : ShiftExpression_Yield_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression : RelationalExpression `<` ShiftExpression')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In : RelationalExpression_In `<` ShiftExpression')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Yield : RelationalExpression_Yield `<` ShiftExpression_Yield')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Yield : RelationalExpression_In_Yield `<` ShiftExpression_Yield')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Await : RelationalExpression_Await `<` ShiftExpression_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Await : RelationalExpression_In_Await `<` ShiftExpression_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Yield_Await : RelationalExpression_Yield_Await `<` ShiftExpression_Yield_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Yield_Await : RelationalExpression_In_Yield_Await `<` ShiftExpression_Yield_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression : RelationalExpression `>` ShiftExpression')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In : RelationalExpression_In `>` ShiftExpression')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Yield : RelationalExpression_Yield `>` ShiftExpression_Yield')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Yield : RelationalExpression_In_Yield `>` ShiftExpression_Yield')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Await : RelationalExpression_Await `>` ShiftExpression_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Await : RelationalExpression_In_Await `>` ShiftExpression_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Yield_Await : RelationalExpression_Yield_Await `>` ShiftExpression_Yield_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Yield_Await : RelationalExpression_In_Yield_Await `>` ShiftExpression_Yield_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression : RelationalExpression `<=` ShiftExpression')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In : RelationalExpression_In `<=` ShiftExpression')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Yield : RelationalExpression_Yield `<=` ShiftExpression_Yield')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Yield : RelationalExpression_In_Yield `<=` ShiftExpression_Yield')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Await : RelationalExpression_Await `<=` ShiftExpression_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Await : RelationalExpression_In_Await `<=` ShiftExpression_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Yield_Await : RelationalExpression_Yield_Await `<=` ShiftExpression_Yield_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `<=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Yield_Await : RelationalExpression_In_Yield_Await `<=` ShiftExpression_Yield_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression : RelationalExpression `>=` ShiftExpression')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In : RelationalExpression_In `>=` ShiftExpression')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Yield : RelationalExpression_Yield `>=` ShiftExpression_Yield')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Yield : RelationalExpression_In_Yield `>=` ShiftExpression_Yield')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Await : RelationalExpression_Await `>=` ShiftExpression_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Await : RelationalExpression_In_Await `>=` ShiftExpression_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Yield_Await : RelationalExpression_Yield_Await `>=` ShiftExpression_Yield_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `>=` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Yield_Await : RelationalExpression_In_Yield_Await `>=` ShiftExpression_Yield_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression : RelationalExpression `instanceof` ShiftExpression')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In : RelationalExpression_In `instanceof` ShiftExpression')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Yield : RelationalExpression_Yield `instanceof` ShiftExpression_Yield')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Yield : RelationalExpression_In_Yield `instanceof` ShiftExpression_Yield')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Await : RelationalExpression_Await `instanceof` ShiftExpression_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Await : RelationalExpression_In_Await `instanceof` ShiftExpression_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_Yield_Await : RelationalExpression_Yield_Await `instanceof` ShiftExpression_Yield_Await')

#RelationalExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await] `instanceof` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Yield_Await : RelationalExpression_In_Yield_Await `instanceof` ShiftExpression_Yield_Await')

#RelationalExpression[In, Yield, Await]  : [+In] RelationalExpression[+In, ?Yield, ?Await] `in` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In : RelationalExpression_In `in` ShiftExpression')

#RelationalExpression[In, Yield, Await]  : [+In] RelationalExpression[+In, ?Yield, ?Await] `in` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Yield : RelationalExpression_In_Yield `in` ShiftExpression_Yield')

#RelationalExpression[In, Yield, Await]  : [+In] RelationalExpression[+In, ?Yield, ?Await] `in` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Await : RelationalExpression_In_Await `in` ShiftExpression_Await')

#RelationalExpression[In, Yield, Await]  : [+In] RelationalExpression[+In, ?Yield, ?Await] `in` ShiftExpression[?Yield, ?Await]
builder.r(w=1, d='RelationalExpression_In_Yield_Await : RelationalExpression_In_Yield_Await `in` ShiftExpression_Yield_Await')

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression : RelationalExpression')

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In : RelationalExpression_In')

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Yield : RelationalExpression_Yield')

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Yield : RelationalExpression_In_Yield')

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Await : RelationalExpression_Await')

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Await : RelationalExpression_In_Await')

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Yield_Await : RelationalExpression_Yield_Await')

#EqualityExpression[In, Yield, Await]  : RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Yield_Await : RelationalExpression_In_Yield_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression : EqualityExpression `==` RelationalExpression')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In : EqualityExpression_In `==` RelationalExpression_In')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Yield : EqualityExpression_Yield `==` RelationalExpression_Yield')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Yield : EqualityExpression_In_Yield `==` RelationalExpression_In_Yield')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Await : EqualityExpression_Await `==` RelationalExpression_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Await : EqualityExpression_In_Await `==` RelationalExpression_In_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Yield_Await : EqualityExpression_Yield_Await `==` RelationalExpression_Yield_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Yield_Await : EqualityExpression_In_Yield_Await `==` RelationalExpression_In_Yield_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression : EqualityExpression `!=` RelationalExpression')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In : EqualityExpression_In `!=` RelationalExpression_In')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Yield : EqualityExpression_Yield `!=` RelationalExpression_Yield')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Yield : EqualityExpression_In_Yield `!=` RelationalExpression_In_Yield')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Await : EqualityExpression_Await `!=` RelationalExpression_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Await : EqualityExpression_In_Await `!=` RelationalExpression_In_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Yield_Await : EqualityExpression_Yield_Await `!=` RelationalExpression_Yield_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!=` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Yield_Await : EqualityExpression_In_Yield_Await `!=` RelationalExpression_In_Yield_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression : EqualityExpression `===` RelationalExpression')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In : EqualityExpression_In `===` RelationalExpression_In')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Yield : EqualityExpression_Yield `===` RelationalExpression_Yield')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Yield : EqualityExpression_In_Yield `===` RelationalExpression_In_Yield')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Await : EqualityExpression_Await `===` RelationalExpression_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Await : EqualityExpression_In_Await `===` RelationalExpression_In_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Yield_Await : EqualityExpression_Yield_Await `===` RelationalExpression_Yield_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `===` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Yield_Await : EqualityExpression_In_Yield_Await `===` RelationalExpression_In_Yield_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression : EqualityExpression `!==` RelationalExpression')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In : EqualityExpression_In `!==` RelationalExpression_In')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Yield : EqualityExpression_Yield `!==` RelationalExpression_Yield')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Yield : EqualityExpression_In_Yield `!==` RelationalExpression_In_Yield')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Await : EqualityExpression_Await `!==` RelationalExpression_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Await : EqualityExpression_In_Await `!==` RelationalExpression_In_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_Yield_Await : EqualityExpression_Yield_Await `!==` RelationalExpression_Yield_Await')

#EqualityExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await] `!==` RelationalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='EqualityExpression_In_Yield_Await : EqualityExpression_In_Yield_Await `!==` RelationalExpression_In_Yield_Await')

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression : EqualityExpression')

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression_In : EqualityExpression_In')

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression_Yield : EqualityExpression_Yield')

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression_In_Yield : EqualityExpression_In_Yield')

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression_Await : EqualityExpression_Await')

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression_In_Await : EqualityExpression_In_Await')

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression_Yield_Await : EqualityExpression_Yield_Await')

#BitwiseANDExpression[In, Yield, Await]  : EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression_In_Yield_Await : EqualityExpression_In_Yield_Await')

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression : BitwiseANDExpression `&` EqualityExpression')

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression_In : BitwiseANDExpression_In `&` EqualityExpression_In')

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression_Yield : BitwiseANDExpression_Yield `&` EqualityExpression_Yield')

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression_In_Yield : BitwiseANDExpression_In_Yield `&` EqualityExpression_In_Yield')

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression_Await : BitwiseANDExpression_Await `&` EqualityExpression_Await')

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression_In_Await : BitwiseANDExpression_In_Await `&` EqualityExpression_In_Await')

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression_Yield_Await : BitwiseANDExpression_Yield_Await `&` EqualityExpression_Yield_Await')

#BitwiseANDExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await] `&` EqualityExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseANDExpression_In_Yield_Await : BitwiseANDExpression_In_Yield_Await `&` EqualityExpression_In_Yield_Await')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression : BitwiseANDExpression')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression_In : BitwiseANDExpression_In')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression_Yield : BitwiseANDExpression_Yield')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression_In_Yield : BitwiseANDExpression_In_Yield')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression_Await : BitwiseANDExpression_Await')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression_In_Await : BitwiseANDExpression_In_Await')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression_Yield_Await : BitwiseANDExpression_Yield_Await')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression_In_Yield_Await : BitwiseANDExpression_In_Yield_Await')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression : BitwiseXORExpression `^` BitwiseANDExpression')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression_In : BitwiseXORExpression_In `^` BitwiseANDExpression_In')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression_Yield : BitwiseXORExpression_Yield `^` BitwiseANDExpression_Yield')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression_In_Yield : BitwiseXORExpression_In_Yield `^` BitwiseANDExpression_In_Yield')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression_Await : BitwiseXORExpression_Await `^` BitwiseANDExpression_Await')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression_In_Await : BitwiseXORExpression_In_Await `^` BitwiseANDExpression_In_Await')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression_Yield_Await : BitwiseXORExpression_Yield_Await `^` BitwiseANDExpression_Yield_Await')

#BitwiseXORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await] `^` BitwiseANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseXORExpression_In_Yield_Await : BitwiseXORExpression_In_Yield_Await `^` BitwiseANDExpression_In_Yield_Await')

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression : BitwiseXORExpression')

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression_In : BitwiseXORExpression_In')

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression_Yield : BitwiseXORExpression_Yield')

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression_In_Yield : BitwiseXORExpression_In_Yield')

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression_Await : BitwiseXORExpression_Await')

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression_In_Await : BitwiseXORExpression_In_Await')

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression_Yield_Await : BitwiseXORExpression_Yield_Await')

#BitwiseORExpression[In, Yield, Await]  : BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression_In_Yield_Await : BitwiseXORExpression_In_Yield_Await')

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression : BitwiseORExpression `|` BitwiseXORExpression')

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression_In : BitwiseORExpression_In `|` BitwiseXORExpression_In')

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression_Yield : BitwiseORExpression_Yield `|` BitwiseXORExpression_Yield')

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression_In_Yield : BitwiseORExpression_In_Yield `|` BitwiseXORExpression_In_Yield')

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression_Await : BitwiseORExpression_Await `|` BitwiseXORExpression_Await')

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression_In_Await : BitwiseORExpression_In_Await `|` BitwiseXORExpression_In_Await')

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression_Yield_Await : BitwiseORExpression_Yield_Await `|` BitwiseXORExpression_Yield_Await')

#BitwiseORExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await] `|` BitwiseXORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='BitwiseORExpression_In_Yield_Await : BitwiseORExpression_In_Yield_Await `|` BitwiseXORExpression_In_Yield_Await')

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression : BitwiseORExpression')

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression_In : BitwiseORExpression_In')

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression_Yield : BitwiseORExpression_Yield')

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression_In_Yield : BitwiseORExpression_In_Yield')

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression_Await : BitwiseORExpression_Await')

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression_In_Await : BitwiseORExpression_In_Await')

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression_Yield_Await : BitwiseORExpression_Yield_Await')

#LogicalANDExpression[In, Yield, Await]  : BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression_In_Yield_Await : BitwiseORExpression_In_Yield_Await')

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression : LogicalANDExpression `&&` BitwiseORExpression')

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression_In : LogicalANDExpression_In `&&` BitwiseORExpression_In')

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression_Yield : LogicalANDExpression_Yield `&&` BitwiseORExpression_Yield')

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression_In_Yield : LogicalANDExpression_In_Yield `&&` BitwiseORExpression_In_Yield')

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression_Await : LogicalANDExpression_Await `&&` BitwiseORExpression_Await')

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression_In_Await : LogicalANDExpression_In_Await `&&` BitwiseORExpression_In_Await')

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression_Yield_Await : LogicalANDExpression_Yield_Await `&&` BitwiseORExpression_Yield_Await')

#LogicalANDExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await] `&&` BitwiseORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalANDExpression_In_Yield_Await : LogicalANDExpression_In_Yield_Await `&&` BitwiseORExpression_In_Yield_Await')

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression : LogicalANDExpression')

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression_In : LogicalANDExpression_In')

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression_Yield : LogicalANDExpression_Yield')

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression_In_Yield : LogicalANDExpression_In_Yield')

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression_Await : LogicalANDExpression_Await')

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression_In_Await : LogicalANDExpression_In_Await')

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression_Yield_Await : LogicalANDExpression_Yield_Await')

#LogicalORExpression[In, Yield, Await]  : LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression_In_Yield_Await : LogicalANDExpression_In_Yield_Await')

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression : LogicalORExpression `||` LogicalANDExpression')

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression_In : LogicalORExpression_In `||` LogicalANDExpression_In')

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression_Yield : LogicalORExpression_Yield `||` LogicalANDExpression_Yield')

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression_In_Yield : LogicalORExpression_In_Yield `||` LogicalANDExpression_In_Yield')

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression_Await : LogicalORExpression_Await `||` LogicalANDExpression_Await')

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression_In_Await : LogicalORExpression_In_Await `||` LogicalANDExpression_In_Await')

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression_Yield_Await : LogicalORExpression_Yield_Await `||` LogicalANDExpression_Yield_Await')

#LogicalORExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `||` LogicalANDExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='LogicalORExpression_In_Yield_Await : LogicalORExpression_In_Yield_Await `||` LogicalANDExpression_In_Yield_Await')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression : LogicalORExpression')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression_In : LogicalORExpression_In')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression_Yield : LogicalORExpression_Yield')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression_In_Yield : LogicalORExpression_In_Yield')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression_Await : LogicalORExpression_Await')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression_In_Await : LogicalORExpression_In_Await')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression_Yield_Await : LogicalORExpression_Yield_Await')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression_In_Yield_Await : LogicalORExpression_In_Yield_Await')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression : LogicalORExpression `?` AssignmentExpression_In `:` AssignmentExpression')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression_In : LogicalORExpression_In `?` AssignmentExpression_In `:` AssignmentExpression_In')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression_Yield : LogicalORExpression_Yield `?` AssignmentExpression_In_Yield `:` AssignmentExpression_Yield')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression_In_Yield : LogicalORExpression_In_Yield `?` AssignmentExpression_In_Yield `:` AssignmentExpression_In_Yield')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression_Await : LogicalORExpression_Await `?` AssignmentExpression_In_Await `:` AssignmentExpression_Await')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression_In_Await : LogicalORExpression_In_Await `?` AssignmentExpression_In_Await `:` AssignmentExpression_In_Await')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression_Yield_Await : LogicalORExpression_Yield_Await `?` AssignmentExpression_In_Yield_Await `:` AssignmentExpression_Yield_Await')

#ConditionalExpression[In, Yield, Await]  : LogicalORExpression[?In, ?Yield, ?Await] `?` AssignmentExpression[+In, ?Yield, ?Await] `:` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='ConditionalExpression_In_Yield_Await : LogicalORExpression_In_Yield_Await `?` AssignmentExpression_In_Yield_Await `:` AssignmentExpression_In_Yield_Await')

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression : ConditionalExpression')

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In : ConditionalExpression_In')

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_Yield : ConditionalExpression_Yield')

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In_Yield : ConditionalExpression_In_Yield')

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_Await : ConditionalExpression_Await')

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In_Await : ConditionalExpression_In_Await')

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_Yield_Await : ConditionalExpression_Yield_Await')

#AssignmentExpression[In, Yield, Await]  : ConditionalExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In_Yield_Await : ConditionalExpression_In_Yield_Await')

#AssignmentExpression[In, Yield, Await]  : [+Yield] YieldExpression[?In, ?Await]
builder.r(w=1, d='AssignmentExpression_Yield : YieldExpression')

#AssignmentExpression[In, Yield, Await]  : [+Yield] YieldExpression[?In, ?Await]
builder.r(w=1, d='AssignmentExpression_In_Yield : YieldExpression_In')

#AssignmentExpression[In, Yield, Await]  : [+Yield] YieldExpression[?In, ?Await]
builder.r(w=1, d='AssignmentExpression_Yield_Await : YieldExpression_Await')

#AssignmentExpression[In, Yield, Await]  : [+Yield] YieldExpression[?In, ?Await]
builder.r(w=1, d='AssignmentExpression_In_Yield_Await : YieldExpression_In_Await')

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression : ArrowFunction')

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In : ArrowFunction_In')

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_Yield : ArrowFunction_Yield')

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In_Yield : ArrowFunction_In_Yield')

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_Await : ArrowFunction_Await')

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In_Await : ArrowFunction_In_Await')

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_Yield_Await : ArrowFunction_Yield_Await')

#AssignmentExpression[In, Yield, Await]  : ArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In_Yield_Await : ArrowFunction_In_Yield_Await')

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression : AsyncArrowFunction')

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In : AsyncArrowFunction_In')

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_Yield : AsyncArrowFunction_Yield')

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In_Yield : AsyncArrowFunction_In_Yield')

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_Await : AsyncArrowFunction_Await')

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In_Await : AsyncArrowFunction_In_Await')

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_Yield_Await : AsyncArrowFunction_Yield_Await')

#AssignmentExpression[In, Yield, Await]  : AsyncArrowFunction[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In_Yield_Await : AsyncArrowFunction_In_Yield_Await')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
builder.r(w=1, d='AssignmentExpression : LeftHandSideExpression `=` AssignmentExpression')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
builder.r(w=1, d='AssignmentExpression_In : LeftHandSideExpression `=` AssignmentExpression_In')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
builder.r(w=1, d='AssignmentExpression_Yield : LeftHandSideExpression_Yield `=` AssignmentExpression_Yield')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
builder.r(w=1, d='AssignmentExpression_In_Yield : LeftHandSideExpression_Yield `=` AssignmentExpression_In_Yield')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
builder.r(w=1, d='AssignmentExpression_Await : LeftHandSideExpression_Await `=` AssignmentExpression_Await')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
builder.r(w=1, d='AssignmentExpression_In_Await : LeftHandSideExpression_Await `=` AssignmentExpression_In_Await')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
builder.r(w=1, d='AssignmentExpression_Yield_Await : LeftHandSideExpression_Yield_Await `=` AssignmentExpression_Yield_Await')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] `=` AssignmentExpression[?In, ?Yield, ?Await] #assignment
builder.r(w=1, d='AssignmentExpression_In_Yield_Await : LeftHandSideExpression_Yield_Await `=` AssignmentExpression_In_Yield_Await')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression : LeftHandSideExpression AssignmentOperator AssignmentExpression')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In : LeftHandSideExpression AssignmentOperator AssignmentExpression_In')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_Yield : LeftHandSideExpression_Yield AssignmentOperator AssignmentExpression_Yield')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In_Yield : LeftHandSideExpression_Yield AssignmentOperator AssignmentExpression_In_Yield')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_Await : LeftHandSideExpression_Await AssignmentOperator AssignmentExpression_Await')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In_Await : LeftHandSideExpression_Await AssignmentOperator AssignmentExpression_In_Await')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_Yield_Await : LeftHandSideExpression_Yield_Await AssignmentOperator AssignmentExpression_Yield_Await')

#AssignmentExpression[In, Yield, Await]  : LeftHandSideExpression[?Yield, ?Await] AssignmentOperator AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='AssignmentExpression_In_Yield_Await : LeftHandSideExpression_Yield_Await AssignmentOperator AssignmentExpression_In_Yield_Await')

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
builder.r(w=1, d='AssignmentOperator : `*=`')

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
builder.r(w=1, d='AssignmentOperator : `/=`')

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
builder.r(w=1, d='AssignmentOperator : `%=`')

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
builder.r(w=1, d='AssignmentOperator : `+=`')

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
builder.r(w=1, d='AssignmentOperator : `-=`')

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
builder.r(w=1, d='AssignmentOperator : `<<=`')

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
builder.r(w=1, d='AssignmentOperator : `>>=`')

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
builder.r(w=1, d='AssignmentOperator : `>>>=`')

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
builder.r(w=1, d='AssignmentOperator : `&=`')

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
builder.r(w=1, d='AssignmentOperator : `^=`')

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
builder.r(w=1, d='AssignmentOperator : `|=`')

#AssignmentOperator : one of `*=` `/=` `%=` `+=` `-=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `**=`
builder.r(w=1, d='AssignmentOperator : `**=`')

#AssignmentPattern[Yield, Await]  : ObjectAssignmentPattern[?Yield, ?Await]
builder.r(w=1, d='AssignmentPattern : ObjectAssignmentPattern')

#AssignmentPattern[Yield, Await]  : ObjectAssignmentPattern[?Yield, ?Await]
builder.r(w=1, d='AssignmentPattern_Yield : ObjectAssignmentPattern_Yield')

#AssignmentPattern[Yield, Await]  : ObjectAssignmentPattern[?Yield, ?Await]
builder.r(w=1, d='AssignmentPattern_Await : ObjectAssignmentPattern_Await')

#AssignmentPattern[Yield, Await]  : ObjectAssignmentPattern[?Yield, ?Await]
builder.r(w=1, d='AssignmentPattern_Yield_Await : ObjectAssignmentPattern_Yield_Await')

#AssignmentPattern[Yield, Await]  : ArrayAssignmentPattern[?Yield, ?Await]
builder.r(w=1, d='AssignmentPattern : ArrayAssignmentPattern')

#AssignmentPattern[Yield, Await]  : ArrayAssignmentPattern[?Yield, ?Await]
builder.r(w=1, d='AssignmentPattern_Yield : ArrayAssignmentPattern_Yield')

#AssignmentPattern[Yield, Await]  : ArrayAssignmentPattern[?Yield, ?Await]
builder.r(w=1, d='AssignmentPattern_Await : ArrayAssignmentPattern_Await')

#AssignmentPattern[Yield, Await]  : ArrayAssignmentPattern[?Yield, ?Await]
builder.r(w=1, d='AssignmentPattern_Yield_Await : ArrayAssignmentPattern_Yield_Await')

#ObjectAssignmentPattern[Yield, Await]  : `{` `}`
builder.r(w=1, d='ObjectAssignmentPattern : `{` `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` `}`
builder.r(w=1, d='ObjectAssignmentPattern_Yield : `{` `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` `}`
builder.r(w=1, d='ObjectAssignmentPattern_Await : `{` `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` `}`
builder.r(w=1, d='ObjectAssignmentPattern_Yield_Await : `{` `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentRestProperty[?Yield, ?Await] `}`
builder.r(w=1, d='ObjectAssignmentPattern : `{` AssignmentRestProperty `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentRestProperty[?Yield, ?Await] `}`
builder.r(w=1, d='ObjectAssignmentPattern_Yield : `{` AssignmentRestProperty_Yield `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentRestProperty[?Yield, ?Await] `}`
builder.r(w=1, d='ObjectAssignmentPattern_Await : `{` AssignmentRestProperty_Await `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentRestProperty[?Yield, ?Await] `}`
builder.r(w=1, d='ObjectAssignmentPattern_Yield_Await : `{` AssignmentRestProperty_Yield_Await `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `}`
builder.r(w=1, d='ObjectAssignmentPattern : `{` AssignmentPropertyList `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `}`
builder.r(w=1, d='ObjectAssignmentPattern_Yield : `{` AssignmentPropertyList_Yield `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `}`
builder.r(w=1, d='ObjectAssignmentPattern_Await : `{` AssignmentPropertyList_Await `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `}`
builder.r(w=1, d='ObjectAssignmentPattern_Yield_Await : `{` AssignmentPropertyList_Yield_Await `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
builder.r(w=1, d='ObjectAssignmentPattern : `{` AssignmentPropertyList `,` `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
builder.r(w=1, d='ObjectAssignmentPattern : `{` AssignmentPropertyList `,` AssignmentRestProperty `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
builder.r(w=1, d='ObjectAssignmentPattern_Yield : `{` AssignmentPropertyList_Yield `,` `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
builder.r(w=1, d='ObjectAssignmentPattern_Yield : `{` AssignmentPropertyList_Yield `,` AssignmentRestProperty_Yield `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
builder.r(w=1, d='ObjectAssignmentPattern_Await : `{` AssignmentPropertyList_Await `,` `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
builder.r(w=1, d='ObjectAssignmentPattern_Await : `{` AssignmentPropertyList_Await `,` AssignmentRestProperty_Await `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
builder.r(w=1, d='ObjectAssignmentPattern_Yield_Await : `{` AssignmentPropertyList_Yield_Await `,` `}`')

#ObjectAssignmentPattern[Yield, Await]  : `{` AssignmentPropertyList[?Yield, ?Await] `,` AssignmentRestProperty[?Yield, ?Await]? `}`
builder.r(w=1, d='ObjectAssignmentPattern_Yield_Await : `{` AssignmentPropertyList_Yield_Await `,` AssignmentRestProperty_Yield_Await `}`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern : `[` `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern : `[` AssignmentRestElement `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern : `[` Elision `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern : `[` Elision AssignmentRestElement `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield : `[` `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield : `[` AssignmentRestElement_Yield `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield : `[` Elision `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield : `[` Elision AssignmentRestElement_Yield `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Await : `[` `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Await : `[` AssignmentRestElement_Await `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Await : `[` Elision `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Await : `[` Elision AssignmentRestElement_Await `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield_Await : `[` `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield_Await : `[` AssignmentRestElement_Yield_Await `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield_Await : `[` Elision `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield_Await : `[` Elision AssignmentRestElement_Yield_Await `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `]`
builder.r(w=1, d='ArrayAssignmentPattern : `[` AssignmentElementList `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield : `[` AssignmentElementList_Yield `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `]`
builder.r(w=1, d='ArrayAssignmentPattern_Await : `[` AssignmentElementList_Await `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield_Await : `[` AssignmentElementList_Yield_Await `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern : `[` AssignmentElementList `,` `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern : `[` AssignmentElementList `,` AssignmentRestElement `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern : `[` AssignmentElementList `,` Elision `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern : `[` AssignmentElementList `,` Elision AssignmentRestElement `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield : `[` AssignmentElementList_Yield `,` `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield : `[` AssignmentElementList_Yield `,` AssignmentRestElement_Yield `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield : `[` AssignmentElementList_Yield `,` Elision `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield : `[` AssignmentElementList_Yield `,` Elision AssignmentRestElement_Yield `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Await : `[` AssignmentElementList_Await `,` `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Await : `[` AssignmentElementList_Await `,` AssignmentRestElement_Await `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Await : `[` AssignmentElementList_Await `,` Elision `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Await : `[` AssignmentElementList_Await `,` Elision AssignmentRestElement_Await `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield_Await : `[` AssignmentElementList_Yield_Await `,` `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield_Await : `[` AssignmentElementList_Yield_Await `,` AssignmentRestElement_Yield_Await `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield_Await : `[` AssignmentElementList_Yield_Await `,` Elision `]`')

#ArrayAssignmentPattern[Yield, Await]  : `[` AssignmentElementList[?Yield, ?Await] `,` Elision? AssignmentRestElement[?Yield, ?Await]? `]`
builder.r(w=1, d='ArrayAssignmentPattern_Yield_Await : `[` AssignmentElementList_Yield_Await `,` Elision AssignmentRestElement_Yield_Await `]`')

#AssignmentRestProperty[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
builder.r(w=1, d='AssignmentRestProperty : `...` DestructuringAssignmentTarget')

#AssignmentRestProperty[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
builder.r(w=1, d='AssignmentRestProperty_Yield : `...` DestructuringAssignmentTarget_Yield')

#AssignmentRestProperty[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
builder.r(w=1, d='AssignmentRestProperty_Await : `...` DestructuringAssignmentTarget_Await')

#AssignmentRestProperty[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
builder.r(w=1, d='AssignmentRestProperty_Yield_Await : `...` DestructuringAssignmentTarget_Yield_Await')

#AssignmentPropertyList[Yield, Await]  : AssignmentProperty[?Yield, ?Await]
builder.r(w=1, d='AssignmentPropertyList : AssignmentProperty')

#AssignmentPropertyList[Yield, Await]  : AssignmentProperty[?Yield, ?Await]
builder.r(w=1, d='AssignmentPropertyList_Yield : AssignmentProperty_Yield')

#AssignmentPropertyList[Yield, Await]  : AssignmentProperty[?Yield, ?Await]
builder.r(w=1, d='AssignmentPropertyList_Await : AssignmentProperty_Await')

#AssignmentPropertyList[Yield, Await]  : AssignmentProperty[?Yield, ?Await]
builder.r(w=1, d='AssignmentPropertyList_Yield_Await : AssignmentProperty_Yield_Await')

#AssignmentPropertyList[Yield, Await]  : AssignmentPropertyList[?Yield, ?Await] `,` AssignmentProperty[?Yield, ?Await]
builder.r(w=1, d='AssignmentPropertyList : AssignmentPropertyList `,` AssignmentProperty')

#AssignmentPropertyList[Yield, Await]  : AssignmentPropertyList[?Yield, ?Await] `,` AssignmentProperty[?Yield, ?Await]
builder.r(w=1, d='AssignmentPropertyList_Yield : AssignmentPropertyList_Yield `,` AssignmentProperty_Yield')

#AssignmentPropertyList[Yield, Await]  : AssignmentPropertyList[?Yield, ?Await] `,` AssignmentProperty[?Yield, ?Await]
builder.r(w=1, d='AssignmentPropertyList_Await : AssignmentPropertyList_Await `,` AssignmentProperty_Await')

#AssignmentPropertyList[Yield, Await]  : AssignmentPropertyList[?Yield, ?Await] `,` AssignmentProperty[?Yield, ?Await]
builder.r(w=1, d='AssignmentPropertyList_Yield_Await : AssignmentPropertyList_Yield_Await `,` AssignmentProperty_Yield_Await')

#AssignmentElementList[Yield, Await]  : AssignmentElisionElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElementList : AssignmentElisionElement')

#AssignmentElementList[Yield, Await]  : AssignmentElisionElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElementList_Yield : AssignmentElisionElement_Yield')

#AssignmentElementList[Yield, Await]  : AssignmentElisionElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElementList_Await : AssignmentElisionElement_Await')

#AssignmentElementList[Yield, Await]  : AssignmentElisionElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElementList_Yield_Await : AssignmentElisionElement_Yield_Await')

#AssignmentElementList[Yield, Await]  : AssignmentElementList[?Yield, ?Await] `,` AssignmentElisionElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElementList : AssignmentElementList `,` AssignmentElisionElement')

#AssignmentElementList[Yield, Await]  : AssignmentElementList[?Yield, ?Await] `,` AssignmentElisionElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElementList_Yield : AssignmentElementList_Yield `,` AssignmentElisionElement_Yield')

#AssignmentElementList[Yield, Await]  : AssignmentElementList[?Yield, ?Await] `,` AssignmentElisionElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElementList_Await : AssignmentElementList_Await `,` AssignmentElisionElement_Await')

#AssignmentElementList[Yield, Await]  : AssignmentElementList[?Yield, ?Await] `,` AssignmentElisionElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElementList_Yield_Await : AssignmentElementList_Yield_Await `,` AssignmentElisionElement_Yield_Await')

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElisionElement : AssignmentElement')

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElisionElement : Elision AssignmentElement')

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElisionElement_Yield : AssignmentElement_Yield')

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElisionElement_Yield : Elision AssignmentElement_Yield')

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElisionElement_Await : AssignmentElement_Await')

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElisionElement_Await : Elision AssignmentElement_Await')

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElisionElement_Yield_Await : AssignmentElement_Yield_Await')

#AssignmentElisionElement[Yield, Await]  : Elision? AssignmentElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentElisionElement_Yield_Await : Elision AssignmentElement_Yield_Await')

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentProperty : IdentifierReference')

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentProperty : IdentifierReference Initializer_In')

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentProperty_Yield : IdentifierReference_Yield')

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentProperty_Yield : IdentifierReference_Yield Initializer_In_Yield')

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentProperty_Await : IdentifierReference_Await')

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentProperty_Await : IdentifierReference_Await Initializer_In_Await')

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentProperty_Yield_Await : IdentifierReference_Yield_Await')

#AssignmentProperty[Yield, Await]  : IdentifierReference[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentProperty_Yield_Await : IdentifierReference_Yield_Await Initializer_In_Yield_Await')

#AssignmentProperty[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentProperty : PropertyName `:` AssignmentElement')

#AssignmentProperty[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentProperty_Yield : PropertyName_Yield `:` AssignmentElement_Yield')

#AssignmentProperty[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentProperty_Await : PropertyName_Await `:` AssignmentElement_Await')

#AssignmentProperty[Yield, Await]  : PropertyName[?Yield, ?Await] `:` AssignmentElement[?Yield, ?Await]
builder.r(w=1, d='AssignmentProperty_Yield_Await : PropertyName_Yield_Await `:` AssignmentElement_Yield_Await')

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentElement : DestructuringAssignmentTarget')

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentElement : DestructuringAssignmentTarget Initializer_In')

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentElement_Yield : DestructuringAssignmentTarget_Yield')

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentElement_Yield : DestructuringAssignmentTarget_Yield Initializer_In_Yield')

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentElement_Await : DestructuringAssignmentTarget_Await')

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentElement_Await : DestructuringAssignmentTarget_Await Initializer_In_Await')

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentElement_Yield_Await : DestructuringAssignmentTarget_Yield_Await')

#AssignmentElement[Yield, Await]  : DestructuringAssignmentTarget[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
builder.r(w=1, d='AssignmentElement_Yield_Await : DestructuringAssignmentTarget_Yield_Await Initializer_In_Yield_Await')

#AssignmentRestElement[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
builder.r(w=1, d='AssignmentRestElement : `...` DestructuringAssignmentTarget')

#AssignmentRestElement[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
builder.r(w=1, d='AssignmentRestElement_Yield : `...` DestructuringAssignmentTarget_Yield')

#AssignmentRestElement[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
builder.r(w=1, d='AssignmentRestElement_Await : `...` DestructuringAssignmentTarget_Await')

#AssignmentRestElement[Yield, Await]  : `...` DestructuringAssignmentTarget[?Yield, ?Await]
builder.r(w=1, d='AssignmentRestElement_Yield_Await : `...` DestructuringAssignmentTarget_Yield_Await')

#DestructuringAssignmentTarget[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
builder.r(w=1, d='DestructuringAssignmentTarget : LeftHandSideExpression')

#DestructuringAssignmentTarget[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
builder.r(w=1, d='DestructuringAssignmentTarget_Yield : LeftHandSideExpression_Yield')

#DestructuringAssignmentTarget[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
builder.r(w=1, d='DestructuringAssignmentTarget_Await : LeftHandSideExpression_Await')

#DestructuringAssignmentTarget[Yield, Await]  : LeftHandSideExpression[?Yield, ?Await]
builder.r(w=1, d='DestructuringAssignmentTarget_Yield_Await : LeftHandSideExpression_Yield_Await')

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=100, d='Expression : AssignmentExpression')

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression_In : AssignmentExpression_In')

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression_Yield : AssignmentExpression_Yield')

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression_In_Yield : AssignmentExpression_In_Yield')

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression_Await : AssignmentExpression_Await')

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression_In_Await : AssignmentExpression_In_Await')

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression_Yield_Await : AssignmentExpression_Yield_Await')

#Expression[In, Yield, Await]  : AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression_In_Yield_Await : AssignmentExpression_In_Yield_Await')

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression : Expression `,` AssignmentExpression')

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression_In : Expression_In `,` AssignmentExpression_In')

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression_Yield : Expression_Yield `,` AssignmentExpression_Yield')

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression_In_Yield : Expression_In_Yield `,` AssignmentExpression_In_Yield')

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression_Await : Expression_Await `,` AssignmentExpression_Await')

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression_In_Await : Expression_In_Await `,` AssignmentExpression_In_Await')

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression_Yield_Await : Expression_Yield_Await `,` AssignmentExpression_Yield_Await')

#Expression[In, Yield, Await]  : Expression[?In, ?Yield, ?Await] `,` AssignmentExpression[?In, ?Yield, ?Await]
builder.r(w=1, d='Expression_In_Yield_Await : Expression_In_Yield_Await `,` AssignmentExpression_In_Yield_Await')

