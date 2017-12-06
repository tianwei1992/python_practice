#8-my-1.py
##try/except
#
#
#
#catch exception
try:
	x=input('input x:')
	y=input('input:y:')
	print(float(x)/float(y))
except ZeroDivisionError:
	print("ZeroDivisionError!!!")

class MuffledCalculator:
	muffled=False
	def calc(self,expression):
		try:
			return eval(expression)
		except ZeroDivisionError:
			if self.muffled==False:
				raise
			else:
				print("ZeroDivisionError!!!")
calculator=MuffledCalculator()
print(calculator.calc('10/2'))

#muffle=false,then raise exception
#print(calculator.calc('10/0'))
calculator.muffled=True
#muffle=true,exception stay here forever
print(calculator.calc('10/0'))
