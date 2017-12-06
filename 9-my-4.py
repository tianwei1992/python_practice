#9-my-4.py
#accessor:combine height & width to size
#
#
#
#
#property()

class Rectangle:
	def __init__(self):
		self.width=0
		self.heitht=0
	def setSize(self,size):
		self.width,self.height=size
	def getSize(self):
		return self.width,self.height
	size=property(getSize,setSize)

r=Rectangle()
r.size=1,2
print(r.size)

#__getattr__
#__setattr__
class Rectangle2:
	def __init__(self):
		self.width=0
		self.heitht=0
	def __getattr__(self,name):
		if name=='size':
			return (self.width,self.height)
		else:
			raise AttributeError
	def __setattr__(self,name,value):
		if name=="size":
		   self.width,self.height=value
		else:
		 	self.__dict__[name]=value

r2=Rectangle2()
r2.size=3,4
print(r2.size)
r2.size2222=5
print(r2.size2222)
