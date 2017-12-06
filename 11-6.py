#11-6.py
#file iteration
#
##by char

def process(char):
	print(char)

f=open(r'somefile.txt')
while True:
	char=f.read(1)
	if char:
		process(char)
	else:
		break
f.close()


