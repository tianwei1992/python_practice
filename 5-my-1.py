#5-my-1.py
#Sequence unpacking
values=1,2,3,4
print('values=',values)
x,y,*rest=values
print('x=',x,'y=',y,'rest=',rest)
print()

dic1={'A':1,'B':2,'C':3}
key,value=dic1.popitem()
print('key=',key)
print('value=',value)
print()

#augmented assignment
x=2
print('x=',x)
x+=1
print('x=',x)
x**=3
print('x=',x)
