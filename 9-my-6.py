#9-my-6.py
#iterator 

class Fibs:
	def __init__(self):
		self.a=0
		self.b=1
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>10:raise StopIteration
		return self.a
f=Fibs()
print(f)

it=iter(f)
print(it)
print(f is it)

#i=next(it)
#print(i)

#i=next(it)
#print(i)

print(list(f))

it=iter([1,2,3])
print(list(it))


for index,i in iter('abc'):
        print(i,index)
print(list('abc'))
