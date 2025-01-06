'''
sentence = 'this sentence has six words long'

words = []
		
		
word = ' '
for index in range(len(sentence)):
	if sentence[index] != ' ':
		word += sentence[index]
	else:
		words.append(word) #record the word
		word = ' '         #resr word to no letters
	
	if index == len(sentence)-1: # if len == end of the word, append
		words.append(word)     
print(words)
	
	
	
words[3] = 'seven'
print(words)

new_sentence = ''
for word in words:
	new_sentence += word
	new_sentence += ' ' 
	
print(new_sentence)
'''

list1 = [1,2,3]
list2 = list1

print(list1)
print(list2)

list1[1] = 5

print(list1)
print(list2)

