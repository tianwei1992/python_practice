#6-my-7.py
#scope 
#global vars
def combine(parameter):
	print (parameter+globals()['parameter'])
parameter='berry'
combine('shrub')
print()


x=1
def change_global():
	global x
	x=x+1
change_global()
print(x)
