class Parent(object):
	def __init__(self,height):
		self.height = height
	def brown_hair(self):
		print('I have brown hair.')

class Son(Parent):
	def __init__(self,school):
		self.school = school
	def blue_eyes(self):
		print('I have blue eyes.')
		
dad = Parent(62)
son = Son('Tara Redwood')
dad.brown_hair()
son.blue_eyes()
son.brown_hair()
