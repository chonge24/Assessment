# Made 03_Yes_Or_No_Checker_v3 into a function for use of answer sheet in final
name = "Emmanuel"


def yes_no():
    continuation = input(f"Hi there, {name}, ready to learn some Māori?\n"
                         "Enter 'Y' to continue or 'X' to Exit:").upper()

    while continuation != 'Y':
        # If they enter 'X', quit program.
        if continuation == 'X':
            quit("Goodbye")

        # If they enter an invalid input, ask them to enter again.
        else:
            continuation = input("Invalid input. Enter 'Y' to continue or 'X' to exit:").upper()
    print("Let's start the quiz!")
