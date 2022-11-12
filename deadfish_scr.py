#!/bin/bash python
# im sorry if this is ugly looking code
import ply.lex as lex

#variabel
accumulator = 0

#lexer
tokens = (
	'INCREMENT',
	'DECREMENT',
	'SQUARE',
	'OUTPUT'
)

t_INCREMENT = r'i'
t_DECREMENT = r'd'
t_SQUARE = r's'
t_OUTPUT = r'o'

def t_error(t):
	print("Illegal character '%s'" % t.value[0])

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore ='\t'

lexer = lex.lex()

#parser
def parser(tokens):
	global accumulator
	if accumulator < 0 or accumulator > 255:
		accumulator = 0
	if tokens.type == 'INCREMENT':
		accumulator += 1
	if tokens.type == 'DECREMENT':
		accumulator -= 1
	if tokens.type == 'SQUARE':
		accumulator = accumulator ** accumulator
	if tokens.type == 'OUTPUT':
		print(accumulator)

program = input(">")
lexer.input(program)
while True:
	tok = lexer.token()
	if not tok:
		break
	parser(tok)