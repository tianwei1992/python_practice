#6-my-9.py
#recursion
#


#factorial
def factorial(n):
	if n==1:
		return 1
	else:
		return n*factorial(n-1)

print(factorial(4))


#power

def power(x,n):
	if n==1:
		return x
	else:
		return x*power(x,n-1)
print(power(2,3))

#binary search
from math import floor
def search(sequence,number,lower=0,upper=None):
	#print('lower=',lower)
	#print('upper=',upper)
	sequence.sort()
	#print('sequence[lower:upper]=',sequence[lower:upper])
	#print('len(sequence[lower:upper])=',len(sequence[lower:upper]))
	print('sequence[lower]=',sequence[lower])
	print('number=',number)
	try:
		if len(sequence[lower:upper])==0 or (lower==0 and upper==None):
			if (sequence[lower]==number):
				print('found')
				print("%d 's index is %d"%(number,lower))
				print()
			else:
				print("can't find,finish")
				print()
				return
	except:
		print("can't find,finish")
		print()
	
	middle=floor(len(sequence[lower:upper])/2)+lower
	#print(middle)
	if number==sequence[middle]:
		print('found')
		print("%d 's index is %d"%(number,middle))
		print()
		
	elif number>sequence[middle]:
		search(sequence,number,middle+1,upper)
	elif number<sequence[middle]:
		search(sequence,number,lower,middle-1)
	else:
		print('find')
		print("%d 's index is %d"%number,middle)
		print()
search([1,2,3,5],2)
#unsort
search([5,3,2,4],3)
#longer list,left
search([1,2,3,4,5,6,7,8,9],3)
#longer list,right
search([1,2,3,4,5,6,7,8,9],7)
#edge
search([1,2,3,4,5,6,7,8,9],1)
search([1,2,3,4,5,6,7,8,9],9)
#cant found 
search([2,3,4,5,6,7,8,9],0)
search([0,0,1],0)
search([0],0)
search([0],1)
