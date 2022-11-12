import os

def run(file,args):
	os.system(f"python {file} {args}")

if __name__ == "__main__":
	run("deadfish.py", "run df.txt")