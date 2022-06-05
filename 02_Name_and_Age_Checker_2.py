# 02_Name_and_Age_Checker Trial 2
# Struggled to make a value checker to say 'invalid input'. searched on google and I found this method
valid = False
while not valid:
    try:
        # Ask user for their name and age.
        name = input("Please enter your name:")
        age = int(input("Please enter your age:"))

        # If they are too young, exit program.
        if age < 5:
            quit("Sorry, you are too young.")

        # If they are too old, exit program.
        elif age > 11:
            quit("Sorry, you are too old.")

        # If they are old enough, continue.
        else:
            valid = True

    # If they do not input an integer, ask them again
    except ValueError:
        print("You did not enter your age\n")
        age = int(input("Please enter your age:"))
