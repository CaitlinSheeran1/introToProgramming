'''

A list: Is an ordered, sequential collection of zero or more python data objects
To create a list, we use [] and commas to seperate values ex.person ['matt','priem', 38, 67.5, 160.25]
A list is mutable, meaning we can change the internal data 
A string is immutable, meaning we an NOT change the internal data
WE can add something to the end of a list with the append() function 

'''

list = ['a', 'xyz', 3, 7.4, 'c', 10]

for element in list:
	print(element)
	
print(list[1]) #prints xyz
print(list[2:5]) # prints 3, 7.4, 'c'

list2 = ['a', 'b', 'c', 'e', 'e', 'f', 'g'] # supposed to be first 7 letters, but e was written twice

print(list2[3] == 'd')

list2[3] = 'd'

print(list2[3] == 'd')


list3 = ['apple','banana']

list3.append('pear') #.append adds onto a list at the end of it

list3.insert(1,'watermelon') # .insert allows you to add a object anywhere in the string at a postion before the new object
print(list3)

longest_length = 0
fruit_with_longest_name = ''
for fruit in list3:
	if len(fruit) > longest_length:
		longest_length = len(fruit)
		fruit_with_longest_name = fruit
		
print(longest_length)
print(fruit_with_longest_name)
