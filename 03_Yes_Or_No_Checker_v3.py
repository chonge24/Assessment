# Checking to see if they want to do the quiz. The variable 'name' is used as an example #
# Changes from version 2 to make it detect if there's an invalid input #
name = "Emmanuel"

# Asking if they want to continue
continuation = input(f"Hi there, {name}, ready to learn some Māori?\n"
                     "Enter 'Y' to continue or 'X' to Exit:").lower()

# Used a while loop for when the answer is not 'y'.
while continuation != 'y':

    # If they enter 'X', quit program.
    if continuation == 'x':
        quit("Goodbye")

    # If they enter an invalid input, ask them to enter again.
    else:
        continuation = input("Invalid input. Enter 'y' to continue or 'x' to exit:").lower()
print("Let's start the quiz!")
