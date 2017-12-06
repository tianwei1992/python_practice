#6-my-5.py
#to change parameter outside func with func
# it needs some skills
# 

'''to realize

foo=1
inc(foo)

'''

#1 way
def inc(foo):
	return foo+1
foo=1
foo=inc(foo)
print(foo)

#2 way
def inc(foo):
	foo[0]+=1
	for i in foo:
		print(i in foo)
		print(i is foo[0])
		i+=1
foo=[1]
inc(foo)
print(foo)
