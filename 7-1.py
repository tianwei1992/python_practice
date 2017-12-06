#7-1.py
##class
class Person:
	def setName(self,name):
		self.name=name
	def getName(self):
		return self.name
	def greet(self):
		print('hello!I am %s'%self.name)
foo=Person()
foo.setName('Grace')
print(foo.getName())
foo.greet()
print()


class Bird:
	song='squaawk!'
	def sing(self):
		print(self.song)
bird=Bird()
bird.sing()
birdsong=bird.sing
birdsong()
print()


#private
class Secretive:
	def __inaccessible(self):
		print('bet you cant see me')
	def accessible(self):
	    print('The secret message is:')
	    self.__inaccessible()
s=Secretive()
#s.__inaccessible()
s.accessible()
#eroor in python 3
s._Secretive_inaccessible()
