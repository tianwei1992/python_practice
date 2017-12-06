#4-my-2.py
#dictory functions


#clear 
x={'A':1,'B':2,'C':[3,4,5]}
y=x
x.clear()
print('x=:',x)
print('y=:',y)
print()

#copy deepcopy
from copy import deepcopy
x={'A':1,'B':2,'C':[3,4,5]}
y1=x.copy()
y2=deepcopy(x)
x['A']=4
x['C'].remove(4)
print('x=:',x)
print('y1=:',y1)
print('y2=:',y2)
print()

#get
x={'A':1,'B':2,'C':[3,4,5]}
r=x.get('A',5)
print('x=:',x)
print('r=:',r)
r=x.get('D',6)
print('r=:',r)
print('x=:',x)
print('get:',x.get('D'))
print()

#setdefault
x={'A':1,'B':2,'C':[3,4,5]}
r=x.setdefault('D',6)
print('setdefault,x=:',x)
print('setdefault,r=:',r)
print()

#fromkeys
x={}
y=x.fromkeys(['A','B','C'],'defaultvalue')
print('y=:',y)
print()

#has_key
#not in 3.0
#x={'A':1,'B':2,'C':[3,4,5]}
#print(x.has_key('B'))
#print()


#items keys values
x={'A':1,'B':2,'C':[3,4,5]}
print('items:',x.items())
print('keys:',x.keys())
print('values:',x.values())
print()

#pop popitem
print("x.pop('A')=",x.pop('A'))
print('x=:',x)
print()
print("x.popitem()=",x.popitem())
print('x=:',x)
print()



#update
x={'A':1,'B':2,'C':[3,4,5]}
y={'D':6}
x.update(y)
print('x=:',x)
print()

