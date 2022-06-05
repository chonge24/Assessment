name = "Joe"
# Ask the user if they want to play again
play_again = input(f"You have just finished your first quiz, {name}!\n"
                   "Want to try the same quiz or a new one?\n"
                   "'Y' to continue or 'N' to exit:").upper()

# If they say yes, output 'Program Continues'
if play_again == "Y":
    print("Here are the quiz choices:")

# If they say no, output 'Display Instructions'
elif play_again == "X":
    quit("Thanks for playing Emmanuel's Māori Quiz!\n"
         "I hope you learned many things!"
         "Goodbye!")

# Otherwise - show error message
else:
    print("Invalid Input.\n"
          "Please enter 'Y' to play again or 'X' to exit:")
