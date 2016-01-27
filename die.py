from random import randint

class Die(object):
	def __init__(self,faces=6): #=6 sets the default to 6
		self.faces = faces
	def roll(self):
		return randint(1,self.faces)
