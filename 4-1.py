#4-1.py
#create a dic,including name with age and address,then look up
#a dic in a dic
A={'phone':'1','addr':'fist street'}
B={'phone':'2','addr':'second street'}
C={'phone':'3','addr':'third street'}
dic1={'a':A,'b':B,'c':C}

lables=dict([('addr','address'),('phone','phone number')])
print('dic1:',dic1)

name=input('input name within a or b or c ')
request=input('p or a ?')

if (request=='p') :
	lable='phone'
if (request=='a'):
	lable='addr'
if (name in dic1):
	print("%s 's %s is %s"%(name,lables[lable],dic1[name][lable]))
