#9-my-5.py
#staticmethod and classmethos
class Myclass:
	@staticmethod
	def smeth():
		print('a static method')
	@classmethod
	def cmeth(cls):
		print('a cmeth methos',cls)

Myclass.smeth()
Myclass.cmeth()
c=Myclass()
c.smeth()
c.cmeth()