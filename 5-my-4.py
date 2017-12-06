#5-my-4.py
##loop while
name=''
#strip: avoid spaces outsides
while(not name.strip()):
   name=input('input your name :')
print('your name is %s'%name.strip())
