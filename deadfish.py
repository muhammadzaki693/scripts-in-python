"""
deadfish was created by Jonathan Todd Skinner this language is so easy to make even you can make on it self in deadfish~
"""
import typer

acc = 0
app = typer.Typer()

def execute_code(code):
	global acc
	for line in code.split('\n'):
		for c in line:
			if acc < 0 or acc > 255:
				acc = 0
			if c == "i":
				acc += 1
			elif c == "d":
				acc -= 1
			elif c == "s":
				acc **= 2
			elif c == "o":
				print(acc,end=" ")
			else:
				continue

@app.command()
def run(file: str):
	"""run a deadfish program"""
	with open(file, 'r') as f:
		code = f.read()
	execute_code(code)
	
@app.command()
def repl():
	"""run a deadfish REPL"""
	while True:
		code = input("deadfish> ")
		execute_code(code)

if __name__ == '__main__':
	app()