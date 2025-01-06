user_input = input("Enter a letter and a word: ")

number = 0
letter_input = user_input[0]
word_input = user_input[2:]

for char in word_input:
    if char == letter_input:
        number += 1
if number == 1:
    print(f'{number} {letter_input}')
else:
    print(f"{number} {letter_input}'s")
