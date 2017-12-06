#8-my-2.py
#try-except-except-except 
#except (error1,error2,error3) as e:
#  print(e)

try:
	x=input('x=:')
	y=input('y=:')
	print(float(x)/float(y))
#except ZeroDivisionError:
#	print("ZeroDivisionError!!!")
#except TypeError:
#	print("TypeError!!!")
except (ZeroDivisionError,TypeError,NameError) as e:
	print(e)
#except:
	#print("Anyway,it's Error!!!")




#try-except-else
while True:
	try:
		x=input('x=')
		y=input('y=')
		print(float(x)/float(y))
	except Exception as e:
		print('except happend!')
		print(e)
	else:
		break
