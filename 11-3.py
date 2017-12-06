#11-3.py
#basic file functions
f=open(r'somefile.txt')
print(f.read(7))
print(f.read(4))
f.close()


f=open(r'somefile.txt')
print(f.read())
f.close()



f=open(r'somefile.txt')
for i in range(3):
	print(f.readline())
f.close()

import pprint
pprint.pprint(open(r'somefile.txt').readlines())


f=open(r'somefile.txt','w')
f.write('this\nis no\n haiku')
f.close()
f=open(r'somefile.txt','r')
lines=f.readlines()
print(lines)
f.close()
lines[1]="isn't a\n"

f=open(r'somefile.txt','w')
f.writelines(lines)
f.close()
pprint.pprint(open(r'somefile.txt').readlines())
