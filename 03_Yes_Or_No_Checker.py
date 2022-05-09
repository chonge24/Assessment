# Checking to see if they want to do the quiz. The variable 'name' is used as an example #
name = "Joe"
continuation = input(f"Hi there, {name}, ready to learn some Māori? Enter 'Y' to continue or 'N' to Exit:").upper()
while continuation == 'N':
    print("Goodbye")
if continuation == 'Y':
    print("Let's start the quiz!")
