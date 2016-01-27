def game():
	print('You are on a game show!')
	print('Please pick a door, One or Two')
	door = input()
	print('And you win...')
	if door == str(1) or door == 'one' or door == 'One':
		print('an island')
	elif door == str(2) or door == 'two' or door == 'Two':
		print('nothing at all')
	else:
		print('an instruction manual')
		game()
game()
