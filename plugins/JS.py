from utils import Randomer

def RndJSNumber():
	return Randomer.rnd(-10, 10)

class JSRegexMaker(object):
	"""docstring for JSRegexMaker"""
	def __init__(self):
		self.debug = True
		self.ruleExpandStack = []
		self.rule = {}
		self.rule['Pattern'] = Randomer.weighted([
			{'w': 0.1, 'v': lambda: self.make('Disjunction')},
			])
		self.rule['Disjunction'] = Randomer.weighted([
			{'w': 0.5, 'v': lambda: self.make('Alternative')},
			{'w': 0.1, 'v': lambda: self.make('Alternative') + '|' + self.make('Disjunction')}
			])
		self.rule['Alternative'] = Randomer.weighted([
			{'w': 0.1, 'v': lambda: '' },
			{'w': 0.3, 'v': lambda: self.make('Alternative') + self.make('Term')},
			])
		self.rule['Term'] = Randomer.weighted([
			{'w': 0.1, 'v': lambda: self.make('Assertion')},
			{'w': 0.3, 'v': lambda: self.make('Atom')},
			{'w': 0.3, 'v': lambda: self.make('Atom') + self.make('Quantifier')},
			])
		self.rule['Assertion'] = ['^', '$', '\\b', '\\B',
			lambda: '(?='+self.make('Alternative')+')',
			lambda: '(?!'+self.make('Alternative')+')',
			lambda: '(?<='+self.make('Alternative')+')',
			lambda: '(?<!'+self.make('Alternative')+')',
			]
		self.rule['Quantifier'] = [
			lambda: self.make('QuantifierPrefix'),
			lambda: self.make('QuantifierPrefix')+'?',
			]
		self.rule['QuantifierPrefix'] = ['*', '+', '?',
			lambda: '{'+self.make('DecimalDigits')+'}',
			lambda: '{'+self.make('DecimalDigits')+',}',
			self.make_Ordered_QuantifierPrefix, #lambda: '{'+self.make('DecimalDigits')+','+self.make('DecimalDigits')+'}',
			]
		self.rule['Atom'] = Randomer.weighted([
			{'w': 0.3, 'v': lambda: self.make('PatternCharacter')},
			{'w': 0.3, 'v': lambda: '.'},
			{'w': 0.3, 'v': lambda: '\\'+self.make('AtomEscape')+'}'},
			{'w': 0.3, 'v': lambda: self.make('CharacterClass')},
			{'w': 0.1, 'v': lambda: '('+self.make('GroupSpecifier')+self.make('Disjunction')+')'},
			{'w': 0.1, 'v': lambda: '(?:'+self.make('Disjunction')+')'},
			])
		self.rule['SyntaxCharacter'] = [ '^', '$', '\\', '.', '*', '+', '?', '(', ')', '[', ']', '{', '}', '|']
		self.rule['PatternCharacter'] = [
			lambda: self.makeSourceCharacter(exclude=self.rule['SyntaxCharacter']), #SourceCharacter but not SyntaxCharacter
			]
		self.rule['AtomEscape'] = [
			lambda: self.make('DecimalEscape'),
			lambda: self.make('CharacterClassEscape'),
			lambda: self.make('CharacterEscape'),
			lambda: 'k'+self.make('GroupName'),
			]
		self.rule['CharacterEscape'] = [
			lambda: self.make('ControlEscape'),
			lambda: 'c'+self.make('ControlLetter'),
			'0',#0[lookahead ∉ DecimalDigit]
			lambda: self.make('HexEscapeSequence'),
			lambda: self.make('RegExpUnicodeEscapeSequence'),
			lambda: self.make('IdentityEscape'),
			]
		self.rule['ControlEscape'] = ['f', 'n', 'r', 't', 'v']
		self.rule['ControlLetter'] = [
			lambda: Randomer.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
			]
		self.rule['GroupSpecifier'] = [
			'',
			lambda: '?'+self.make('GroupName'),
			]
		self.rule['GroupName'] = [
			lambda: '<'+self.make('RegExpIdentifierName')+'>',
			]
		self.rule['RegExpIdentifierName'] = Randomer.weighted([
			{'w': 0.3, 'v': lambda: self.make('RegExpIdentifierStart')},
			{'w': 0.1, 'v': lambda: self.make('RegExpIdentifierName') + self.make('RegExpIdentifierPart')},
			])
		self.rule['RegExpIdentifierStart'] = [
			#lambda: self.make('UnicodeIDStart'),
			'$',
			'_',
			lambda: '\\'+self.make('RegExpUnicodeEscapeSequence')
			]
		self.rule['RegExpIdentifierPart'] = [
			#lambda: self.make('UnicodeIDStart'),
			'$',
			lambda: '\\'+self.make('RegExpUnicodeEscapeSequence'),
			'<ZWNJ> <ZWJ>'
			]
		self.rule['RegExpUnicodeEscapeSequence'] = [
			lambda: 'u'+self.make('LeadSurrogate')+'\\u'+self.make('TrailSurrogate'),
			lambda: 'u'+self.make('LeadSurrogate'),
			lambda: 'u'+self.make('TrailSurrogate'),
			lambda: 'u'+self.make('NonSurrogate'),
			lambda: 'u'+self.makeHex4Digits(),
			lambda: 'u{'+self.make('CodePoint')+'}',
			]
		self.rule['LeadSurrogate'] = [
			lambda: self.makeHex4Digits(start=0xD800, end=0xDBFF),
			]
		self.rule['TrailSurrogate'] = [
			lambda: self.makeHex4Digits(start=0xDC00, end=0xDFFF),
			]
		self.rule['NonSurrogate'] = [
			#
			#Hex4Digits but only if the SV of Hex4Digits is not in the inclusive range 0xD800 to 0xDFFF
			#
			lambda: self.makeHex4Digits(start=0x0000, end=0xD800),
			lambda: self.makeHex4Digits(start=0xDFFF, end=0xFFFF),
			]
		self.rule['IdentityEscape'] = [
			lambda: self.make('SyntaxCharacter'),
			#'/',
			lambda: self.makeSourceCharacter(exclude=None), #SourceCharacter but not UnicodeIDContinue
			]
		self.rule['DecimalEscape'] = [
			#NonZeroDigit DecimalDigits [lookahead ∉ DecimalDigit]
			lambda: self.make('NonZeroDigit') + self.make('DecimalDigits'),
			]
		self.rule['CharacterClassEscape'] = [
			'd', 'D', 's', 'S', 'w', 'W',
			#[+U]p{UnicodePropertyValueExpression}
			#[+U]P{UnicodePropertyValueExpression}
			]
		self.rule['CharacterClass'] = [
			#
			#[[lookahead ∉ { ^ }]ClassRanges[?U]]
			#[^ClassRanges[?U]]
			#
			lambda: '['+self.make('ClassRanges')+']',
			lambda: '[^'+self.make('ClassRanges')+']',
			]
		self.rule['ClassRanges'] = [
			'',
			lambda: self.make('NonemptyClassRanges'),
			]
		self.rule['NonemptyClassRanges'] = [
			lambda: self.make('ClassAtom'),
			lambda: self.make('ClassAtom')+self.make('NonemptyClassRangesNoDash'),
			#lambda: self.make('ClassAtom')+'-'+self.make('ClassAtom')+self.make('ClassRanges'),
			self.make_Ordered_NonemptyClassRanges, # fix 'Range out of order in character class' error
			]
		self.rule['NonemptyClassRangesNoDash'] = [
			lambda: self.make('ClassAtom'),
			lambda: self.make('ClassAtomNoDash')+self.make('NonemptyClassRangesNoDash'),
			#lambda: self.make('ClassAtomNoDash')+'-'+self.make('ClassAtom')+self.make('ClassRanges'),
			self.make_Ordered_NonemptyClassRangesNoDash, # fix 'Range out of order in character class' error
			]
		self.rule['ClassAtom'] = [
			'-',
			lambda: self.make('ClassAtomNoDash'),
			]
		self.rule['ClassAtomNoDash'] = [
			lambda: self.makeSourceCharacter(exclude=['\\', ']', '-']), #SourceCharacter but not one of \ or ] or -
			lambda: '\\'+self.make('ClassEscape'),
			]
		self.rule['ClassEscape'] = [
			'b',
			'-',
			lambda: self.make('CharacterClassEscape'),
			lambda: self.make('CharacterEscape'),
			]

		####
		self.rule['DecimalDigits'] = Randomer.weighted([
			{'w': 0.1, 'v': lambda: self.make('DecimalDigit')},
			{'w': 0.1, 'v': lambda: self.make('DecimalDigits')+self.make('DecimalDigit')},
			])
		self.rule['DecimalDigits'] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		self.rule['NonZeroDigit'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
		self.rule['HexEscapeSequence'] = [
			lambda: 'x'+self.make('HexDigit')+self.make('HexDigit'),
			]
		self.rule['HexDigits'] = Randomer.weighted([
			{'w': 0.1, 'v': lambda: self.make('HexDigit')},
			{'w': 0.1, 'v': lambda: self.make('HexDigits')+self.make('HexDigit')},
			])
		self.rule['HexDigit'] = [
			lambda: '%x' % Randomer.rnd(0, 16)
		]
		self.rule['CodePoint'] = [
			lambda: '%x' % Randomer.rnd(0, 16)
		]

	def make_Ordered_QuantifierPrefix(self):
		#fix js the error if {a,b} and b<a
		s = Randomer.rnd(0,5)
		e = Randomer.rnd(s,10)
		return '{%d,%d}' % (s, e)

	def make_Ordered_NonemptyClassRanges(self):
		# fix 'Range out of order in character class' error
		s = Randomer.rnd(0, 255)
		e = Randomer.rnd(s, 256)
		s = 11 if s in [10, 13] else s
		e = 12 if e in [10, 13] else e
		return '%s-%s%s' % (chr(s), chr(e), self.make('ClassRanges'))

	def make_Ordered_NonemptyClassRangesNoDash(self):
		# fix 'Range out of order in character class' error
		s = Randomer.rnd(0, 255)
		if s == ord('-'):
			s += 1
		e = Randomer.rnd(s, 256)
		s = 11 if s in [10, 13] else s
		e = 12 if e in [10, 13] else e
		return '%s-%s%s' % (chr(s), chr(e), self.make('ClassRanges'))

	def makeSourceCharacter(self, exclude=None):
		c = Randomer.rnd(0, 256)
		while exclude and chr(c) in exclude:
			c = Randomer.rnd(0, 256)
		c = 12 if c in [10, 13] else c
		return '%s' % chr(c)

	def makeHex4Digits(self, start=0x0000, end=0xFFFF):
		return '%04x' % Randomer.rnd(start, end+1)


	def make(self, name):
		#self.ruleExpandStack.append(name)
		o = Randomer.choice(self.rule[name])
		if callable(o):
			o = o()
		#self.ruleExpandStack.pop()
		#print('[DEBUG]%s%s -> %s' % (len(self.ruleExpandStack)*' ', name, o))
		return o

	def makePattern(self):
		max_try = 5
		tried = 0
		while tried < max_try:
			tried += 1
			try:
				return self.make('Pattern')
			except RecursionError as e:
				pass
		raise RecursionError('unexceptly RecursionError while make pattern...')

regexMaker = JSRegexMaker()
export = {
	'name': 'JS',
	'expression': {
		'number': RndJSNumber,
		'regex': regexMaker.makePattern,
	}
}
