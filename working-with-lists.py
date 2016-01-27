cities = ['Santa Cruz','Palo Alto','Lexington','Reno','Seattle','Dayton']
states = ['CA','IN','KY','TX','ID','FL']

for city in cities:
	print('The city is %s' % city)
	
for state in states:
	print('I have lived in',state)
	
elements = []
for i in range(0,6):
	print('Adding %d to the list' % i)
	elements.append(i)

for i in elements:
	print('The element is',i)

print(elements)
