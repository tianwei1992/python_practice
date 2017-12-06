#5-my-6.py
#break and continue
##while true
#for-else
from math import sqrt

while True:
	max=input('input max:')
	if int(max)==int(float(max)):
		break
	print('integer,please')
while True:
	min=input('input min:')
	if int(min)==int(float(min)):
		break
	print('integer,please')

for i in range(int(max),int(min),-1):
	root=sqrt(i)
	if root==int(root):
		print(i)
		break
else:
	print("can't find!")
print()

