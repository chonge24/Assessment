def play_quiz():
    print("You can choose the following quizzes:")
    print("Enter '1' for Numbers to numbers in Māori or")
    print("Enter '2' for Numbers in Māori to numbers or")
    print("Enter '3' for Days to days in Māori or")
    print("Enter '4' for Days in Māori to days or")
    print("Enter '5' for Months to months in Māori or")
    print("Enter '6' for Months in Māori to months")
    quiz_choice = int(input("Which test would you like:"))
    if quiz_choice == 1:
        print("You have chosen Numbers to numbers in Māori.")
    elif quiz_choice == 2:
        print("You have chosen numbers in Māori to numbers")
    elif quiz_choice == 3:
        print("You have chosen days in English to days in Māori")
    elif quiz_choice == 4:
        print("You have chosen days in Māori to days in English")
    elif quiz_choice == 5:
        print("You have chosen months in English to months in Māori")
    elif quiz_choice == 6:
        print("You have chosen months in Māori to months in English")
    else:
        int(input("You have not entered any of the numbers representing a quiz. Please enter a number between 1 and 6:"))
