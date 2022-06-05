# Checking to see if they want to do the quiz. The variable 'name' is used as an example
# Changes made to line 8 of code because it would constantly say 'goodbye' instead of 'goodbye' and exit
name = "Joe"

# Asking if they want to continue
continuation = input(f"Hi there, {name}, ready to learn some Māori? Enter 'Y' to continue or 'X' to Exit:").upper()

# If they enter 'X', exit program.
if continuation == 'X':
    quit("goodbye")
# If they enter 'Y', continue program
elif continuation == 'Y':
    print("Let's start the quiz!")
 
