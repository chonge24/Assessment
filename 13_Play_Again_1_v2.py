# testing in while loop
name = "Emmanuel"
play_again = ""
while play_again != "random word":
    # Ask the user if the have played before
    play_again = input(f"You have just finished your first quiz, {name}!\n"
                       "Want to try the same quiz or a new one?\n"
                       "'Y' to continue or 'N' to exit:").lower()

    # If they enter 'y', continue
    if play_again == "y":
        print("Here are the quiz choices:")

    # If they enter 'x', quit and leave goodbye message
    elif play_again == "x":
        quit("Thanks for playing Emmanuel's Māori Quiz!\n"
             "I hope you learned many things!"
             "Goodbye!")

    # else tell them input is invalid
    else:
        print("Invalid input.\n"
              "Please Enter 'y' to play again or 'x' to exit")
