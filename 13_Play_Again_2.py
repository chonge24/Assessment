# Name is used as an example. Based on 03_Yes_Or_No_Checker_v3
# the two unused functions represents what is in there for the final program
name = "Emmanuel"
play_again = input(f"You have finished your first quiz, {name}!\n"
                   "Want to try the same quiz or a new one?\n"
                   "'Y' to continue or 'X' to exit:").lower()
# while loop so that it keeps asking if they want to play again unless 'x' is entered
while play_again != "x":

    # If they enter 'y', call the functions
    if play_again == "y":
        print("quiz_chooser()\n"
              "yes_no()")

    # If they enter an invalid input, ask again. This is also where the code goes to after the 2 functions finish.
    else:
        print("Invalid input.")
    play_again = input("You have finished a quiz! Enter 'Y' to continue or 'X' to exit:").lower()
    print()

# If they got to this point, they played at least 1 quiz. Thank them and say goodbye
quit("Thanks for playing Emmanuel's Māori Quiz!\n"
     "I hope you learned many things!\n"
     "Goodbye!")
