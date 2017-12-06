#11-8.py
#f=open(r'somefile.txt')
#read each line in tern

def process(line):
	print(line)
f=open(r'somefile.txt')
while True:
	line=f.readline()
	if line:
		process(line)
	else:
		break
f.close()

#11-10.py
f=open(r'somefile.txt')
for line in f.readlines():
	process(line)
f.close()
