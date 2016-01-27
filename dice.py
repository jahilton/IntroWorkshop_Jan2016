from die import Die

class D8(Die):
	def __init__(self):
		super(D8,self).__init__(8)
	
class D20(Die):
	def __init__(self):
		super(D20,self).__init__(20)

d8 = D8()
d20 = D20()

print(d8.roll())
print(d20.roll())
