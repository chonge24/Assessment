def quiz_again(question_text):
    while True:

        # Ask the user if the have played before
        answer = input(question_text).upper()

        # If they say yes, output 'Program Continues'
        if answer == "Y":
            return answer

        # If they say no, output 'Display Instructions'
        elif answer == "X":
            quit("Goodbye")

        # Otherwise - show error
        else:
            print("Invalid input. Enter 'Y' to continue or 'N' to exit")

# Main routine


name = "Joe"
quiz_again(f"You have just finished your first quiz, {name}!\n"
           "Want to try the same quiz or a new one?\n"
           "'Y' to continue or 'X' to exit:").upper()
print("Here are your quiz choices:")
