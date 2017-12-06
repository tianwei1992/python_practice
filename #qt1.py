#qt1.py
class A:
	def __init__(self, *args): 
		self.contained = args  
	def __iter__(self): 
		for elem in self.contained:   
			yield elem + 1 

a=A(1,2,3)
print(a.next())
print(a.next())
print(a.next())