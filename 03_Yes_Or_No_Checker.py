# Checking to see if they want to do the quiz. The variable 'name' is used as an example #
name = "Joe"

# Asking if they want to continue
continuation = input(f"Hi there, {name}, ready to learn some Māori? Enter 'Y' to continue or 'X' to Exit:").upper()

# If they enter 'X', program will say goodbye
while continuation == 'X':
    print("Goodbye")
# If they don't enter 'Y', program will say goodbye
if continuation != 'Y':
    print("Goodbye")
