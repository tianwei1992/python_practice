#6-my-8.py
#nest of scope
def multiplier(factor):
	def multiplierByFactor(number):
		return number*factor
	return multiplierByFactor


double=multiplier(2)
print(double)
print(type(double))
print(type(double(5)))
print('double(5)=',double(5))
triple=multiplier(3)
print(triple)
print(type(triple))
print('triple(3)=',triple(3))
print(multiplier(5)(4))
print(multiplier.<locals>)
