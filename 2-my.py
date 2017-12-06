#2-my1.py
#input your name ,check whether you are in the list ,if yes ,output name and age
'''
wei=['tian wei',24]
hong=['li hong',48]
guang=['tian guang zhi',49]
database=[wei,hong,guang]
print(database)
name=input('input your full name:')
found=False

for firstname in database:
	if firstname[0]==name:
		print('your name is :'+name,'and your age is :',str(firstname[1]))
		break
		found=True
if found==False:
        print('you are not in the list')

'''

wei=['tian wei',24]
hong=['li hong',48]
guang=['tian guang zhi',49]
database=[wei,hong,guang]
print(database)
name=input('input your full name:')

for firstname in database:
	if firstname[0]==name:
		print('your name is :'+name,'and your age is :',str(firstname[1]))
		break		
else:
        print('you are not in the list')


