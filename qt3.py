#qt3.py
def f1(**kwds):      
    print (kwds['a'])
    
dt=dict(a=1,b=2)
f1(**dt)



def f2(kwds):
    print(kwds['a'])

f2(dt)




key1,key2=dt
print(key1)
print(key2)
f1(a=1)
