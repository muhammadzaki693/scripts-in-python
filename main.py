"""
if you can not run the file then run this
"""
import glob

for file in glob.glob("*.py"):
	os.system("chmod 777 {}".format(file))