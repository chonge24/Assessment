# Checking to see if they want to do the quiz. The variable 'name' is used as an example #
# Changes from version 2 to make it detect if there's an invalid input #
name = "Emmanuel"

# Asking if they want to continue
continuation = input(f"Hi there, {name}, ready to learn some Māori?\n"
                     "Enter 'Y' to continue or 'X' to Exit:").upper()

# Used a while loop for when the answer is not 'Y'.
while continuation != 'Y':

    # If they enter 'X', quit program.
    if continuation == 'X':
        quit("Goodbye")

    # If they enter an invalid input, ask them to enter again.
    else:
        continuation = input("Invalid input. Enter 'Y' to continue or 'X' to exit:").upper()
print("Let's start the quiz!")
