from language import Builder
from language import Stage
from language import State
builder = Builder.get_builder()

#Statement[Yield, Await, Return]  : BlockStatement[?Yield, ?Await, ?Return]
@builder.build('Statement : BlockStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BlockStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield : BlockStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BlockStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Await : BlockStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BlockStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Await : BlockStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BlockStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Return : BlockStatement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BlockStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Return : BlockStatement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BlockStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Await_Return : BlockStatement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BlockStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Await_Return : BlockStatement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : VariableStatement[?Yield, ?Await]
@builder.build('Statement : VariableStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : VariableStatement[?Yield, ?Await]
@builder.build('Statement_Yield : VariableStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : VariableStatement[?Yield, ?Await]
@builder.build('Statement_Await : VariableStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : VariableStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Await : VariableStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : VariableStatement[?Yield, ?Await]
@builder.build('Statement_Return : VariableStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : VariableStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Return : VariableStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : VariableStatement[?Yield, ?Await]
@builder.build('Statement_Await_Return : VariableStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : VariableStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Await_Return : VariableStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : EmptyStatement
@builder.build('Statement : EmptyStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : EmptyStatement
@builder.build('Statement_Yield : EmptyStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : EmptyStatement
@builder.build('Statement_Await : EmptyStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : EmptyStatement
@builder.build('Statement_Yield_Await : EmptyStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : EmptyStatement
@builder.build('Statement_Return : EmptyStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : EmptyStatement
@builder.build('Statement_Yield_Return : EmptyStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : EmptyStatement
@builder.build('Statement_Await_Return : EmptyStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : EmptyStatement
@builder.build('Statement_Yield_Await_Return : EmptyStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ExpressionStatement[?Yield, ?Await]
@builder.build('Statement : ExpressionStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ExpressionStatement[?Yield, ?Await]
@builder.build('Statement_Yield : ExpressionStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ExpressionStatement[?Yield, ?Await]
@builder.build('Statement_Await : ExpressionStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ExpressionStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Await : ExpressionStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ExpressionStatement[?Yield, ?Await]
@builder.build('Statement_Return : ExpressionStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ExpressionStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Return : ExpressionStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ExpressionStatement[?Yield, ?Await]
@builder.build('Statement_Await_Return : ExpressionStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ExpressionStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Await_Return : ExpressionStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : IfStatement[?Yield, ?Await, ?Return]
@builder.build('Statement : IfStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : IfStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield : IfStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : IfStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Await : IfStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : IfStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Await : IfStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : IfStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Return : IfStatement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : IfStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Return : IfStatement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : IfStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Await_Return : IfStatement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : IfStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Await_Return : IfStatement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakableStatement[?Yield, ?Await, ?Return]
@builder.build('Statement : BreakableStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakableStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield : BreakableStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakableStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Await : BreakableStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakableStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Await : BreakableStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakableStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Return : BreakableStatement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakableStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Return : BreakableStatement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakableStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Await_Return : BreakableStatement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakableStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Await_Return : BreakableStatement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ContinueStatement[?Yield, ?Await]
@builder.build('Statement : ContinueStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ContinueStatement[?Yield, ?Await]
@builder.build('Statement_Yield : ContinueStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ContinueStatement[?Yield, ?Await]
@builder.build('Statement_Await : ContinueStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ContinueStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Await : ContinueStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ContinueStatement[?Yield, ?Await]
@builder.build('Statement_Return : ContinueStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ContinueStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Return : ContinueStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ContinueStatement[?Yield, ?Await]
@builder.build('Statement_Await_Return : ContinueStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ContinueStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Await_Return : ContinueStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakStatement[?Yield, ?Await]
@builder.build('Statement : BreakStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakStatement[?Yield, ?Await]
@builder.build('Statement_Yield : BreakStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakStatement[?Yield, ?Await]
@builder.build('Statement_Await : BreakStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Await : BreakStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakStatement[?Yield, ?Await]
@builder.build('Statement_Return : BreakStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Return : BreakStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakStatement[?Yield, ?Await]
@builder.build('Statement_Await_Return : BreakStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : BreakStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Await_Return : BreakStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : [+Return] ReturnStatement[?Yield, ?Await]
@builder.build('Statement_Return : ReturnStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : [+Return] ReturnStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Return : ReturnStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : [+Return] ReturnStatement[?Yield, ?Await]
@builder.build('Statement_Await_Return : ReturnStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : [+Return] ReturnStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Await_Return : ReturnStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : WithStatement[?Yield, ?Await, ?Return]
@builder.build('Statement : WithStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : WithStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield : WithStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : WithStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Await : WithStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : WithStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Await : WithStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : WithStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Return : WithStatement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : WithStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Return : WithStatement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : WithStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Await_Return : WithStatement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : WithStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Await_Return : WithStatement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : LabelledStatement[?Yield, ?Await, ?Return]
@builder.build('Statement : LabelledStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : LabelledStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield : LabelledStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : LabelledStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Await : LabelledStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : LabelledStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Await : LabelledStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : LabelledStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Return : LabelledStatement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : LabelledStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Return : LabelledStatement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : LabelledStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Await_Return : LabelledStatement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : LabelledStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Await_Return : LabelledStatement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ThrowStatement[?Yield, ?Await]
@builder.build('Statement : ThrowStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ThrowStatement[?Yield, ?Await]
@builder.build('Statement_Yield : ThrowStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ThrowStatement[?Yield, ?Await]
@builder.build('Statement_Await : ThrowStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ThrowStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Await : ThrowStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ThrowStatement[?Yield, ?Await]
@builder.build('Statement_Return : ThrowStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ThrowStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Return : ThrowStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ThrowStatement[?Yield, ?Await]
@builder.build('Statement_Await_Return : ThrowStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : ThrowStatement[?Yield, ?Await]
@builder.build('Statement_Yield_Await_Return : ThrowStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : TryStatement[?Yield, ?Await, ?Return]
@builder.build('Statement : TryStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : TryStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield : TryStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : TryStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Await : TryStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : TryStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Await : TryStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : TryStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Return : TryStatement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : TryStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Return : TryStatement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : TryStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Await_Return : TryStatement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : TryStatement[?Yield, ?Await, ?Return]
@builder.build('Statement_Yield_Await_Return : TryStatement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : DebuggerStatement
@builder.build('Statement : DebuggerStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : DebuggerStatement
@builder.build('Statement_Yield : DebuggerStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : DebuggerStatement
@builder.build('Statement_Await : DebuggerStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : DebuggerStatement
@builder.build('Statement_Yield_Await : DebuggerStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : DebuggerStatement
@builder.build('Statement_Return : DebuggerStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : DebuggerStatement
@builder.build('Statement_Yield_Return : DebuggerStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : DebuggerStatement
@builder.build('Statement_Await_Return : DebuggerStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Statement[Yield, Await, Return]  : DebuggerStatement
@builder.build('Statement_Yield_Await_Return : DebuggerStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Declaration[Yield, Await]  : HoistableDeclaration[?Yield, ?Await, ~Default]
@builder.build('Declaration : HoistableDeclaration')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Declaration[Yield, Await]  : HoistableDeclaration[?Yield, ?Await, ~Default]
@builder.build('Declaration_Yield : HoistableDeclaration_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Declaration[Yield, Await]  : HoistableDeclaration[?Yield, ?Await, ~Default]
@builder.build('Declaration_Await : HoistableDeclaration_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Declaration[Yield, Await]  : HoistableDeclaration[?Yield, ?Await, ~Default]
@builder.build('Declaration_Yield_Await : HoistableDeclaration_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Declaration[Yield, Await]  : ClassDeclaration[?Yield, ?Await, ~Default]
@builder.build('Declaration : ClassDeclaration')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Declaration[Yield, Await]  : ClassDeclaration[?Yield, ?Await, ~Default]
@builder.build('Declaration_Yield : ClassDeclaration_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Declaration[Yield, Await]  : ClassDeclaration[?Yield, ?Await, ~Default]
@builder.build('Declaration_Await : ClassDeclaration_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Declaration[Yield, Await]  : ClassDeclaration[?Yield, ?Await, ~Default]
@builder.build('Declaration_Yield_Await : ClassDeclaration_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Declaration[Yield, Await]  : LexicalDeclaration[+In, ?Yield, ?Await]
@builder.build('Declaration : LexicalDeclaration_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Declaration[Yield, Await]  : LexicalDeclaration[+In, ?Yield, ?Await]
@builder.build('Declaration_Yield : LexicalDeclaration_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Declaration[Yield, Await]  : LexicalDeclaration[+In, ?Yield, ?Await]
@builder.build('Declaration_Await : LexicalDeclaration_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Declaration[Yield, Await]  : LexicalDeclaration[+In, ?Yield, ?Await]
@builder.build('Declaration_Yield_Await : LexicalDeclaration_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : FunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration : FunctionDeclaration')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : FunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield : FunctionDeclaration_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : FunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Await : FunctionDeclaration_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : FunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield_Await : FunctionDeclaration_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : FunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Default : FunctionDeclaration_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : FunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield_Default : FunctionDeclaration_Yield_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : FunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Await_Default : FunctionDeclaration_Await_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : FunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield_Await_Default : FunctionDeclaration_Yield_Await_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : GeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration : GeneratorDeclaration')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : GeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield : GeneratorDeclaration_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : GeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Await : GeneratorDeclaration_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : GeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield_Await : GeneratorDeclaration_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : GeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Default : GeneratorDeclaration_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : GeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield_Default : GeneratorDeclaration_Yield_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : GeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Await_Default : GeneratorDeclaration_Await_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : GeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield_Await_Default : GeneratorDeclaration_Yield_Await_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncFunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration : AsyncFunctionDeclaration')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncFunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield : AsyncFunctionDeclaration_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncFunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Await : AsyncFunctionDeclaration_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncFunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield_Await : AsyncFunctionDeclaration_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncFunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Default : AsyncFunctionDeclaration_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncFunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield_Default : AsyncFunctionDeclaration_Yield_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncFunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Await_Default : AsyncFunctionDeclaration_Await_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncFunctionDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield_Await_Default : AsyncFunctionDeclaration_Yield_Await_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncGeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration : AsyncGeneratorDeclaration')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncGeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield : AsyncGeneratorDeclaration_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncGeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Await : AsyncGeneratorDeclaration_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncGeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield_Await : AsyncGeneratorDeclaration_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncGeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Default : AsyncGeneratorDeclaration_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncGeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield_Default : AsyncGeneratorDeclaration_Yield_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncGeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Await_Default : AsyncGeneratorDeclaration_Await_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#HoistableDeclaration[Yield, Await, Default]  : AsyncGeneratorDeclaration[?Yield, ?Await, ?Default]
@builder.build('HoistableDeclaration_Yield_Await_Default : AsyncGeneratorDeclaration_Yield_Await_Default')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : IterationStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement : IterationStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : IterationStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement_Yield : IterationStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : IterationStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement_Await : IterationStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : IterationStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement_Yield_Await : IterationStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : IterationStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement_Return : IterationStatement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : IterationStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement_Yield_Return : IterationStatement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : IterationStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement_Await_Return : IterationStatement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : IterationStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement_Yield_Await_Return : IterationStatement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : SwitchStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement : SwitchStatement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : SwitchStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement_Yield : SwitchStatement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : SwitchStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement_Await : SwitchStatement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : SwitchStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement_Yield_Await : SwitchStatement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : SwitchStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement_Return : SwitchStatement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : SwitchStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement_Yield_Return : SwitchStatement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : SwitchStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement_Await_Return : SwitchStatement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakableStatement[Yield, Await, Return]  : SwitchStatement[?Yield, ?Await, ?Return]
@builder.build('BreakableStatement_Yield_Await_Return : SwitchStatement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BlockStatement[Yield, Await, Return]  : Block[?Yield, ?Await, ?Return]
@builder.build('BlockStatement : Block')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BlockStatement[Yield, Await, Return]  : Block[?Yield, ?Await, ?Return]
@builder.build('BlockStatement_Yield : Block_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BlockStatement[Yield, Await, Return]  : Block[?Yield, ?Await, ?Return]
@builder.build('BlockStatement_Await : Block_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BlockStatement[Yield, Await, Return]  : Block[?Yield, ?Await, ?Return]
@builder.build('BlockStatement_Yield_Await : Block_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BlockStatement[Yield, Await, Return]  : Block[?Yield, ?Await, ?Return]
@builder.build('BlockStatement_Return : Block_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BlockStatement[Yield, Await, Return]  : Block[?Yield, ?Await, ?Return]
@builder.build('BlockStatement_Yield_Return : Block_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BlockStatement[Yield, Await, Return]  : Block[?Yield, ?Await, ?Return]
@builder.build('BlockStatement_Await_Return : Block_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BlockStatement[Yield, Await, Return]  : Block[?Yield, ?Await, ?Return]
@builder.build('BlockStatement_Yield_Await_Return : Block_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block : `{` StatementList `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block_Yield : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block_Yield : `{` StatementList_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block_Await : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block_Await : `{` StatementList_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block_Yield_Await : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block_Yield_Await : `{` StatementList_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block_Return : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block_Return : `{` StatementList_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block_Yield_Return : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block_Yield_Return : `{` StatementList_Yield_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block_Await_Return : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block_Await_Return : `{` StatementList_Await_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block_Yield_Await_Return : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Block[Yield, Await, Return]  : `{` StatementList[?Yield, ?Await, ?Return]? `}`
@builder.build('Block_Yield_Await_Return : `{` StatementList_Yield_Await_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList : StatementListItem')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList_Yield : StatementListItem_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList_Await : StatementListItem_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList_Yield_Await : StatementListItem_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList_Return : StatementListItem_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList_Yield_Return : StatementListItem_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList_Await_Return : StatementListItem_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList_Yield_Await_Return : StatementListItem_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementList[?Yield, ?Await, ?Return] StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList : StatementList StatementListItem')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementList[?Yield, ?Await, ?Return] StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList_Yield : StatementList_Yield StatementListItem_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementList[?Yield, ?Await, ?Return] StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList_Await : StatementList_Await StatementListItem_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementList[?Yield, ?Await, ?Return] StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList_Yield_Await : StatementList_Yield_Await StatementListItem_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementList[?Yield, ?Await, ?Return] StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList_Return : StatementList_Return StatementListItem_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementList[?Yield, ?Await, ?Return] StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList_Yield_Return : StatementList_Yield_Return StatementListItem_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementList[?Yield, ?Await, ?Return] StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList_Await_Return : StatementList_Await_Return StatementListItem_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementList[Yield, Await, Return]  : StatementList[?Yield, ?Await, ?Return] StatementListItem[?Yield, ?Await, ?Return]
@builder.build('StatementList_Yield_Await_Return : StatementList_Yield_Await_Return StatementListItem_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('StatementListItem : Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('StatementListItem_Yield : Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('StatementListItem_Await : Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('StatementListItem_Yield_Await : Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('StatementListItem_Return : Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('StatementListItem_Yield_Return : Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('StatementListItem_Await_Return : Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('StatementListItem_Yield_Await_Return : Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Declaration[?Yield, ?Await]
@builder.build('StatementListItem : Declaration')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Declaration[?Yield, ?Await]
@builder.build('StatementListItem_Yield : Declaration_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Declaration[?Yield, ?Await]
@builder.build('StatementListItem_Await : Declaration_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Declaration[?Yield, ?Await]
@builder.build('StatementListItem_Yield_Await : Declaration_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Declaration[?Yield, ?Await]
@builder.build('StatementListItem_Return : Declaration')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Declaration[?Yield, ?Await]
@builder.build('StatementListItem_Yield_Return : Declaration_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Declaration[?Yield, ?Await]
@builder.build('StatementListItem_Await_Return : Declaration_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#StatementListItem[Yield, Await, Return]  : Declaration[?Yield, ?Await]
@builder.build('StatementListItem_Yield_Await_Return : Declaration_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalDeclaration[In, Yield, Await]  : LetOrConst BindingList[?In, ?Yield, ?Await] `;`
@builder.build('LexicalDeclaration : LetOrConst BindingList `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalDeclaration[In, Yield, Await]  : LetOrConst BindingList[?In, ?Yield, ?Await] `;`
@builder.build('LexicalDeclaration_In : LetOrConst BindingList_In `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalDeclaration[In, Yield, Await]  : LetOrConst BindingList[?In, ?Yield, ?Await] `;`
@builder.build('LexicalDeclaration_Yield : LetOrConst BindingList_Yield `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalDeclaration[In, Yield, Await]  : LetOrConst BindingList[?In, ?Yield, ?Await] `;`
@builder.build('LexicalDeclaration_In_Yield : LetOrConst BindingList_In_Yield `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalDeclaration[In, Yield, Await]  : LetOrConst BindingList[?In, ?Yield, ?Await] `;`
@builder.build('LexicalDeclaration_Await : LetOrConst BindingList_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalDeclaration[In, Yield, Await]  : LetOrConst BindingList[?In, ?Yield, ?Await] `;`
@builder.build('LexicalDeclaration_In_Await : LetOrConst BindingList_In_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalDeclaration[In, Yield, Await]  : LetOrConst BindingList[?In, ?Yield, ?Await] `;`
@builder.build('LexicalDeclaration_Yield_Await : LetOrConst BindingList_Yield_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalDeclaration[In, Yield, Await]  : LetOrConst BindingList[?In, ?Yield, ?Await] `;`
@builder.build('LexicalDeclaration_In_Yield_Await : LetOrConst BindingList_In_Yield_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LetOrConst  : `let`
@builder.build('LetOrConst : `let`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LetOrConst  : `const`
@builder.build('LetOrConst : `const`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList : LexicalBinding')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList_In : LexicalBinding_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList_Yield : LexicalBinding_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList_In_Yield : LexicalBinding_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList_Await : LexicalBinding_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList_In_Await : LexicalBinding_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList_Yield_Await : LexicalBinding_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList_In_Yield_Await : LexicalBinding_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : BindingList[?In, ?Yield, ?Await] `,` LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList : BindingList `,` LexicalBinding')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : BindingList[?In, ?Yield, ?Await] `,` LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList_In : BindingList_In `,` LexicalBinding_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : BindingList[?In, ?Yield, ?Await] `,` LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList_Yield : BindingList_Yield `,` LexicalBinding_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : BindingList[?In, ?Yield, ?Await] `,` LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList_In_Yield : BindingList_In_Yield `,` LexicalBinding_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : BindingList[?In, ?Yield, ?Await] `,` LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList_Await : BindingList_Await `,` LexicalBinding_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : BindingList[?In, ?Yield, ?Await] `,` LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList_In_Await : BindingList_In_Await `,` LexicalBinding_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : BindingList[?In, ?Yield, ?Await] `,` LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList_Yield_Await : BindingList_Yield_Await `,` LexicalBinding_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingList[In, Yield, Await]  : BindingList[?In, ?Yield, ?Await] `,` LexicalBinding[?In, ?Yield, ?Await]
@builder.build('BindingList_In_Yield_Await : BindingList_In_Yield_Await `,` LexicalBinding_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding : BindingIdentifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding : BindingIdentifier Initializer')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding_In : BindingIdentifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding_In : BindingIdentifier Initializer_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding_Yield : BindingIdentifier_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding_Yield : BindingIdentifier_Yield Initializer_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding_In_Yield : BindingIdentifier_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding_In_Yield : BindingIdentifier_Yield Initializer_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding_Await : BindingIdentifier_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding_Await : BindingIdentifier_Await Initializer_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding_In_Await : BindingIdentifier_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding_In_Await : BindingIdentifier_Await Initializer_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding_Yield_Await : BindingIdentifier_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding_Yield_Await : BindingIdentifier_Yield_Await Initializer_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding_In_Yield_Await : BindingIdentifier_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('LexicalBinding_In_Yield_Await : BindingIdentifier_Yield_Await Initializer_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('LexicalBinding : BindingPattern Initializer')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('LexicalBinding_In : BindingPattern Initializer_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('LexicalBinding_Yield : BindingPattern_Yield Initializer_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('LexicalBinding_In_Yield : BindingPattern_Yield Initializer_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('LexicalBinding_Await : BindingPattern_Await Initializer_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('LexicalBinding_In_Await : BindingPattern_Await Initializer_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('LexicalBinding_Yield_Await : BindingPattern_Yield_Await Initializer_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LexicalBinding[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('LexicalBinding_In_Yield_Await : BindingPattern_Yield_Await Initializer_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableStatement[Yield, Await]  : `var` VariableDeclarationList[+In, ?Yield, ?Await] `;`
@builder.build('VariableStatement : `var` VariableDeclarationList_In `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableStatement[Yield, Await]  : `var` VariableDeclarationList[+In, ?Yield, ?Await] `;`
@builder.build('VariableStatement_Yield : `var` VariableDeclarationList_In_Yield `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableStatement[Yield, Await]  : `var` VariableDeclarationList[+In, ?Yield, ?Await] `;`
@builder.build('VariableStatement_Await : `var` VariableDeclarationList_In_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableStatement[Yield, Await]  : `var` VariableDeclarationList[+In, ?Yield, ?Await] `;`
@builder.build('VariableStatement_Yield_Await : `var` VariableDeclarationList_In_Yield_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList : VariableDeclaration')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList_In : VariableDeclaration_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList_Yield : VariableDeclaration_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList_In_Yield : VariableDeclaration_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList_Await : VariableDeclaration_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList_In_Await : VariableDeclaration_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList_Yield_Await : VariableDeclaration_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList_In_Yield_Await : VariableDeclaration_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclarationList[?In, ?Yield, ?Await] `,` VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList : VariableDeclarationList `,` VariableDeclaration')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclarationList[?In, ?Yield, ?Await] `,` VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList_In : VariableDeclarationList_In `,` VariableDeclaration_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclarationList[?In, ?Yield, ?Await] `,` VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList_Yield : VariableDeclarationList_Yield `,` VariableDeclaration_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclarationList[?In, ?Yield, ?Await] `,` VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList_In_Yield : VariableDeclarationList_In_Yield `,` VariableDeclaration_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclarationList[?In, ?Yield, ?Await] `,` VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList_Await : VariableDeclarationList_Await `,` VariableDeclaration_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclarationList[?In, ?Yield, ?Await] `,` VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList_In_Await : VariableDeclarationList_In_Await `,` VariableDeclaration_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclarationList[?In, ?Yield, ?Await] `,` VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList_Yield_Await : VariableDeclarationList_Yield_Await `,` VariableDeclaration_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclarationList[In, Yield, Await]  : VariableDeclarationList[?In, ?Yield, ?Await] `,` VariableDeclaration[?In, ?Yield, ?Await]
@builder.build('VariableDeclarationList_In_Yield_Await : VariableDeclarationList_In_Yield_Await `,` VariableDeclaration_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration : BindingIdentifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration : BindingIdentifier Initializer')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration_In : BindingIdentifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration_In : BindingIdentifier Initializer_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration_Yield : BindingIdentifier_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration_Yield : BindingIdentifier_Yield Initializer_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration_In_Yield : BindingIdentifier_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration_In_Yield : BindingIdentifier_Yield Initializer_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration_Await : BindingIdentifier_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration_Await : BindingIdentifier_Await Initializer_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration_In_Await : BindingIdentifier_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration_In_Await : BindingIdentifier_Await Initializer_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration_Yield_Await : BindingIdentifier_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration_Yield_Await : BindingIdentifier_Yield_Await Initializer_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration_In_Yield_Await : BindingIdentifier_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]?
@builder.build('VariableDeclaration_In_Yield_Await : BindingIdentifier_Yield_Await Initializer_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('VariableDeclaration : BindingPattern Initializer')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('VariableDeclaration_In : BindingPattern Initializer_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('VariableDeclaration_Yield : BindingPattern_Yield Initializer_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('VariableDeclaration_In_Yield : BindingPattern_Yield Initializer_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('VariableDeclaration_Await : BindingPattern_Await Initializer_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('VariableDeclaration_In_Await : BindingPattern_Await Initializer_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('VariableDeclaration_Yield_Await : BindingPattern_Yield_Await Initializer_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#VariableDeclaration[In, Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[?In, ?Yield, ?Await]
@builder.build('VariableDeclaration_In_Yield_Await : BindingPattern_Yield_Await Initializer_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPattern[Yield, Await]  : ObjectBindingPattern[?Yield, ?Await]
@builder.build('BindingPattern : ObjectBindingPattern')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPattern[Yield, Await]  : ObjectBindingPattern[?Yield, ?Await]
@builder.build('BindingPattern_Yield : ObjectBindingPattern_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPattern[Yield, Await]  : ObjectBindingPattern[?Yield, ?Await]
@builder.build('BindingPattern_Await : ObjectBindingPattern_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPattern[Yield, Await]  : ObjectBindingPattern[?Yield, ?Await]
@builder.build('BindingPattern_Yield_Await : ObjectBindingPattern_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPattern[Yield, Await]  : ArrayBindingPattern[?Yield, ?Await]
@builder.build('BindingPattern : ArrayBindingPattern')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPattern[Yield, Await]  : ArrayBindingPattern[?Yield, ?Await]
@builder.build('BindingPattern_Yield : ArrayBindingPattern_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPattern[Yield, Await]  : ArrayBindingPattern[?Yield, ?Await]
@builder.build('BindingPattern_Await : ArrayBindingPattern_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPattern[Yield, Await]  : ArrayBindingPattern[?Yield, ?Await]
@builder.build('BindingPattern_Yield_Await : ArrayBindingPattern_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` `}`
@builder.build('ObjectBindingPattern : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` `}`
@builder.build('ObjectBindingPattern_Yield : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` `}`
@builder.build('ObjectBindingPattern_Await : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` `}`
@builder.build('ObjectBindingPattern_Yield_Await : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingRestProperty[?Yield, ?Await] `}`
@builder.build('ObjectBindingPattern : `{` BindingRestProperty `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingRestProperty[?Yield, ?Await] `}`
@builder.build('ObjectBindingPattern_Yield : `{` BindingRestProperty_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingRestProperty[?Yield, ?Await] `}`
@builder.build('ObjectBindingPattern_Await : `{` BindingRestProperty_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingRestProperty[?Yield, ?Await] `}`
@builder.build('ObjectBindingPattern_Yield_Await : `{` BindingRestProperty_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingPropertyList[?Yield, ?Await] `}`
@builder.build('ObjectBindingPattern : `{` BindingPropertyList `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingPropertyList[?Yield, ?Await] `}`
@builder.build('ObjectBindingPattern_Yield : `{` BindingPropertyList_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingPropertyList[?Yield, ?Await] `}`
@builder.build('ObjectBindingPattern_Await : `{` BindingPropertyList_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingPropertyList[?Yield, ?Await] `}`
@builder.build('ObjectBindingPattern_Yield_Await : `{` BindingPropertyList_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingPropertyList[?Yield, ?Await] `,` BindingRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectBindingPattern : `{` BindingPropertyList `,` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingPropertyList[?Yield, ?Await] `,` BindingRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectBindingPattern : `{` BindingPropertyList `,` BindingRestProperty `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingPropertyList[?Yield, ?Await] `,` BindingRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectBindingPattern_Yield : `{` BindingPropertyList_Yield `,` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingPropertyList[?Yield, ?Await] `,` BindingRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectBindingPattern_Yield : `{` BindingPropertyList_Yield `,` BindingRestProperty_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingPropertyList[?Yield, ?Await] `,` BindingRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectBindingPattern_Await : `{` BindingPropertyList_Await `,` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingPropertyList[?Yield, ?Await] `,` BindingRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectBindingPattern_Await : `{` BindingPropertyList_Await `,` BindingRestProperty_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingPropertyList[?Yield, ?Await] `,` BindingRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectBindingPattern_Yield_Await : `{` BindingPropertyList_Yield_Await `,` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ObjectBindingPattern[Yield, Await]  : `{` BindingPropertyList[?Yield, ?Await] `,` BindingRestProperty[?Yield, ?Await]? `}`
@builder.build('ObjectBindingPattern_Yield_Await : `{` BindingPropertyList_Yield_Await `,` BindingRestProperty_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern : `[` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern : `[` BindingRestElement `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern : `[` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern : `[` Elision BindingRestElement `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield : `[` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield : `[` BindingRestElement_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield : `[` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield : `[` Elision BindingRestElement_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Await : `[` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Await : `[` BindingRestElement_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Await : `[` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Await : `[` Elision BindingRestElement_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield_Await : `[` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield_Await : `[` BindingRestElement_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield_Await : `[` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield_Await : `[` Elision BindingRestElement_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `]`
@builder.build('ArrayBindingPattern : `[` BindingElementList `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `]`
@builder.build('ArrayBindingPattern_Yield : `[` BindingElementList_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `]`
@builder.build('ArrayBindingPattern_Await : `[` BindingElementList_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `]`
@builder.build('ArrayBindingPattern_Yield_Await : `[` BindingElementList_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern : `[` BindingElementList `,` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern : `[` BindingElementList `,` BindingRestElement `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern : `[` BindingElementList `,` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern : `[` BindingElementList `,` Elision BindingRestElement `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield : `[` BindingElementList_Yield `,` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield : `[` BindingElementList_Yield `,` BindingRestElement_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield : `[` BindingElementList_Yield `,` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield : `[` BindingElementList_Yield `,` Elision BindingRestElement_Yield `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Await : `[` BindingElementList_Await `,` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Await : `[` BindingElementList_Await `,` BindingRestElement_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Await : `[` BindingElementList_Await `,` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Await : `[` BindingElementList_Await `,` Elision BindingRestElement_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield_Await : `[` BindingElementList_Yield_Await `,` `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield_Await : `[` BindingElementList_Yield_Await `,` BindingRestElement_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield_Await : `[` BindingElementList_Yield_Await `,` Elision `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ArrayBindingPattern[Yield, Await]  : `[` BindingElementList[?Yield, ?Await] `,` Elision? BindingRestElement[?Yield, ?Await]? `]`
@builder.build('ArrayBindingPattern_Yield_Await : `[` BindingElementList_Yield_Await `,` Elision BindingRestElement_Yield_Await `]`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingRestProperty[Yield, Await]  : `...` BindingIdentifier[?Yield, ?Await]
@builder.build('BindingRestProperty : `...` BindingIdentifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingRestProperty[Yield, Await]  : `...` BindingIdentifier[?Yield, ?Await]
@builder.build('BindingRestProperty_Yield : `...` BindingIdentifier_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingRestProperty[Yield, Await]  : `...` BindingIdentifier[?Yield, ?Await]
@builder.build('BindingRestProperty_Await : `...` BindingIdentifier_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingRestProperty[Yield, Await]  : `...` BindingIdentifier[?Yield, ?Await]
@builder.build('BindingRestProperty_Yield_Await : `...` BindingIdentifier_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPropertyList[Yield, Await]  : BindingProperty[?Yield, ?Await]
@builder.build('BindingPropertyList : BindingProperty')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPropertyList[Yield, Await]  : BindingProperty[?Yield, ?Await]
@builder.build('BindingPropertyList_Yield : BindingProperty_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPropertyList[Yield, Await]  : BindingProperty[?Yield, ?Await]
@builder.build('BindingPropertyList_Await : BindingProperty_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPropertyList[Yield, Await]  : BindingProperty[?Yield, ?Await]
@builder.build('BindingPropertyList_Yield_Await : BindingProperty_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPropertyList[Yield, Await]  : BindingPropertyList[?Yield, ?Await] `,` BindingProperty[?Yield, ?Await]
@builder.build('BindingPropertyList : BindingPropertyList `,` BindingProperty')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPropertyList[Yield, Await]  : BindingPropertyList[?Yield, ?Await] `,` BindingProperty[?Yield, ?Await]
@builder.build('BindingPropertyList_Yield : BindingPropertyList_Yield `,` BindingProperty_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPropertyList[Yield, Await]  : BindingPropertyList[?Yield, ?Await] `,` BindingProperty[?Yield, ?Await]
@builder.build('BindingPropertyList_Await : BindingPropertyList_Await `,` BindingProperty_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingPropertyList[Yield, Await]  : BindingPropertyList[?Yield, ?Await] `,` BindingProperty[?Yield, ?Await]
@builder.build('BindingPropertyList_Yield_Await : BindingPropertyList_Yield_Await `,` BindingProperty_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElementList[Yield, Await]  : BindingElisionElement[?Yield, ?Await]
@builder.build('BindingElementList : BindingElisionElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElementList[Yield, Await]  : BindingElisionElement[?Yield, ?Await]
@builder.build('BindingElementList_Yield : BindingElisionElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElementList[Yield, Await]  : BindingElisionElement[?Yield, ?Await]
@builder.build('BindingElementList_Await : BindingElisionElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElementList[Yield, Await]  : BindingElisionElement[?Yield, ?Await]
@builder.build('BindingElementList_Yield_Await : BindingElisionElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElementList[Yield, Await]  : BindingElementList[?Yield, ?Await] `,` BindingElisionElement[?Yield, ?Await]
@builder.build('BindingElementList : BindingElementList `,` BindingElisionElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElementList[Yield, Await]  : BindingElementList[?Yield, ?Await] `,` BindingElisionElement[?Yield, ?Await]
@builder.build('BindingElementList_Yield : BindingElementList_Yield `,` BindingElisionElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElementList[Yield, Await]  : BindingElementList[?Yield, ?Await] `,` BindingElisionElement[?Yield, ?Await]
@builder.build('BindingElementList_Await : BindingElementList_Await `,` BindingElisionElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElementList[Yield, Await]  : BindingElementList[?Yield, ?Await] `,` BindingElisionElement[?Yield, ?Await]
@builder.build('BindingElementList_Yield_Await : BindingElementList_Yield_Await `,` BindingElisionElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElisionElement[Yield, Await]  : Elision? BindingElement[?Yield, ?Await]
@builder.build('BindingElisionElement : BindingElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElisionElement[Yield, Await]  : Elision? BindingElement[?Yield, ?Await]
@builder.build('BindingElisionElement : Elision BindingElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElisionElement[Yield, Await]  : Elision? BindingElement[?Yield, ?Await]
@builder.build('BindingElisionElement_Yield : BindingElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElisionElement[Yield, Await]  : Elision? BindingElement[?Yield, ?Await]
@builder.build('BindingElisionElement_Yield : Elision BindingElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElisionElement[Yield, Await]  : Elision? BindingElement[?Yield, ?Await]
@builder.build('BindingElisionElement_Await : BindingElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElisionElement[Yield, Await]  : Elision? BindingElement[?Yield, ?Await]
@builder.build('BindingElisionElement_Await : Elision BindingElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElisionElement[Yield, Await]  : Elision? BindingElement[?Yield, ?Await]
@builder.build('BindingElisionElement_Yield_Await : BindingElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElisionElement[Yield, Await]  : Elision? BindingElement[?Yield, ?Await]
@builder.build('BindingElisionElement_Yield_Await : Elision BindingElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingProperty[Yield, Await]  : SingleNameBinding[?Yield, ?Await]
@builder.build('BindingProperty : SingleNameBinding')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingProperty[Yield, Await]  : SingleNameBinding[?Yield, ?Await]
@builder.build('BindingProperty_Yield : SingleNameBinding_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingProperty[Yield, Await]  : SingleNameBinding[?Yield, ?Await]
@builder.build('BindingProperty_Await : SingleNameBinding_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingProperty[Yield, Await]  : SingleNameBinding[?Yield, ?Await]
@builder.build('BindingProperty_Yield_Await : SingleNameBinding_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingProperty[Yield, Await]  : PropertyName[?Yield, ?Await] `:` BindingElement[?Yield, ?Await]
@builder.build('BindingProperty : PropertyName `:` BindingElement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingProperty[Yield, Await]  : PropertyName[?Yield, ?Await] `:` BindingElement[?Yield, ?Await]
@builder.build('BindingProperty_Yield : PropertyName_Yield `:` BindingElement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingProperty[Yield, Await]  : PropertyName[?Yield, ?Await] `:` BindingElement[?Yield, ?Await]
@builder.build('BindingProperty_Await : PropertyName_Await `:` BindingElement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingProperty[Yield, Await]  : PropertyName[?Yield, ?Await] `:` BindingElement[?Yield, ?Await]
@builder.build('BindingProperty_Yield_Await : PropertyName_Yield_Await `:` BindingElement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElement[Yield, Await]  : SingleNameBinding[?Yield, ?Await]
@builder.build('BindingElement : SingleNameBinding')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElement[Yield, Await]  : SingleNameBinding[?Yield, ?Await]
@builder.build('BindingElement_Yield : SingleNameBinding_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElement[Yield, Await]  : SingleNameBinding[?Yield, ?Await]
@builder.build('BindingElement_Await : SingleNameBinding_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElement[Yield, Await]  : SingleNameBinding[?Yield, ?Await]
@builder.build('BindingElement_Yield_Await : SingleNameBinding_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElement[Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('BindingElement : BindingPattern')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElement[Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('BindingElement : BindingPattern Initializer_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElement[Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('BindingElement_Yield : BindingPattern_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElement[Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('BindingElement_Yield : BindingPattern_Yield Initializer_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElement[Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('BindingElement_Await : BindingPattern_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElement[Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('BindingElement_Await : BindingPattern_Await Initializer_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElement[Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('BindingElement_Yield_Await : BindingPattern_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingElement[Yield, Await]  : BindingPattern[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('BindingElement_Yield_Await : BindingPattern_Yield_Await Initializer_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SingleNameBinding[Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('SingleNameBinding : BindingIdentifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SingleNameBinding[Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('SingleNameBinding : BindingIdentifier Initializer_In')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SingleNameBinding[Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('SingleNameBinding_Yield : BindingIdentifier_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SingleNameBinding[Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('SingleNameBinding_Yield : BindingIdentifier_Yield Initializer_In_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SingleNameBinding[Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('SingleNameBinding_Await : BindingIdentifier_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SingleNameBinding[Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('SingleNameBinding_Await : BindingIdentifier_Await Initializer_In_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SingleNameBinding[Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('SingleNameBinding_Yield_Await : BindingIdentifier_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SingleNameBinding[Yield, Await]  : BindingIdentifier[?Yield, ?Await] Initializer[+In, ?Yield, ?Await]?
@builder.build('SingleNameBinding_Yield_Await : BindingIdentifier_Yield_Await Initializer_In_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingRestElement[Yield, Await]  : `...` BindingIdentifier[?Yield, ?Await]
@builder.build('BindingRestElement : `...` BindingIdentifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingRestElement[Yield, Await]  : `...` BindingIdentifier[?Yield, ?Await]
@builder.build('BindingRestElement_Yield : `...` BindingIdentifier_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingRestElement[Yield, Await]  : `...` BindingIdentifier[?Yield, ?Await]
@builder.build('BindingRestElement_Await : `...` BindingIdentifier_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingRestElement[Yield, Await]  : `...` BindingIdentifier[?Yield, ?Await]
@builder.build('BindingRestElement_Yield_Await : `...` BindingIdentifier_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingRestElement[Yield, Await]  : `...` BindingPattern[?Yield, ?Await]
@builder.build('BindingRestElement : `...` BindingPattern')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingRestElement[Yield, Await]  : `...` BindingPattern[?Yield, ?Await]
@builder.build('BindingRestElement_Yield : `...` BindingPattern_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingRestElement[Yield, Await]  : `...` BindingPattern[?Yield, ?Await]
@builder.build('BindingRestElement_Await : `...` BindingPattern_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BindingRestElement[Yield, Await]  : `...` BindingPattern[?Yield, ?Await]
@builder.build('BindingRestElement_Yield_Await : `...` BindingPattern_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#EmptyStatement  : `;`
@builder.build('EmptyStatement : `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ExpressionStatement[Yield, Await]  :   Expression[+In, ?Yield, ?Await] `;`
@builder.build('ExpressionStatement : Expression_In `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ExpressionStatement[Yield, Await]  :   Expression[+In, ?Yield, ?Await] `;`
@builder.build('ExpressionStatement_Yield : Expression_In_Yield `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ExpressionStatement[Yield, Await]  :   Expression[+In, ?Yield, ?Await] `;`
@builder.build('ExpressionStatement_Await : Expression_In_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ExpressionStatement[Yield, Await]  :   Expression[+In, ?Yield, ?Await] `;`
@builder.build('ExpressionStatement_Yield_Await : Expression_In_Yield_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return] `else` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement : `if` `(` Expression_In `)` Statement `else` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return] `else` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement_Yield : `if` `(` Expression_In_Yield `)` Statement_Yield `else` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return] `else` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement_Await : `if` `(` Expression_In_Await `)` Statement_Await `else` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return] `else` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement_Yield_Await : `if` `(` Expression_In_Yield_Await `)` Statement_Yield_Await `else` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return] `else` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement_Return : `if` `(` Expression_In `)` Statement_Return `else` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return] `else` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement_Yield_Return : `if` `(` Expression_In_Yield `)` Statement_Yield_Return `else` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return] `else` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement_Await_Return : `if` `(` Expression_In_Await `)` Statement_Await_Return `else` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return] `else` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement_Yield_Await_Return : `if` `(` Expression_In_Yield_Await `)` Statement_Yield_Await_Return `else` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement : `if` `(` Expression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement_Yield : `if` `(` Expression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement_Await : `if` `(` Expression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement_Yield_Await : `if` `(` Expression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement_Return : `if` `(` Expression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement_Yield_Return : `if` `(` Expression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement_Await_Return : `if` `(` Expression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IfStatement[Yield, Await, Return]  : `if` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IfStatement_Yield_Await_Return : `if` `(` Expression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `do` Statement[?Yield, ?Await, ?Return] `while` `(` Expression[+In, ?Yield, ?Await] `)` `;`
@builder.build('IterationStatement : `do` Statement `while` `(` Expression_In `)` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `do` Statement[?Yield, ?Await, ?Return] `while` `(` Expression[+In, ?Yield, ?Await] `)` `;`
@builder.build('IterationStatement_Yield : `do` Statement_Yield `while` `(` Expression_In_Yield `)` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `do` Statement[?Yield, ?Await, ?Return] `while` `(` Expression[+In, ?Yield, ?Await] `)` `;`
@builder.build('IterationStatement_Await : `do` Statement_Await `while` `(` Expression_In_Await `)` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `do` Statement[?Yield, ?Await, ?Return] `while` `(` Expression[+In, ?Yield, ?Await] `)` `;`
@builder.build('IterationStatement_Yield_Await : `do` Statement_Yield_Await `while` `(` Expression_In_Yield_Await `)` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `do` Statement[?Yield, ?Await, ?Return] `while` `(` Expression[+In, ?Yield, ?Await] `)` `;`
@builder.build('IterationStatement_Return : `do` Statement_Return `while` `(` Expression_In `)` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `do` Statement[?Yield, ?Await, ?Return] `while` `(` Expression[+In, ?Yield, ?Await] `)` `;`
@builder.build('IterationStatement_Yield_Return : `do` Statement_Yield_Return `while` `(` Expression_In_Yield `)` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `do` Statement[?Yield, ?Await, ?Return] `while` `(` Expression[+In, ?Yield, ?Await] `)` `;`
@builder.build('IterationStatement_Await_Return : `do` Statement_Await_Return `while` `(` Expression_In_Await `)` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `do` Statement[?Yield, ?Await, ?Return] `while` `(` Expression[+In, ?Yield, ?Await] `)` `;`
@builder.build('IterationStatement_Yield_Await_Return : `do` Statement_Yield_Await_Return `while` `(` Expression_In_Yield_Await `)` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `while` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `while` `(` Expression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `while` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `while` `(` Expression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `while` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `while` `(` Expression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `while` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `while` `(` Expression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `while` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `while` `(` Expression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `while` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `while` `(` Expression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `while` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `while` `(` Expression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `while` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `while` `(` Expression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` `;` `;` `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` `;` `;` Expression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` `;` Expression_In `;` `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` `;` Expression_In `;` Expression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` Expression `;` `;` `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` Expression `;` `;` Expression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` Expression `;` Expression_In `;` `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` Expression `;` Expression_In `;` Expression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` `;` `;` `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` `;` `;` Expression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` `;` Expression_In_Yield `;` `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` `;` Expression_In_Yield `;` Expression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` Expression_Yield `;` `;` `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` Expression_Yield `;` `;` Expression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` Expression_Yield `;` Expression_In_Yield `;` `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` Expression_Yield `;` Expression_In_Yield `;` Expression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` `;` `;` `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` `;` `;` Expression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` `;` Expression_In_Await `;` `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` `;` Expression_In_Await `;` Expression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` Expression_Await `;` `;` `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` Expression_Await `;` `;` Expression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` Expression_Await `;` Expression_In_Await `;` `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` Expression_Await `;` Expression_In_Await `;` Expression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` `;` `;` `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` `;` `;` Expression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` `;` Expression_In_Yield_Await `;` `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` `;` Expression_In_Yield_Await `;` Expression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` Expression_Yield_Await `;` `;` `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` Expression_Yield_Await `;` `;` Expression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` Expression_Yield_Await `;` Expression_In_Yield_Await `;` `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` Expression_Yield_Await `;` Expression_In_Yield_Await `;` Expression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` `;` `;` `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` `;` `;` Expression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` `;` Expression_In `;` `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` `;` Expression_In `;` Expression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` Expression `;` `;` `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` Expression `;` `;` Expression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` Expression `;` Expression_In `;` `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` Expression `;` Expression_In `;` Expression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` `;` `;` `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` `;` `;` Expression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` `;` Expression_In_Yield `;` `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` `;` Expression_In_Yield `;` Expression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` Expression_Yield `;` `;` `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` Expression_Yield `;` `;` Expression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` Expression_Yield `;` Expression_In_Yield `;` `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` Expression_Yield `;` Expression_In_Yield `;` Expression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` `;` `;` `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` `;` `;` Expression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` `;` Expression_In_Await `;` `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` `;` Expression_In_Await `;` Expression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` Expression_Await `;` `;` `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` Expression_Await `;` `;` Expression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` Expression_Await `;` Expression_In_Await `;` `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` Expression_Await `;` Expression_In_Await `;` Expression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` `;` `;` `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` `;` `;` Expression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` `;` Expression_In_Yield_Await `;` `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` `;` Expression_In_Yield_Await `;` Expression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` Expression_Yield_Await `;` `;` `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` Expression_Yield_Await `;` `;` Expression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` Expression_Yield_Await `;` Expression_In_Yield_Await `;` `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   Expression[~In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` Expression_Yield_Await `;` Expression_In_Yield_Await `;` Expression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` `var` VariableDeclarationList `;` `;` `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` `var` VariableDeclarationList `;` `;` Expression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` `var` VariableDeclarationList `;` Expression_In `;` `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` `var` VariableDeclarationList `;` Expression_In `;` Expression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` `var` VariableDeclarationList_Yield `;` `;` `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` `var` VariableDeclarationList_Yield `;` `;` Expression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` `var` VariableDeclarationList_Yield `;` Expression_In_Yield `;` `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` `var` VariableDeclarationList_Yield `;` Expression_In_Yield `;` Expression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` `var` VariableDeclarationList_Await `;` `;` `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` `var` VariableDeclarationList_Await `;` `;` Expression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` `var` VariableDeclarationList_Await `;` Expression_In_Await `;` `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` `var` VariableDeclarationList_Await `;` Expression_In_Await `;` Expression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` `var` VariableDeclarationList_Yield_Await `;` `;` `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` `var` VariableDeclarationList_Yield_Await `;` `;` Expression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` `var` VariableDeclarationList_Yield_Await `;` Expression_In_Yield_Await `;` `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` `var` VariableDeclarationList_Yield_Await `;` Expression_In_Yield_Await `;` Expression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` `var` VariableDeclarationList `;` `;` `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` `var` VariableDeclarationList `;` `;` Expression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` `var` VariableDeclarationList `;` Expression_In `;` `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` `var` VariableDeclarationList `;` Expression_In `;` Expression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` `var` VariableDeclarationList_Yield `;` `;` `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` `var` VariableDeclarationList_Yield `;` `;` Expression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` `var` VariableDeclarationList_Yield `;` Expression_In_Yield `;` `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` `var` VariableDeclarationList_Yield `;` Expression_In_Yield `;` Expression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` `var` VariableDeclarationList_Await `;` `;` `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` `var` VariableDeclarationList_Await `;` `;` Expression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` `var` VariableDeclarationList_Await `;` Expression_In_Await `;` `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` `var` VariableDeclarationList_Await `;` Expression_In_Await `;` Expression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` `var` VariableDeclarationList_Yield_Await `;` `;` `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` `var` VariableDeclarationList_Yield_Await `;` `;` Expression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` `var` VariableDeclarationList_Yield_Await `;` Expression_In_Yield_Await `;` `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` VariableDeclarationList[~In, ?Yield, ?Await] `;` Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` `var` VariableDeclarationList_Yield_Await `;` Expression_In_Yield_Await `;` Expression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` LexicalDeclaration `;` `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` LexicalDeclaration `;` Expression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` LexicalDeclaration Expression_In `;` `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` LexicalDeclaration Expression_In `;` Expression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` LexicalDeclaration_Yield `;` `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` LexicalDeclaration_Yield `;` Expression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` LexicalDeclaration_Yield Expression_In_Yield `;` `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` LexicalDeclaration_Yield Expression_In_Yield `;` Expression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` LexicalDeclaration_Await `;` `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` LexicalDeclaration_Await `;` Expression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` LexicalDeclaration_Await Expression_In_Await `;` `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` LexicalDeclaration_Await Expression_In_Await `;` Expression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` LexicalDeclaration_Yield_Await `;` `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` LexicalDeclaration_Yield_Await `;` Expression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` LexicalDeclaration_Yield_Await Expression_In_Yield_Await `;` `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` LexicalDeclaration_Yield_Await Expression_In_Yield_Await `;` Expression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` LexicalDeclaration `;` `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` LexicalDeclaration `;` Expression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` LexicalDeclaration Expression_In `;` `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` LexicalDeclaration Expression_In `;` Expression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` LexicalDeclaration_Yield `;` `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` LexicalDeclaration_Yield `;` Expression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` LexicalDeclaration_Yield Expression_In_Yield `;` `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` LexicalDeclaration_Yield Expression_In_Yield `;` Expression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` LexicalDeclaration_Await `;` `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` LexicalDeclaration_Await `;` Expression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` LexicalDeclaration_Await Expression_In_Await `;` `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` LexicalDeclaration_Await Expression_In_Await `;` Expression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` LexicalDeclaration_Yield_Await `;` `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` LexicalDeclaration_Yield_Await `;` Expression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` LexicalDeclaration_Yield_Await Expression_In_Yield_Await `;` `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` LexicalDeclaration[~In, ?Yield, ?Await] Expression[+In, ?Yield, ?Await]? `;` Expression[+In, ?Yield, ?Await]? `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` LexicalDeclaration_Yield_Await Expression_In_Yield_Await `;` Expression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` LeftHandSideExpression `in` Expression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` LeftHandSideExpression_Yield `in` Expression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` LeftHandSideExpression_Await `in` Expression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` LeftHandSideExpression_Yield_Await `in` Expression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` LeftHandSideExpression `in` Expression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` LeftHandSideExpression_Yield `in` Expression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` LeftHandSideExpression_Await `in` Expression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` LeftHandSideExpression_Yield_Await `in` Expression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` `var` ForBinding `in` Expression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` `var` ForBinding_Yield `in` Expression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` `var` ForBinding_Await `in` Expression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` `var` ForBinding_Yield_Await `in` Expression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` `var` ForBinding `in` Expression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` `var` ForBinding_Yield `in` Expression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` `var` ForBinding_Await `in` Expression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` `var` ForBinding_Yield_Await `in` Expression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` ForDeclaration `in` Expression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` ForDeclaration_Yield `in` Expression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` ForDeclaration_Await `in` Expression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` ForDeclaration_Yield_Await `in` Expression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` ForDeclaration `in` Expression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` ForDeclaration_Yield `in` Expression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` ForDeclaration_Await `in` Expression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `in` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` ForDeclaration_Yield_Await `in` Expression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` LeftHandSideExpression `of` AssignmentExpression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` LeftHandSideExpression_Yield `of` AssignmentExpression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` LeftHandSideExpression_Await `of` AssignmentExpression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` LeftHandSideExpression_Yield_Await `of` AssignmentExpression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` LeftHandSideExpression `of` AssignmentExpression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` LeftHandSideExpression_Yield `of` AssignmentExpression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` LeftHandSideExpression_Await `of` AssignmentExpression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(`   LeftHandSideExpression[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` LeftHandSideExpression_Yield_Await `of` AssignmentExpression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` `var` ForBinding `of` AssignmentExpression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` `var` ForBinding_Yield `of` AssignmentExpression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` `var` ForBinding_Await `of` AssignmentExpression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` `var` ForBinding_Yield_Await `of` AssignmentExpression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` `var` ForBinding `of` AssignmentExpression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` `var` ForBinding_Yield `of` AssignmentExpression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` `var` ForBinding_Await `of` AssignmentExpression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` `var` ForBinding[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` `var` ForBinding_Yield_Await `of` AssignmentExpression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement : `for` `(` ForDeclaration `of` AssignmentExpression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield : `for` `(` ForDeclaration_Yield `of` AssignmentExpression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `(` ForDeclaration_Await `of` AssignmentExpression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `(` ForDeclaration_Yield_Await `of` AssignmentExpression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Return : `for` `(` ForDeclaration `of` AssignmentExpression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Return : `for` `(` ForDeclaration_Yield `of` AssignmentExpression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `(` ForDeclaration_Await `of` AssignmentExpression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : `for` `(` ForDeclaration[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `(` ForDeclaration_Yield_Await `of` AssignmentExpression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : [+Await] `for` `await` `(`   LeftHandSideExpression[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `await` `(` LeftHandSideExpression_Await `of` AssignmentExpression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : [+Await] `for` `await` `(`   LeftHandSideExpression[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `await` `(` LeftHandSideExpression_Yield_Await `of` AssignmentExpression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : [+Await] `for` `await` `(`   LeftHandSideExpression[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `await` `(` LeftHandSideExpression_Await `of` AssignmentExpression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : [+Await] `for` `await` `(`   LeftHandSideExpression[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `await` `(` LeftHandSideExpression_Yield_Await `of` AssignmentExpression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : [+Await] `for` `await` `(` `var` ForBinding[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `await` `(` `var` ForBinding_Await `of` AssignmentExpression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : [+Await] `for` `await` `(` `var` ForBinding[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `await` `(` `var` ForBinding_Yield_Await `of` AssignmentExpression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : [+Await] `for` `await` `(` `var` ForBinding[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `await` `(` `var` ForBinding_Await `of` AssignmentExpression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : [+Await] `for` `await` `(` `var` ForBinding[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `await` `(` `var` ForBinding_Yield_Await `of` AssignmentExpression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : [+Await] `for` `await` `(` ForDeclaration[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await : `for` `await` `(` ForDeclaration_Await `of` AssignmentExpression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : [+Await] `for` `await` `(` ForDeclaration[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await : `for` `await` `(` ForDeclaration_Yield_Await `of` AssignmentExpression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : [+Await] `for` `await` `(` ForDeclaration[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Await_Return : `for` `await` `(` ForDeclaration_Await `of` AssignmentExpression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#IterationStatement[Yield, Await, Return]  : [+Await] `for` `await` `(` ForDeclaration[?Yield, ?Await] `of` AssignmentExpression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('IterationStatement_Yield_Await_Return : `for` `await` `(` ForDeclaration_Yield_Await `of` AssignmentExpression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ForDeclaration[Yield, Await]  : LetOrConst ForBinding[?Yield, ?Await]
@builder.build('ForDeclaration : LetOrConst ForBinding')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ForDeclaration[Yield, Await]  : LetOrConst ForBinding[?Yield, ?Await]
@builder.build('ForDeclaration_Yield : LetOrConst ForBinding_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ForDeclaration[Yield, Await]  : LetOrConst ForBinding[?Yield, ?Await]
@builder.build('ForDeclaration_Await : LetOrConst ForBinding_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ForDeclaration[Yield, Await]  : LetOrConst ForBinding[?Yield, ?Await]
@builder.build('ForDeclaration_Yield_Await : LetOrConst ForBinding_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ForBinding[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
@builder.build('ForBinding : BindingIdentifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ForBinding[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
@builder.build('ForBinding_Yield : BindingIdentifier_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ForBinding[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
@builder.build('ForBinding_Await : BindingIdentifier_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ForBinding[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
@builder.build('ForBinding_Yield_Await : BindingIdentifier_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ForBinding[Yield, Await]  : BindingPattern[?Yield, ?Await]
@builder.build('ForBinding : BindingPattern')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ForBinding[Yield, Await]  : BindingPattern[?Yield, ?Await]
@builder.build('ForBinding_Yield : BindingPattern_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ForBinding[Yield, Await]  : BindingPattern[?Yield, ?Await]
@builder.build('ForBinding_Await : BindingPattern_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ForBinding[Yield, Await]  : BindingPattern[?Yield, ?Await]
@builder.build('ForBinding_Yield_Await : BindingPattern_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ContinueStatement[Yield, Await]  : `continue` `;`
@builder.build('ContinueStatement : `continue` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ContinueStatement[Yield, Await]  : `continue` `;`
@builder.build('ContinueStatement_Yield : `continue` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ContinueStatement[Yield, Await]  : `continue` `;`
@builder.build('ContinueStatement_Await : `continue` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ContinueStatement[Yield, Await]  : `continue` `;`
@builder.build('ContinueStatement_Yield_Await : `continue` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ContinueStatement[Yield, Await]  : `continue`  LabelIdentifier[?Yield, ?Await] `;`
@builder.build('ContinueStatement : `continue` LabelIdentifier `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ContinueStatement[Yield, Await]  : `continue`  LabelIdentifier[?Yield, ?Await] `;`
@builder.build('ContinueStatement_Yield : `continue` LabelIdentifier_Yield `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ContinueStatement[Yield, Await]  : `continue`  LabelIdentifier[?Yield, ?Await] `;`
@builder.build('ContinueStatement_Await : `continue` LabelIdentifier_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ContinueStatement[Yield, Await]  : `continue`  LabelIdentifier[?Yield, ?Await] `;`
@builder.build('ContinueStatement_Yield_Await : `continue` LabelIdentifier_Yield_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakStatement[Yield, Await]  : `break` `;`
@builder.build('BreakStatement : `break` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakStatement[Yield, Await]  : `break` `;`
@builder.build('BreakStatement_Yield : `break` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakStatement[Yield, Await]  : `break` `;`
@builder.build('BreakStatement_Await : `break` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakStatement[Yield, Await]  : `break` `;`
@builder.build('BreakStatement_Yield_Await : `break` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakStatement[Yield, Await]  : `break`  LabelIdentifier[?Yield, ?Await] `;`
@builder.build('BreakStatement : `break` LabelIdentifier `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakStatement[Yield, Await]  : `break`  LabelIdentifier[?Yield, ?Await] `;`
@builder.build('BreakStatement_Yield : `break` LabelIdentifier_Yield `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakStatement[Yield, Await]  : `break`  LabelIdentifier[?Yield, ?Await] `;`
@builder.build('BreakStatement_Await : `break` LabelIdentifier_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#BreakStatement[Yield, Await]  : `break`  LabelIdentifier[?Yield, ?Await] `;`
@builder.build('BreakStatement_Yield_Await : `break` LabelIdentifier_Yield_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ReturnStatement[Yield, Await]  : `return` `;`
@builder.build('ReturnStatement : `return` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ReturnStatement[Yield, Await]  : `return` `;`
@builder.build('ReturnStatement_Yield : `return` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ReturnStatement[Yield, Await]  : `return` `;`
@builder.build('ReturnStatement_Await : `return` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ReturnStatement[Yield, Await]  : `return` `;`
@builder.build('ReturnStatement_Yield_Await : `return` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ReturnStatement[Yield, Await]  : `return`  Expression[+In, ?Yield, ?Await] `;`
@builder.build('ReturnStatement : `return` Expression_In `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ReturnStatement[Yield, Await]  : `return`  Expression[+In, ?Yield, ?Await] `;`
@builder.build('ReturnStatement_Yield : `return` Expression_In_Yield `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ReturnStatement[Yield, Await]  : `return`  Expression[+In, ?Yield, ?Await] `;`
@builder.build('ReturnStatement_Await : `return` Expression_In_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ReturnStatement[Yield, Await]  : `return`  Expression[+In, ?Yield, ?Await] `;`
@builder.build('ReturnStatement_Yield_Await : `return` Expression_In_Yield_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#WithStatement[Yield, Await, Return]  : `with` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('WithStatement : `with` `(` Expression_In `)` Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#WithStatement[Yield, Await, Return]  : `with` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('WithStatement_Yield : `with` `(` Expression_In_Yield `)` Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#WithStatement[Yield, Await, Return]  : `with` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('WithStatement_Await : `with` `(` Expression_In_Await `)` Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#WithStatement[Yield, Await, Return]  : `with` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('WithStatement_Yield_Await : `with` `(` Expression_In_Yield_Await `)` Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#WithStatement[Yield, Await, Return]  : `with` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('WithStatement_Return : `with` `(` Expression_In `)` Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#WithStatement[Yield, Await, Return]  : `with` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('WithStatement_Yield_Return : `with` `(` Expression_In_Yield `)` Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#WithStatement[Yield, Await, Return]  : `with` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('WithStatement_Await_Return : `with` `(` Expression_In_Await `)` Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#WithStatement[Yield, Await, Return]  : `with` `(` Expression[+In, ?Yield, ?Await] `)` Statement[?Yield, ?Await, ?Return]
@builder.build('WithStatement_Yield_Await_Return : `with` `(` Expression_In_Yield_Await `)` Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SwitchStatement[Yield, Await, Return]  : `switch` `(` Expression[+In, ?Yield, ?Await] `)` CaseBlock[?Yield, ?Await, ?Return]
@builder.build('SwitchStatement : `switch` `(` Expression_In `)` CaseBlock')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SwitchStatement[Yield, Await, Return]  : `switch` `(` Expression[+In, ?Yield, ?Await] `)` CaseBlock[?Yield, ?Await, ?Return]
@builder.build('SwitchStatement_Yield : `switch` `(` Expression_In_Yield `)` CaseBlock_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SwitchStatement[Yield, Await, Return]  : `switch` `(` Expression[+In, ?Yield, ?Await] `)` CaseBlock[?Yield, ?Await, ?Return]
@builder.build('SwitchStatement_Await : `switch` `(` Expression_In_Await `)` CaseBlock_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SwitchStatement[Yield, Await, Return]  : `switch` `(` Expression[+In, ?Yield, ?Await] `)` CaseBlock[?Yield, ?Await, ?Return]
@builder.build('SwitchStatement_Yield_Await : `switch` `(` Expression_In_Yield_Await `)` CaseBlock_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SwitchStatement[Yield, Await, Return]  : `switch` `(` Expression[+In, ?Yield, ?Await] `)` CaseBlock[?Yield, ?Await, ?Return]
@builder.build('SwitchStatement_Return : `switch` `(` Expression_In `)` CaseBlock_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SwitchStatement[Yield, Await, Return]  : `switch` `(` Expression[+In, ?Yield, ?Await] `)` CaseBlock[?Yield, ?Await, ?Return]
@builder.build('SwitchStatement_Yield_Return : `switch` `(` Expression_In_Yield `)` CaseBlock_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SwitchStatement[Yield, Await, Return]  : `switch` `(` Expression[+In, ?Yield, ?Await] `)` CaseBlock[?Yield, ?Await, ?Return]
@builder.build('SwitchStatement_Await_Return : `switch` `(` Expression_In_Await `)` CaseBlock_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#SwitchStatement[Yield, Await, Return]  : `switch` `(` Expression[+In, ?Yield, ?Await] `)` CaseBlock[?Yield, ?Await, ?Return]
@builder.build('SwitchStatement_Yield_Await_Return : `switch` `(` Expression_In_Yield_Await `)` CaseBlock_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock : `{` CaseClauses `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield : `{` CaseClauses_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Await : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Await : `{` CaseClauses_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Await : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Await : `{` CaseClauses_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Return : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Return : `{` CaseClauses_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Return : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Return : `{` CaseClauses_Yield_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Await_Return : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Await_Return : `{` CaseClauses_Await_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Await_Return : `{` `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Await_Return : `{` CaseClauses_Yield_Await_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock : `{` DefaultClause `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock : `{` DefaultClause CaseClauses `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock : `{` CaseClauses DefaultClause `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock : `{` CaseClauses DefaultClause CaseClauses `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield : `{` DefaultClause_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield : `{` DefaultClause_Yield CaseClauses_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield : `{` CaseClauses_Yield DefaultClause_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield : `{` CaseClauses_Yield DefaultClause_Yield CaseClauses_Yield `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Await : `{` DefaultClause_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Await : `{` DefaultClause_Await CaseClauses_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Await : `{` CaseClauses_Await DefaultClause_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Await : `{` CaseClauses_Await DefaultClause_Await CaseClauses_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Await : `{` DefaultClause_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Await : `{` DefaultClause_Yield_Await CaseClauses_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Await : `{` CaseClauses_Yield_Await DefaultClause_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Await : `{` CaseClauses_Yield_Await DefaultClause_Yield_Await CaseClauses_Yield_Await `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Return : `{` DefaultClause_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Return : `{` DefaultClause_Return CaseClauses_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Return : `{` CaseClauses_Return DefaultClause_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Return : `{` CaseClauses_Return DefaultClause_Return CaseClauses_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Return : `{` DefaultClause_Yield_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Return : `{` DefaultClause_Yield_Return CaseClauses_Yield_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Return : `{` CaseClauses_Yield_Return DefaultClause_Yield_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Return : `{` CaseClauses_Yield_Return DefaultClause_Yield_Return CaseClauses_Yield_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Await_Return : `{` DefaultClause_Await_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Await_Return : `{` DefaultClause_Await_Return CaseClauses_Await_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Await_Return : `{` CaseClauses_Await_Return DefaultClause_Await_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Await_Return : `{` CaseClauses_Await_Return DefaultClause_Await_Return CaseClauses_Await_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Await_Return : `{` DefaultClause_Yield_Await_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Await_Return : `{` DefaultClause_Yield_Await_Return CaseClauses_Yield_Await_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Await_Return : `{` CaseClauses_Yield_Await_Return DefaultClause_Yield_Await_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseBlock[Yield, Await, Return]  : `{` CaseClauses[?Yield, ?Await, ?Return]? DefaultClause[?Yield, ?Await, ?Return] CaseClauses[?Yield, ?Await, ?Return]? `}`
@builder.build('CaseBlock_Yield_Await_Return : `{` CaseClauses_Yield_Await_Return DefaultClause_Yield_Await_Return CaseClauses_Yield_Await_Return `}`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses : CaseClause')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses_Yield : CaseClause_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses_Await : CaseClause_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses_Yield_Await : CaseClause_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses_Return : CaseClause_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses_Yield_Return : CaseClause_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses_Await_Return : CaseClause_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses_Yield_Await_Return : CaseClause_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClauses[?Yield, ?Await, ?Return] CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses : CaseClauses CaseClause')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClauses[?Yield, ?Await, ?Return] CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses_Yield : CaseClauses_Yield CaseClause_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClauses[?Yield, ?Await, ?Return] CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses_Await : CaseClauses_Await CaseClause_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClauses[?Yield, ?Await, ?Return] CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses_Yield_Await : CaseClauses_Yield_Await CaseClause_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClauses[?Yield, ?Await, ?Return] CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses_Return : CaseClauses_Return CaseClause_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClauses[?Yield, ?Await, ?Return] CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses_Yield_Return : CaseClauses_Yield_Return CaseClause_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClauses[?Yield, ?Await, ?Return] CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses_Await_Return : CaseClauses_Await_Return CaseClause_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClauses[Yield, Await, Return]  : CaseClauses[?Yield, ?Await, ?Return] CaseClause[?Yield, ?Await, ?Return]
@builder.build('CaseClauses_Yield_Await_Return : CaseClauses_Yield_Await_Return CaseClause_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause : `case` Expression_In `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause : `case` Expression_In `:` StatementList')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause_Yield : `case` Expression_In_Yield `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause_Yield : `case` Expression_In_Yield `:` StatementList_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause_Await : `case` Expression_In_Await `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause_Await : `case` Expression_In_Await `:` StatementList_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause_Yield_Await : `case` Expression_In_Yield_Await `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause_Yield_Await : `case` Expression_In_Yield_Await `:` StatementList_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause_Return : `case` Expression_In `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause_Return : `case` Expression_In `:` StatementList_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause_Yield_Return : `case` Expression_In_Yield `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause_Yield_Return : `case` Expression_In_Yield `:` StatementList_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause_Await_Return : `case` Expression_In_Await `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause_Await_Return : `case` Expression_In_Await `:` StatementList_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause_Yield_Await_Return : `case` Expression_In_Yield_Await `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CaseClause[Yield, Await, Return]  : `case` Expression[+In, ?Yield, ?Await] `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('CaseClause_Yield_Await_Return : `case` Expression_In_Yield_Await `:` StatementList_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause : `default` `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause : `default` `:` StatementList')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause_Yield : `default` `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause_Yield : `default` `:` StatementList_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause_Await : `default` `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause_Await : `default` `:` StatementList_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause_Yield_Await : `default` `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause_Yield_Await : `default` `:` StatementList_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause_Return : `default` `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause_Return : `default` `:` StatementList_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause_Yield_Return : `default` `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause_Yield_Return : `default` `:` StatementList_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause_Await_Return : `default` `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause_Await_Return : `default` `:` StatementList_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause_Yield_Await_Return : `default` `:`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DefaultClause[Yield, Await, Return]  : `default` `:` StatementList[?Yield, ?Await, ?Return]?
@builder.build('DefaultClause_Yield_Await_Return : `default` `:` StatementList_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledStatement[Yield, Await, Return]  : LabelIdentifier[?Yield, ?Await] `:` LabelledItem[?Yield, ?Await, ?Return]
@builder.build('LabelledStatement : LabelIdentifier `:` LabelledItem')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledStatement[Yield, Await, Return]  : LabelIdentifier[?Yield, ?Await] `:` LabelledItem[?Yield, ?Await, ?Return]
@builder.build('LabelledStatement_Yield : LabelIdentifier_Yield `:` LabelledItem_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledStatement[Yield, Await, Return]  : LabelIdentifier[?Yield, ?Await] `:` LabelledItem[?Yield, ?Await, ?Return]
@builder.build('LabelledStatement_Await : LabelIdentifier_Await `:` LabelledItem_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledStatement[Yield, Await, Return]  : LabelIdentifier[?Yield, ?Await] `:` LabelledItem[?Yield, ?Await, ?Return]
@builder.build('LabelledStatement_Yield_Await : LabelIdentifier_Yield_Await `:` LabelledItem_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledStatement[Yield, Await, Return]  : LabelIdentifier[?Yield, ?Await] `:` LabelledItem[?Yield, ?Await, ?Return]
@builder.build('LabelledStatement_Return : LabelIdentifier `:` LabelledItem_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledStatement[Yield, Await, Return]  : LabelIdentifier[?Yield, ?Await] `:` LabelledItem[?Yield, ?Await, ?Return]
@builder.build('LabelledStatement_Yield_Return : LabelIdentifier_Yield `:` LabelledItem_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledStatement[Yield, Await, Return]  : LabelIdentifier[?Yield, ?Await] `:` LabelledItem[?Yield, ?Await, ?Return]
@builder.build('LabelledStatement_Await_Return : LabelIdentifier_Await `:` LabelledItem_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledStatement[Yield, Await, Return]  : LabelIdentifier[?Yield, ?Await] `:` LabelledItem[?Yield, ?Await, ?Return]
@builder.build('LabelledStatement_Yield_Await_Return : LabelIdentifier_Yield_Await `:` LabelledItem_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('LabelledItem : Statement')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('LabelledItem_Yield : Statement_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('LabelledItem_Await : Statement_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('LabelledItem_Yield_Await : Statement_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('LabelledItem_Return : Statement_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('LabelledItem_Yield_Return : Statement_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('LabelledItem_Await_Return : Statement_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : Statement[?Yield, ?Await, ?Return]
@builder.build('LabelledItem_Yield_Await_Return : Statement_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : FunctionDeclaration[?Yield, ?Await, ~Default]
@builder.build('LabelledItem : FunctionDeclaration')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : FunctionDeclaration[?Yield, ?Await, ~Default]
@builder.build('LabelledItem_Yield : FunctionDeclaration_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : FunctionDeclaration[?Yield, ?Await, ~Default]
@builder.build('LabelledItem_Await : FunctionDeclaration_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : FunctionDeclaration[?Yield, ?Await, ~Default]
@builder.build('LabelledItem_Yield_Await : FunctionDeclaration_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : FunctionDeclaration[?Yield, ?Await, ~Default]
@builder.build('LabelledItem_Return : FunctionDeclaration')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : FunctionDeclaration[?Yield, ?Await, ~Default]
@builder.build('LabelledItem_Yield_Return : FunctionDeclaration_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : FunctionDeclaration[?Yield, ?Await, ~Default]
@builder.build('LabelledItem_Await_Return : FunctionDeclaration_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#LabelledItem[Yield, Await, Return]  : FunctionDeclaration[?Yield, ?Await, ~Default]
@builder.build('LabelledItem_Yield_Await_Return : FunctionDeclaration_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ThrowStatement[Yield, Await]  : `throw`  Expression[+In, ?Yield, ?Await] `;`
@builder.build('ThrowStatement : `throw` Expression_In `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ThrowStatement[Yield, Await]  : `throw`  Expression[+In, ?Yield, ?Await] `;`
@builder.build('ThrowStatement_Yield : `throw` Expression_In_Yield `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ThrowStatement[Yield, Await]  : `throw`  Expression[+In, ?Yield, ?Await] `;`
@builder.build('ThrowStatement_Await : `throw` Expression_In_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#ThrowStatement[Yield, Await]  : `throw`  Expression[+In, ?Yield, ?Await] `;`
@builder.build('ThrowStatement_Yield_Await : `throw` Expression_In_Yield_Await `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return]
@builder.build('TryStatement : `try` Block Catch')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Yield : `try` Block_Yield Catch_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Await : `try` Block_Await Catch_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Yield_Await : `try` Block_Yield_Await Catch_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Return : `try` Block_Return Catch_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Yield_Return : `try` Block_Yield_Return Catch_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Await_Return : `try` Block_Await_Return Catch_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Yield_Await_Return : `try` Block_Yield_Await_Return Catch_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement : `try` Block Finally')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Yield : `try` Block_Yield Finally_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Await : `try` Block_Await Finally_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Yield_Await : `try` Block_Yield_Await Finally_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Return : `try` Block_Return Finally_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Yield_Return : `try` Block_Yield_Return Finally_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Await_Return : `try` Block_Await_Return Finally_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Yield_Await_Return : `try` Block_Yield_Await_Return Finally_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement : `try` Block Catch Finally')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Yield : `try` Block_Yield Catch_Yield Finally_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Await : `try` Block_Await Catch_Await Finally_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Yield_Await : `try` Block_Yield_Await Catch_Yield_Await Finally_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Return : `try` Block_Return Catch_Return Finally_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Yield_Return : `try` Block_Yield_Return Catch_Yield_Return Finally_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Await_Return : `try` Block_Await_Return Catch_Await_Return Finally_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#TryStatement[Yield, Await, Return]  : `try` Block[?Yield, ?Await, ?Return] Catch[?Yield, ?Await, ?Return] Finally[?Yield, ?Await, ?Return]
@builder.build('TryStatement_Yield_Await_Return : `try` Block_Yield_Await_Return Catch_Yield_Await_Return Finally_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` `(` CatchParameter[?Yield, ?Await] `)` Block[?Yield, ?Await, ?Return]
@builder.build('Catch : `catch` `(` CatchParameter `)` Block')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` `(` CatchParameter[?Yield, ?Await] `)` Block[?Yield, ?Await, ?Return]
@builder.build('Catch_Yield : `catch` `(` CatchParameter_Yield `)` Block_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` `(` CatchParameter[?Yield, ?Await] `)` Block[?Yield, ?Await, ?Return]
@builder.build('Catch_Await : `catch` `(` CatchParameter_Await `)` Block_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` `(` CatchParameter[?Yield, ?Await] `)` Block[?Yield, ?Await, ?Return]
@builder.build('Catch_Yield_Await : `catch` `(` CatchParameter_Yield_Await `)` Block_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` `(` CatchParameter[?Yield, ?Await] `)` Block[?Yield, ?Await, ?Return]
@builder.build('Catch_Return : `catch` `(` CatchParameter `)` Block_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` `(` CatchParameter[?Yield, ?Await] `)` Block[?Yield, ?Await, ?Return]
@builder.build('Catch_Yield_Return : `catch` `(` CatchParameter_Yield `)` Block_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` `(` CatchParameter[?Yield, ?Await] `)` Block[?Yield, ?Await, ?Return]
@builder.build('Catch_Await_Return : `catch` `(` CatchParameter_Await `)` Block_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` `(` CatchParameter[?Yield, ?Await] `)` Block[?Yield, ?Await, ?Return]
@builder.build('Catch_Yield_Await_Return : `catch` `(` CatchParameter_Yield_Await `)` Block_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` Block[?Yield, ?Await, ?Return]
@builder.build('Catch : `catch` Block')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` Block[?Yield, ?Await, ?Return]
@builder.build('Catch_Yield : `catch` Block_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` Block[?Yield, ?Await, ?Return]
@builder.build('Catch_Await : `catch` Block_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` Block[?Yield, ?Await, ?Return]
@builder.build('Catch_Yield_Await : `catch` Block_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` Block[?Yield, ?Await, ?Return]
@builder.build('Catch_Return : `catch` Block_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` Block[?Yield, ?Await, ?Return]
@builder.build('Catch_Yield_Return : `catch` Block_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` Block[?Yield, ?Await, ?Return]
@builder.build('Catch_Await_Return : `catch` Block_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Catch[Yield, Await, Return]  : `catch` Block[?Yield, ?Await, ?Return]
@builder.build('Catch_Yield_Await_Return : `catch` Block_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Finally[Yield, Await, Return]  : `finally` Block[?Yield, ?Await, ?Return]
@builder.build('Finally : `finally` Block')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Finally[Yield, Await, Return]  : `finally` Block[?Yield, ?Await, ?Return]
@builder.build('Finally_Yield : `finally` Block_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Finally[Yield, Await, Return]  : `finally` Block[?Yield, ?Await, ?Return]
@builder.build('Finally_Await : `finally` Block_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Finally[Yield, Await, Return]  : `finally` Block[?Yield, ?Await, ?Return]
@builder.build('Finally_Yield_Await : `finally` Block_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Finally[Yield, Await, Return]  : `finally` Block[?Yield, ?Await, ?Return]
@builder.build('Finally_Return : `finally` Block_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Finally[Yield, Await, Return]  : `finally` Block[?Yield, ?Await, ?Return]
@builder.build('Finally_Yield_Return : `finally` Block_Yield_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Finally[Yield, Await, Return]  : `finally` Block[?Yield, ?Await, ?Return]
@builder.build('Finally_Await_Return : `finally` Block_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#Finally[Yield, Await, Return]  : `finally` Block[?Yield, ?Await, ?Return]
@builder.build('Finally_Yield_Await_Return : `finally` Block_Yield_Await_Return')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CatchParameter[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
@builder.build('CatchParameter : BindingIdentifier')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CatchParameter[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
@builder.build('CatchParameter_Yield : BindingIdentifier_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CatchParameter[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
@builder.build('CatchParameter_Await : BindingIdentifier_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CatchParameter[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
@builder.build('CatchParameter_Yield_Await : BindingIdentifier_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CatchParameter[Yield, Await]  : BindingPattern[?Yield, ?Await]
@builder.build('CatchParameter : BindingPattern')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CatchParameter[Yield, Await]  : BindingPattern[?Yield, ?Await]
@builder.build('CatchParameter_Yield : BindingPattern_Yield')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CatchParameter[Yield, Await]  : BindingPattern[?Yield, ?Await]
@builder.build('CatchParameter_Await : BindingPattern_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#CatchParameter[Yield, Await]  : BindingPattern[?Yield, ?Await]
@builder.build('CatchParameter_Yield_Await : BindingPattern_Yield_Await')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

#DebuggerStatement  : `debugger` `;`
@builder.build('DebuggerStatement : `debugger` `;`')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }): pass

