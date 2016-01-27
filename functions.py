def add(a,b):
	print(a + b)
	
def subt(a,b):
	print(a - b)

pairs = {
	1: 21,
	30: 20
}

for x,y in pairs.items():
	add(x,y)
	subt(x,y)
