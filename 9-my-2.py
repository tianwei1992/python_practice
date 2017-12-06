#9-my-2.py
#member access
#to creat classes like sequence or dict
def checkIndex(key):
	if not isinstance(key,int):
		raise TypeError
	if key<0:
		raise IndexError


class ArithmeticSequnce:
	def __init__(self,start=0,step=1):
		self.start=start
		self.step=step
		self.changed={}
	def __getitem__(self,key):
		checkIndex(key)
		try:
			return self.changed[key]
		except KeyError:
			return self.start+key*self.step
	def __setitem__(self,key,value):
		checkIndex(key)
		self.changed[key]=value

a=ArithmeticSequnce(1,2)
print(a[3])
a[3]=10
print(a[3])
