# Checking to see if they want to do the quiz. The variable 'name' is used as an example #
# Changes made to line 4 of code (excluding the 2 grey lines) because it would constantly say 'goodbye' instead of 'goodbye' and exit #
name = "Joe"
continuation = input(f"Hi there, {name}, ready to learn some Māori? Enter 'Y' to continue or 'N' to Exit:").upper()
while continuation == 'N':
    quit("goodbye")
if continuation == 'Y':
    print("Let's start the quiz!")
 
