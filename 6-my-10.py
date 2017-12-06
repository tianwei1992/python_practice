#6-my-10.py
#map filter reduce
#function tools
import functools
from functools import reduce


#map
print(list(map(str,range(10))))

ls=[1,2,3]
rs=map(str,ls)
print(list(rs))


#filter
def func(x):
    return x.isalnum()
seq=['1','str','?!','***']
ls=filter(func,seq)
print(list(ls))



ln=filter(lambda x:x.isalnum(),seq)
print(list(ln))


#reduce
seq=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,seq)
print(sum)

def add(x,y):
    return x+y  
print(functools.reduce(add, range(1, 5)))
