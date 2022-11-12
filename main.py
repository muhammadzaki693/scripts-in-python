import os,glob

def init():
	for file in glob.glob("*_scr.py"):
		os.system(f"chmod 777 {file}")

def run(file):
	os.system(f"python {file}")

if __name__ == "__main__":
	init()
	run("deadfish_scr.py")