#11-11.py
#fileinput.input
def process(line):
	print(line)
import fileinput
for line in fileinput.input('somefile.txt'):
	process(line)

