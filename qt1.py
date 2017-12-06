#qt1.py
class A:
	def __init__(self, *args): 
		self.contained = args  
	def __iter__(self): 
		for elem in self.contained:
 			yield elem+1
			#yield from map(lambda x:x+1, self.contained)

a=A(1,2,3)
x=iter(a)
print(next(x))
print(next(x))
print(next(x))

