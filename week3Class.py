# does numbers between 0-10 if they are even or odd
'''
number = 0

while number <= 10:
	
	if number % 2 ==1:
		print(number, "is odd")
	
	else:
		print(number, "is even")
	
	
	number += 1

'''

#Write a number guessing game
'''
import random

computers_pick = random.randint(0,10)
keep_playing = True

while keep_playing:
	user_guess = int(input('Please guess a number between 0-10: '))
	if user_guess == computers_pick:
		print(f'You win')
		keep_playing = False
		
	elif user_guess < computers_pick:
		print(f'Your number is too small')
	elif user_guess > computers_pick:
		print(f'Your number is too big')
'''
'''
for number in range(0,11):
	if number % 2 != 0:
		print(f'{number} is odd')
		
	else:
		print(f'{number} is even')		
		
'''

#Strings

x = 'hello world'

full_name = 'matt priem'
first_name = full_name[:4]
last_name =full_name[5:]

print(full_name)
print(first_name)
print(last_name)

#print all the mubmbers between 10 and 50 (inclusively)

for number in range(10,51):
	print(number)
	
word = 'apples and bananas'

for letter in word:
	print(letter)

for index in range(0,len(word)):
	print(index)



