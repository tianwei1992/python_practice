#7-my-2.py
#The namespace of the class
class MemberCounter:
	member=0
	def init(self):
		MemberCounter.member+=1
a=MemberCounter()
a.init()
b=MemberCounter()
b.init()
c=MemberCounter()
c.init()
print('a.member=',a.member)
print('b.member=',b.member)
print('c.member=',c.member)
print(MemberCounter.member)
