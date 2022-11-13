import ply.lex as lex
import ply.yacc as yacc
import sys

#lexer
tokens = [
	"INT",
	"FLOAT",
	"NAME",
	"PLUS",
	"MINUS",
	"MULT",
	"DIV",
	"EQUALS"
]

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_EQUALS = r'\='
t_ignore = " "

def t_FLOAT(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_INT(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_NAME(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type = 'NAME'
	return t

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

lexer = lex.lex()

#parser
precedence = (
	("left", "PLUS", "MINUS"),
	("left", "MULT", "DIV"),
)
env = {}

def p_calc(p):
	"""
 	calc : expression
         | empty
		 | var_assign
	"""
	print(run(p[1]))

def p_var_assign(p):
	"""
    var_assign : NAME EQUALS expression
	"""
	p[0] = ("=", p[1], p[3])

def p_expression(p):
	"""
    expression : expression PLUS expression
	           | expression MINUS expression
			   | expression MULT expression
	  	       | expression DIV expression
    """
	p[0] = (p[2], p[1], p[3])

def p_expression_int_float(p):
	"""
    expression : INT
	           | FLOAT
	"""
	p[0] = p[1]

def p_expression_var(p):
	"""
    expression : NAME
	"""
	p[0] = ("var", p[1])

def p_error(p):
	print("syntax error")

def p_empty(p):
	"""
    empty :
	"""
	p[0] = None

def run(p):
	global env
	if type(p) == tuple:
		if p[0] == "+":
			return run(p[1]) + run(p[2])
		elif p[0] == "-":
			return run(p[1]) - run(p[2])
		elif p[0] == "*":
			return run(p[1]) * run(p[2])
		elif p[0] == "/":
			return run(p[1]) / run(p[2])
		elif p[0] == "=":
			env[p[1]] = run(p[2])
		elif p[0] == "var":
			if p[1] not in env:
				print(p[1] + " is not defined")
				return 0
			else:
			    return env[p[1]]
	else:
		return p

parser = yacc.yacc()

while True:
	try:
		s = input("calculator> ")
	except:
		break
	parser.parse(s)