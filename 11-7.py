#11-7.py
#file iteration
#
##read file by char
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


#11-9
f=open(r'somefile.txt')
for char in f.read():
	if char:
		process(char)
	else:
		break
f.close()
