# Made 13_Play_Again_1_v2 into function so it can be repeated
def quiz_again(question_text):
    while True:

        # Ask the user if the have played before
        answer = input(question_text).lower()

        # If they enter 'y', continue
        if answer == "y":
            print("quiz_chooser()\n"
                  "yes_no()")

        # If they enter 'x', quit program and leave goodbye message
        elif answer == "x":
            quit("Thanks for playing Emmanuel's Māori Quiz!\n"
                 "I hope you learned many things!"
                 "Goodbye!")

        # else tell them input is invalid
        else:
            print("Invalid input. Enter 'y' to continue or 'x' to exit")

# Main routine


name = "Emmanuel"
quiz_again(f"You have just finished your first quiz, {name}!\n"
           "Want to try the same quiz or a new one?\n"
           "'Y' to continue or 'X' to exit:")
print("Here are your quiz choices:")
