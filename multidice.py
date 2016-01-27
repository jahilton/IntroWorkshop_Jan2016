from random import randint

print('How many dice?')
dice_count = input()
print('How many faces?')
faces = input()
print('\n')

for i in range(1,int(dice_count)+1):
	print(randint(1,int(faces)))
