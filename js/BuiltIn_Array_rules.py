from language import Builder
from language import Stage
from language import State
builder = Builder.get_builder()

#ArrayLiteral[Yield, Await]  : `[` Elision? `]`
#@builder.build('ArrayLiteral : ``')
def _(context, ruler, stage=Stage.Prepare, target='', storage={ }):
		o = {
			'text': '[1,2,3,4]',
			'type': 'Array',
			'properties': []
		}
		return o