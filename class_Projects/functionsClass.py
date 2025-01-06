	
'''	
A function is another data type with 2 operators
1. Assignments
2. Parentheses ()

the parentheses are the operator that tells python to apply the
function of the supplied parameters

The process by which a function's formal parameters recieves an actual
parameter value is know as parameter passing
'''
'''
def add_three(x):
	y = x + 4
	return y
	
var1 = add_three(var0)


x is the formal parameter and 7 is the actual parameter which is passed
to the function when it is invoked (called)

Namescapces
In python, all names defined in a program for data and functions are 
organized into namespaces. There are the names available when the
program is executed, By defailt, python loads
1. __builtin__
2. __main__

ONce the function is completed the local namespace is destroyed. That is,
the memory is reallocated

When we try to import the math module using import math, Python creates
a namespace with a reference to the new namespace for the module itself


'''

'''
var0 - 7

def add_three(x):
	y = x + 3
	print(y)
	return y
	
def add_two_values(value1, value2, value3):
	return value1 + value2 + value3
	
x = add_two_values(1,2,3)

print(x)
'''

def greeting(name, age = 'unknown'):
	print(f'hello {name}.')
	if age == 'unknown':
		print(f'what is your age?')
		
greeting('matt',38)
print('\n-----\n')
greeting('matt')


















