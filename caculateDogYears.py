'''
Caitlin Sheeran
9/6/2024

This program will caculate human years to dog years
'''

age = float(input("Enter your age: "))

age_in_dog_years = int((age * 7))
years_in_months = age_in_dog_years % 12
dog_age_days = years_in_months % 30

age_in_cat_years = int(age / 9)
months_in_cat_years = age_in_cat_years % 12
days_in_cat = months_in_cat_years % 30

age_in_horse_years = int( 3 * ((((age **2) - 47 ) / 7) + 12))
months_in_horse = age_in_horse_years % 12
days_in_horse = months_in_horse % 30

print("Your age in dog years is " + str(age_in_dog_years) + " years " + str(years_in_months) + " months and " + str(dog_age_days) + " days")
print("Your age in cat years is " + str(age_in_cat_years) + " years " + str(months_in_cat_years) + " months and " + str(days_in_cat) + " days")
print("Your age in cat years is " + str(age_in_horse_years) + " years " + str(months_in_horse) + " months and " + str(days_in_horse) + " days")


