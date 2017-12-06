#5-my-8.py
#pass del exec eval

 #pass
counter=3
while True:
  	print('you can try only'+str(counter)+'times' )
  	counter-=1
  	if(counter<0):
  	    break
  	x=input('input a or b')
  	if x=='a':
  	    pass
  	else:
  	    print('should input a!')

#del
dict1={'a':1,'b':2}
dict2=dict1
print('dict1=',dict1)
print('dict2=',dict2)
dict1=None
print('dict2=',dict2)
print()


x=['a','b']
y=x
y[1]='c'
print('x=',x)
del x
print(y)


#exec
#exec ('hello')

from math import sqrt
scope={}
exec ('sqrt=1',{})
print(len(scope))
print(scope.keys())
print(sqrt(4))
print()

#eval
scope={}
scope['x']=2
scope['y']=3
print(eval('x*y',scope))
scope={}
exec('x=2',scope)
print(eval('x*x',scope))
