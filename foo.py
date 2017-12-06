def inc(foo2):
	foo[0]+=1
	for i in foo:
		print(id(i))
		print(id(foo[0]))
		print(i in foo)
		print(i is foo[0])
		i+=1
		print(id(i))	
		print(id(foo[0]))
		print(id(1))
foo2=[1]
inc(foo2)
print(foo2)
