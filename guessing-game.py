from random import randint

actual = randint(1,20)
tries = 3

print('Guess a number between 1 and 20. You have %d tries' % tries)

def game():
	global tries
	guess = int(input())
	if guess == actual:
		print('YOU ARE A CORRECT!')
	elif guess < actual and guess > 0:
		print('Nope, aim higher')
		tries -= 1
		if tries > 0:
			print('You have %d guesses remaining. Try again' % tries)
			game()
		else:
			print('You are out of chances. The number was %d.' % actual)
			print('Thank you for playing')
	elif guess > actual and guess < 21:
		print('Nope, go lower')
		tries -= 1
		if tries > 0:
			print('You have %d guesses remaining. Try again' % tries)
			game()
		else:
			print('You are out of chances. The number was %d.' % actual)
			print('Thank you for playing')
	else:
		print('Please re-read the rules')
		tries -= 1
		if tries > 0:
			print('Try again')
			game()
		else:
			print('You are out of chances. The number was %d.' % actual)
			print('Thank you for playing')
		
game()
