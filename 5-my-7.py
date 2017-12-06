#5-my-7
#list conprehension
print(x*x for i in range(1,10,2))

boys=['1a','2b','3c']
girls=['1A','2B','3C']
print([a+'+'+b for a in boys for b in girls if a[0]==b[0]])
print([a+'+'+b for a in boys for b in girls])

#better version
boys=['1a','2b','3c']
girls=['1A','2B','3C']
c=[]
for boy in boys:
    for girl in girls:
        if boy[0]==girl[0]:
            c.append(boy+'+'+girl )
print(c)
        
#another etter version
boys=['1a','2b','3c']
girls=['1A','2B','3C']
letterBoys={}
for boy in boys:
	letterBoys.setdefault(boy[0],[]).append(boy)
print(letterBoys)
print([a+'+'+b for b in girls for a in letterBoys[b[0]]] )

print('here'[0])
#don't write like this: print('here'(0))

