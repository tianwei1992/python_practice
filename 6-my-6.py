#6-my-6.py
#func parameters specials
#key paramters
def hello(name='tian',greeting='hello'):
	print("%s,%s"%(greeting,name))
hello()
hello('li')
hello(greeting='good morning')

#*rest collect parameters
def test(a,b,*rest):
	print('a=',a)
	print('b=',b)
	print('rest=',rest)
test(1,2,3,4,5)
#here  rest will be a tuple collecting the other params
print()




def testdict(a,b,**rest):
	print('a=',a)
	print('b=',b)
	print('rest=',rest)
testdict(1,2,A=1,B=2)
#here  rest will be a tuple collecting the other params
print()

def testmix(a,b,*lst,**dictt):
        print('a=',a)
        print('b=',b)
        print('lst=',lst)
        print('dictt=',dictt)
testmix(1,2,3,4,5,name='A',age=24)
print()



#assign parameters
def test2(*lst):    
	print(lst)
para=[2,3,4,5]
test2(*para)
#here test2 returns a tuple ,too,
print()



def add(x,y):
	return x+y
params=(1,2)
print(add(*params))
print()
print()

#splicing
print('splicing')
def foo(x,y,z,m=0,n=0):
        print(x,y,z,m,n)
def call_foo(*args,**kwds):
        print('call foo')
        print(args,kwds)
        foo(*args,**kwds)
call_foo(1,2,3)



#special




def story(**kwds):
	return '%(job)s called %(name)s'%kwds
params={'name':'python'}
print(story(job='genius',**params))



def power(x,y,*others):
	if others:
		print('received others:',others)
	return pow(x,y)
lst=[3,4,5,6]
power(*lst)
print()
print()
