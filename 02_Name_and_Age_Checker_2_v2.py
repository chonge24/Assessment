# 02_Name_and_Age_Checker Trial 2
# Changes made to 02_Name_and_Age_Checker_v4 in except ValueError. If I did a value error more than twice, it would
# crash the program. I figured it was the age input in line 23 (which has been deleted) so I deleted it and now it
# works.
name = input("Enter your name:")
valid = False
while not valid:
    try:
        # Ask user for their name and age
        age = int(input("Please enter your age:"))

        # If they are too young, exit program
        if age < 5:
            quit(f"Sorry, {name}, you are too young.")

        # If they are too old, exit program
        elif age > 11:
            quit(f"Sorry, {name}, you are too old.")

        # If they are old enough, continue
        else:
            valid = True
            print(f"Hi there, {name}, ready to learn some Māori?\n"
                  "Enter 'Y' to continue or 'X' to Exit:")

    # If they do not input an integer, ask them again
    except ValueError:
        print("You did not enter your age\n")
