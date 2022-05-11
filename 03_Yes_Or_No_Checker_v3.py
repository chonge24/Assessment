# Checking to see if they want to do the quiz. The variable 'name' is used as an example #
# Changes made to line 4 of code (excluding the 2 grey lines) because it would constantly say 'goodbye' instead of 'goodbye' and exit #
# Changes from version 2 to make the code shorter #
name = "Joe"
continuation = input(f"Hi there, {name}, ready to learn some Māori? Enter 'Y' to continue or 'N' to Exit:").upper()
if continuation != 'Y':
    continuation = input("Invalid input. Enter 'Y' to continue or 'N' to exit")
elif continuation == 'N':
    quit("Goodbye")
else:
    print("Let's start the quiz!")
