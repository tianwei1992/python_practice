#11-13.py
from __future__ import with_statement
for line in  open(r'somefile.txt'):
	print(line)

print(list(open(r'somefile.txt')))
print(open(r'somefile.txt'))
a,b,c=open(r'somefile.txt')

print(a)
print(b)
print(c)
