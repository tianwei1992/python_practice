#6-my-4.py
#storage{}
#



def init(names):
	'names is a dict'
	names['first']={}
	names['middle']={}
	names['last']={}
	print(names)
def lookup(label,name,names):
	'return a list'
	#print(names[label].get(name))
	return(names[label].get(name))

def store(sb,names):
	lst=sb.split()
	if len(lst)==2:
		lst.insert(1,' ')
	a,b,c=lst
	for x,y in zip([a,b,c],['first','middle','last']):
		if lookup(y,x,names):
			names[y][x].append(sb)
		else:
			names[y].setdefault(x,[sb])

storages={}
init(storages)
store('tian wei',storages)
store('li hong',storages)
store('tian guang zhi',storages)
lookup('first','tian',storages)
print(storages)
print()
print()

#imporved 
#what if stre('li hong','tian wei',storage)


def init(names):
	'names is a dict'
	names['first']={}
	names['middle']={}
	names['last']={}
	print(names)
	print()
def lookup(label,name,names):
	'return a list'
	#print(names[label].get(name))
	return(names[label].get(name))

def store(names,*sb):
	#changed here
	for someone in sb:
		lst=someone.split()
		if len(lst)==2:
			lst.insert(1,' ')
		a,b,c=lst
		for x,y in zip([a,b,c],['first','middle','last']):
			if lookup(y,x,names):
				names[y][x].append(someone)
			else:
				names[y].setdefault(x,[someone])
storages={}
init(storages)
store(storages,'tian wei','li hong','tian guang zhi')
print()
print(storages)
