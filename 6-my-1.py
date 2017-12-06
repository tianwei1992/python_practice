#6-my-1.py
##{}.setdefault('a',[]).append()
storage={}
storage['first']={}
#storage['first'].setdefault('Grace',[]).append('sister')
tian='tian'
r=storage['first'].setdefault('Grace',tian)
print(r is storage['first']['Grace'])
print(storage)
