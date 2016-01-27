class Shape(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def area(self):
		return self.x * self.y
	def perimeter(self):
		return 2*self.x + 2*self.y

long_rectangle = Shape(120,10)
fat_rectangle = Shape(130,120)

print(fat_rectangle.area() + long_rectangle.area())
