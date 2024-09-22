'''''
Caitlin Sheeran
9/13/2024

Tax Brackets and Rates
'''

earned_income = int(input("Enter the amount of income you earned in 2023: "))
marital_status = str(input("Are you married or single? M for Married S for Single: "))


if marital_status == 'S' or marital_status == 's':
	if earned_income >= 0 and earned_income <= 11000:
		earned_income = earned_income * 0.10
		print("This year you owe", earned_income, "in taxes")
		
	elif earned_income >= 11001 and earned_income <=44725:
		earned_income = (earned_income - 11000) * 0.12
		earned_income = 11000 * 0.10 + earned_income
		print("This year you owe", earned_income, "in taxes")
		
	elif earned_income >= 44726 and earned_income <= 95375:
		earned_income = (earned_income - 44725) * 0.22
		earned_income = (11000 * 0.10) + ((44725 - 11000)* 0.12) + earned_income
		print("This year you owe", earned_income,"in taxes")
		
	elif earned_income >= 95376:
		print("You made too much for this calculator. Hurray!")
		
elif marital_status == 'M' or marital_status == 'm':
	if earned_income >= 0 and earned_income <= 22000:
		earned_income = earned_income * 0.10
		print("This year you owe", earned_income, "in taxes")
		
	elif earned_income >= 220001 and earned_income <= 89450:
		earned_income = (earned_income - 22000) * 0.12
		earned_income = 22000 * 0.10 + earned_income
		print("This year you owe", earned_income, "in taxes")
		
	elif earned_income >= 89451 and earned_income <= 190750:
		earned_income = (earned_income - 89450) * 0.22
		earned_income = (22000 * 0.10) + ((89450 - 22000) * 0.12) + earned_income
		print("This year you owe", earned_income, "in taxes")
		
	elif earned_income >= 190751:
		print("You made too much for this calculator. Hurray!")
else:
	print("Invalid number or marital status entered")
