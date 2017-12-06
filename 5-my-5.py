#5-my-5.py
#for
for number in range(1,10):
	print (number)
print()

for i in {'A':1,'B':2,'C':3}.values():
	print('key=',i)
print()

for key,value in {'A':1,'B':2,'C':3}.items():
	print('key=',key)
	print('value=',value)
print()

print('A' in {'A':1,'B':2,'C':3})
print(1 in {'A':1,'B':2,'C':3})
print()


#parallel iteration
names=['tian','li','guang']
ages=[24,48,49]
for i in range(0,3):
	print("%s's age is %d"%(names[i],ages[i]))
	
print(list(zip(names,ages)))
#in version 3,zip is an iterable objects;
for (name,age) in list(zip(names,ages)):
	print("%s's age is %d"%(name,age))
print()


#index iteration
strings=['xyabc','zyabc','abc']
index=0
for string in strings:
	if 'abc' in string:
		strings[index]='123'
	index+=1
print('strings=',strings)
print()
	
#better version
strings=['xyabc','zyabc','abc']
for index,string in enumerate(strings):
	if 'abc' in string:
		strings[index]='123'
print('strings=',strings)
print()


#reversed() and sorted(),join()
#sorted() return list
#reversed return iterator
print(sorted('Hello word'))
print(list(reversed('Hello word')))
print(''.join(reversed('Hello word')))