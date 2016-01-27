from sys import argv

script, file_name = argv
print('we\'re going to erase %r' % file_name)
print('if you don\'t want to, type STOP')
print('if you are ok with the erase, hit Y')
def func():
	answer = input('?')
	if answer == 'STOP':
		print('Sorry to bother you')
	elif answer == 'Y' or answer == 'y':
		target = open(file_name,'w')
		target.truncate()

		print('Now I will ask for 3 lines')
		line1 = input('Line1:')
		line2 = input('Line2:')
		line3 = input('Line3:')

		target.write(line1)
		target.write('\n')
		target.write(line2)
		target.write('\n')
		target.write(line3)
		target.write('\n')

		target.close()
	else:
		print('huh?')
		func()
func()
