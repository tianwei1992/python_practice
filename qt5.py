#qt5.py
class A:
	def __init__(self,*args):
		self.contained=args
	def __iter__(self):
		for elem in self.contained:
			yield elem+1
a=A(1,2,3)
it=iter(a)
print(next(it))
print(next(it))
