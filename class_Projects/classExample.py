'''
movie theater prices
0-4 price is free
5-17 price is 10
18-64 is 20
65+ price is 12
''''

age= int(input("Please enter your age: "))

if age < 5:
	print("Ticket price is free")
	
if age < 18:
	print("Ticket price is $10")
	
if age < 65:
	print("Ticket price is $20")
	
else:
	print("Ticket price is $12")
	
	
	
	
	
	''''
	>90 A
	80-89 B
	70-79 C
	60-69 D
	<60 F
	''''
	
	
grade = float(input("Enter percentage: ")

if grade >= 90:
	print("your letter grade is: A")
if grade >= 80 and grade < 90:
	print("your letter grade is: B")
if grade >= 70 and grade < 80:
	print("Your letter grade is: C")
if grade >= 60 and grade < 70:
	print("your letter grade is: D")
else:
	print("Your letter grade is: Fail")
	
	
