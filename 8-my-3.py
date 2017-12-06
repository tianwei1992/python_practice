#8-my-3.py
#try finally

x=None
try:

	print('try1')
	x=1/2
	print('try2')
finally:
	print('cleaning up')
	del x
print()

x=None
y=2
try:
	x=1/y
	print('try')
except NameError:
	print('unkown variable')
else:
	print('went well')
finally:
	print('cleaning up')
	del x
