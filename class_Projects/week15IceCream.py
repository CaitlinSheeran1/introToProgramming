

ice_cream = {'Vanilla': 3, 'Chocalte': 4, "Strawberry": 5}

done = False

while not done:
    
    user_input = input("Pick a flavor of icecream you want: ")
        if user_input in ice_cream:
            print(f"{user_input} is {ice_cream[user_input]} dollars!")
        else:
            print(f"You picked an invalid falvour, we are currently out of {user_input}")
            print(f"The falvours we have are {ice_cream.values()}")
    #except:
    #    print(f"You picked an invalid falvour, we are currently out of {user_input}")
    #    print(f"The falvours we have are {ice_cream.values()}")
    #else:
    print(f"Now give me money!")
    done = True
            