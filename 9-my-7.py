#9-my-7.py
#generator
def faltten(nested):
	for subline in nested:
		for element in subline:
			yield element
f=faltten([[1,2],[3,4],[5]])
#print(f.next())

print(list(f))
for num in f:
	print(num)

def flattens(nested):
	try:
		#to avoid recursion of str
		try:
			nested+' '
		except:
			pass
		else:
			raise TypeError
		for subline in nested:
			for element in flattens(subline):
				yield element
	except TypeError:
		yield nested

lst=[[[[1,2],[3],[[4,5]]]]]
print(list(flattens(lst)))

#generator expressions
g=(i+2 for i in range(0,12) if i%3==0)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
try:
	print(next(g))
except:
	pass


#generator functions
##send throw close
def repeater(value):
	while True:
		new=(yield value)
		if new is not None:
			value=new
r=repeater(42)
print(next(repeater(42)))
print(next(r))
print('r=',r)
r.send(54)
print('r=',r)
# this is a new 

print('repeater(42)=',repeater(42))
print(next(r))
print(next(repeater(42)))
