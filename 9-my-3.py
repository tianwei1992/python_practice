#9-my-3.py
#CounterList
class CounterList(list):
	def __init__(self,*args):
		super(CounterList,self).__init__(*args)
		self.counter=0
	def __getitem__(self,index):
		self.counter+=1
		return super(CounterList,self).__getitem__(index)
c=CounterList([1,2,3])
print(c.counter)
c[1]=4
print(c.counter)
c[0]+c[2]
print(c.counter)
