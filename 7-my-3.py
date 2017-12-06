#7-my-3.py
#super class
class Filter:
	def init(self):
		self.blocked=[]
	def filter(self,sequence):
		return([x for x in sequence if x not in self.blocked])
class SPAMFilter(Filter):
	def init(self):
		self.blocked=['SPAM']
s=SPAMFilter()
s.init()
print(s.filter(['SPAM','egg','bacon']))
print()



#multiple inheritance
class Calculator:
	def calculate(self,expression):
		self.value=eval(expression)
class Talker:
	def talk(self):
		print('my value is:',self.value)
class TalkingCalculator(Calculator,Talker):
	pass
tc=TalkingCalculator()
tc.calculate('1+2')
tc.talk()
t=Talker()
#t.talk()
print()

#Interface and Introspection
#hasattr
print(hasattr(tc,'calculate'))
print(hasattr(t,'calculate'))
#getattr
print(getattr(tc,'talk'))

#check if 'talk' callable?
print(hasattr(getattr(tc,'talk',None),'__call__'))

#setattr
setattr(tc,'name','Grace')
print(tc.name)

print()


#check inheritation
print('issubclass(SPAMFilter,Filter):')
print(issubclass(SPAMFilter,Filter))
print('SPAMFilter.__bases__:')
print(SPAMFilter.__bases__)
print('isinstance(s,SPAMFilter):')
print(isinstance(s,SPAMFilter))
print('s.__class__:')
print(s.__class__)




#
