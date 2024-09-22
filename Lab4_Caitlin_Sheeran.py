'''
Caitlin Sheeran
9/20/2024
Program that outputs the amount of difcient numbers, perfect numbers,
and abundant numbers between 1 and number by user
'''

user_input = int(input('Enter an upper bound for a check: '))

dificient = 0
abundant = 0
perfect = 0

for i in range(1,user_input + 1):
	sum_d = 0
	for g in range(1,i):
		if i % g == 0:
			sum_d += g
	if i > sum_d:
		dificient += 1
		
	elif i < sum_d:
		abundant += 1
		
	else:
		perfect += 1	
		
print(f'Between 1 and {user_input} there are')
print(f'{dificient} dificient numbers')
print(f'{perfect} perfect numbers')
print(f'{abundant} abundant numbers')


