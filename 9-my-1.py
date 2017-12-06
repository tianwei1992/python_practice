#9-my-1.py
#magic methods with __
#subclass redefine __init



class A:
	def __init__(self):
		self.name='A'
		self.age=1
	def hello(self):
		print('My name is %s,and age is %d'%(self.name,self.age))

class B(A):
	def __init__(self):
		A.__init__(self)
		self.name='B'

class C(A):
	def __init__(self):
		super(C,self).__init__()
		self.name='C'
a=A()
a.hello()
b=B()
b.hello()
c=C()
c.hello()

