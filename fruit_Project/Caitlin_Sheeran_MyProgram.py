from Caitlin_Sheeran_Stats import *

txt_list = []
apple_numbers = []
banana_numbers = []
stawberries_number = []
fruit_number = []
total_number = []

attempts = 0
file_opened = False

while not file_opened:
    file_name = input("Enter file name: ")
    attempts += 1

    try:
        


            with open(file_name, 'r') as file:
                for line in file:
                    fruit_info = line.strip().split()
    
                    txt_list.append(fruit_info)

                file_opened = True
    except FileNotFoundError:
        ask_again = input("File not found. Try another file name? (y/n): ")
        if ask_again != 'y':
            print(f"No file found. Exiting program")
            break
    print(f"Number of tries so far: {attempts}")

if file_opened:
    print(f"file: {file_name} has successfully been processed")
    print(f"See output.txt for fruit statistics")
    print(f"Number of tries so far: {attempts}")

    for day in txt_list:
        if day[1] == "apple":
            apple_numbers.append(int(day[2]))
        elif day[1] == 'banana':
            banana_numbers.append(int(day[2]))
        elif day[1] == 'strawberry':
            stawberries_number.append(int(day[2]))
        if day[1] == "apple" or day[1] == 'banana' or day[1] == 'strawberry':
            total_number.append(int(day[2]))

    

    apple_mean = Mean(apple_numbers)
    apple_median = Median(apple_numbers)
    banana_mean = Mean(banana_numbers)
    banana_median = Median(banana_numbers)
    stawberries_mean = Mean(stawberries_number)
    stawberries_median = Median(stawberries_number)
    total_mean = Mean(total_number)
    total_median = Median(total_number)


    new_file = open('Caitlin_Sheeran_Output.txt', 'w')

    new_file.write(f'The mean number of apples eaten is {apple_mean:.2f}\n')
    new_file.write(f'The median number of apples eaten is {apple_median:.2f}\n\n')

    new_file.write(f'The mean number of bananas eaten is {banana_mean:.2f}\n')
    new_file.write(f'The median number of bananas eaten is {banana_median:.2f}\n\n')

    new_file.write(f'The mean number of strawberries eaten is {stawberries_mean:.2f}\n')
    new_file.write(f'The median number of strawberries eaten is {stawberries_median:.2f}\n\n')

    new_file.write(f'The mean number of all fruit eaten is {total_mean:.2f}\n')
    new_file.write(f'The median number of all fruit eaten is {total_median:.2f}\n')

    new_file.close()

