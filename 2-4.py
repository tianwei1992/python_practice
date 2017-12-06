#2-4
#input your name and pin code,then to check whther you are in the list 
database=[['wei','1234'],['hong','5678'],['guang','9012']]
username=input('input username:')
pin=input('input PIN code:')
if[username,pin] in database:
	print('Access granted')
else:
        print('Acess deny')
