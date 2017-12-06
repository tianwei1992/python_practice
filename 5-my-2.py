#5-my-2.py
#if and or
#a or b ,Short expressions
name=input('plese input your name') or '<unknow>'
print("name=",name )
name.lower();
if name.endswith('wei'):
	if 'tian' in name :
		print('are you tian wei?')
	else:
		print('xxxx wei?')

elif name.endswith('hong') and 'li' in name:
	print('are you li hong?')
elif name=='<unknow>':
	print("you didint input" )
else:
	print("I don't know you" )
