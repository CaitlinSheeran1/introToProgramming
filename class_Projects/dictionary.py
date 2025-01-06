'''
a dictionary orginizes information by association rather than position
example. a phonebook is an example of a dictionary
the names are the keys and the phone numbers are the values
A dictionary associates a set of keys with values
The entire sequence of entries (of a dictionary) is enclosed in curly
braces {}, a colon : separates a key and its value, and a comma, 
separates different key-value pairs

We can look up values in a dictionary by searching the key. The syntax
is dictionary_name[key] this will produce the value.

If we search for a key that is not in the dictionary, we will get 
a key error

To add a key-value pair to the dictionary, we use the syntax
	dictionary_name[key] = name
'''

phonebook = {'matt':3891438, 'waters':3891496}

phonebook['ashley'] = 3891234

phonebook['matt'] = 3891234

print(phonebook['matt'])

for key in phonebook:
	print(key)
	
#create a custom function
def text_user(user_number, msg):
	virtual_phone = sys.open_phone_app
	virtual_phone.call()
	
for key in phonebook:
	print(phonebook[key])
	automated_msg = 'ggigijgijg'
	spam_call(phonebook[key], automated_msg)

