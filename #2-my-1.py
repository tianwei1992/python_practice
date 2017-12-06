#2-my1.py
wei=['tian wei',24]
hong=['li hong',48]
guang=['tian guang zhi',49]
database=[wei,hong,guang]
print(database)
while True:
	name=input('input your full name:')
	find=False
	for firstname in database:
		if firstname[0]==name:
			print('your name is :'+name,'and your age is',str(firstname[1]))
			find=True
	if find==False:
		print('you are not in the list')




