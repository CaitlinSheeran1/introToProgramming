
done = False

while not done:

    try:
        user_number = int(input("Give me a number: "))
        fun_number = 10/user_number
        pass

    except ZeroDivisionError:
        print("Do not pick a zero!")

    except ValueError:
        print("Must pick a number")

    else:
        print(f"The fun number is {fun_number}")
        done = True







