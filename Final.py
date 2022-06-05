import random


def yes_no():
    yesno = input(f"Would you like to see the answer sheet?\n"
                  "Enter 'Y' to see, 'N' to not see, or 'X' to Exit:").upper()
    while yesno != 'N':
        if yesno == 'X':
            quit("Goodbye")

        elif yesno == 'Y':
            answer_sheet()
        else:
            yesno = input("Invalid input. Enter 'Y' to see, 'N' to not see, or 'X' to Exit:").upper()


def quiz_chooser():
    choose_quiz = 0
    while choose_quiz == 0:
        # Ask the user which quiz they want to choose
        print("You can choose the following quizzes:\n"
              "Enter '1' for Numbers to numbers in Māori\n"
              "Enter '2' for Numbers in Māori to numbers\n"
              "Enter '3' for Days to days in Māori\n"
              "Enter '4' for Days in Māori to days\n"
              "Enter '5' for Months to months in Māori\n"
              "Enter '6' for Months in Māori to months\n"
              "Enter 'x' to quit")
        choose_quiz = input("Choose one of the options above and press enter: ").lower()

        if choose_quiz == '1':
            score = 0
            total_score = numbers_quiz(score)
            print(f"Your total score was {total_score}/10")
            score_percent = total_score / 10
            print()
            feedback_giver(score_percent)

        elif choose_quiz == '2':
            score = 0
            total_score = maori_numbers_quiz(score)
            print(f"Your total score was {total_score}/10")
            score_percent = total_score / 10
            print()
            feedback_giver(score_percent)

        elif choose_quiz == '3':
            score = 0
            total_score = days_quiz(score)
            print(f"Your total score was {total_score}/7")
            score_percent = total_score / 7
            print()
            feedback_giver(score_percent)

        elif choose_quiz == '4':
            score = 0
            total_score = maori_days_quiz(score)
            print(f"Your total score was {total_score}/7")
            score_percent = total_score / 7
            print()
            feedback_giver(score_percent)

        elif choose_quiz == '5':
            score = 0
            total_score = months_quiz(score)
            print(f"Your total score was {total_score}/12")
            score_percent = total_score / 12
            print()
            feedback_giver(score_percent)

        elif choose_quiz == '6':
            score = 0
            total_score = maori_months_quiz(score)
            print(f"Your total score was {total_score}/12")
            score_percent = total_score / 12
            print()
            feedback_giver(score_percent)

        elif choose_quiz == 'x':
            quit(formatter("~", "goodbye"))
        # If the user enters an invalid answer, output 'Please enter a valid answer'
        else:
            print("Invalid input.\n"
                  "Please enter an option from below.")
            choose_quiz = 0


def numbers_quiz(_quiz_score):
    # Variables
    player_score = 0
    question_number = 0

    # List of numbers
    numbers = [['1', "tahi"], ['2', "rua"], ['3', "toru"], ['4', "wha"], ['5', "rima"], ['6', "ono"],
               ['7', "whitu"], ['8', "waru"], ['9', "iwa"], ['10', "tekau"]]

    # Shuffling the list in a random order
    random.shuffle(numbers)

    # Looping test for all numbers between 1-10.
    while question_number < 10:

        # Asking user the question.
        user_answer = input(f"What is the number '{numbers[question_number][0]}' in Maori: ").lower()

        # Checking if the user got the question right, or wrong.
        if user_answer == numbers[question_number][1]:
            player_score += 1
            print(formatter("+", "You are correct"))
        else:
            print(formatter("!", "You are incorrect"))

        # Increasing the question number by 1 every time the while loop 'loops'.
        question_number += 1
    return player_score


def maori_numbers_quiz(_quiz_score):
    # Variables
    player_score = 0
    question_number = 0

    # List of numbers in Maori
    maori_numbers = [["tahi", '1'], ["rua", '2'], ["toru", '3'], ["wha", '4'], ["rima", '5'], ["ono", '6'],
                     ["whitu", '7'], ["waru", '8'], ["iwa", '9'], ["tekau", '10']]

    # Shuffling the list in a random order
    random.shuffle(maori_numbers)

    # Looping test for all numbers between 1-10
    while question_number < 10:

        # Asking user the question.
        user_answer = input(f"What is maori word '{maori_numbers[question_number][0]}' in numbers: ")

        # Checking if the user got the question right, or wrong.
        if user_answer == maori_numbers[question_number][1]:
            player_score += 1
            print(formatter("+", "You are correct"))
        else:
            print(formatter("!", "You are incorrect"))

        # Increasing the question number by 1 every time the while loop 'loops'.
        question_number += 1
    return player_score


def days_quiz(_quiz_score):
    # Variables
    player_score = 0
    question_number = 0

    # List of days
    days = [["monday", "rahina"], ["tuesday", "ratu"], ["wednesday", "raapa"], ["thursday", "rapare"],
            ["friday", "ramere"], ["saturday", "rahoroi"], ["sunday", "ratapu"]]

    # Shuffling the list in a random order
    random.shuffle(days)

    # Looping test for all days
    while question_number < 7:

        # Asking user the question.
        user_answer = input(f"What is '{days[question_number][0]}' in Maori: ").lower()

        # Checking if the user got the question right, or wrong.
        if user_answer == days[question_number][1]:
            player_score += 1
            print(formatter("+", "You are correct"))
        else:
            print(formatter("!", "You are incorrect"))

        # Increasing the question number by 1 every time the while loop 'loops'.
        question_number += 1
    return player_score


def maori_days_quiz(_quiz_score):
    # Variables
    player_score = 0
    question_number = 0

    # List of maori days
    maori_days = [["rahina", "monday"], ["ratu", "tuesday"], ["raapa", "wednesday"], ["rapare", "thursday"],
                  ["ramere", "friday"], ["rahoroi", "saturday"], ["ratapu", "sunday"]]

    # Shuffling the list in a random order
    random.shuffle(maori_days)

    # Looping test for all days
    while question_number < 7:

        # Asking user the question.
        user_answer = input(f"What is '{maori_days[question_number][0]}' in English: ").lower()

        # Checking if the user got the question right, or wrong.
        if user_answer == maori_days[question_number][1]:
            player_score += 1
            print(formatter("+", "You are correct"))
        else:
            print(formatter("!", "You are incorrect"))

        # Increasing the question number by 1 every time the while loop 'loops'.
        question_number += 1
    return player_score


def months_quiz(_quiz_score):
    # Variables
    player_score = 0
    question_amount = 0

    # List of months
    months = [["january", "kohitatea"], ["february", "hui-tanguru"], ["march", "poutute-rangi"], ["april", "paenga-whawha"],
              ["may", "haratua"], ["june", "pipiri"], ["july", "hongongoi"], ["august", "here-turi-koka"],
              ["september", "mahuru"], ["october", "whiringa-a-nuku"], ["november", "whiringa-a-rangi"], ["december", "hakihea"]]

    # Shuffling the list in a random order
    random.shuffle(months)

    # Looping test for all months
    while question_amount < 12:

        # Asking user the question.
        user_answer = input(f"What is '{months[question_amount][0]}' in Maori: ").lower()

        # Checking if the user got the question right, or wrong.
        if user_answer == months[question_amount][1]:
            player_score += 1
            print(formatter("+", "You are correct"))
        else:
            print(formatter("!", "You are incorrect"))

        # Increasing the question number by 1 every time the while loop 'loops'.
        question_amount += 1
    return player_score


def maori_months_quiz(_quiz_score):
    # Variables
    player_score = 0
    question_amount = 0

    # List of months in Maori
    maori_months = [["kohitatea", "january"], ["hui-tanguru", "february"], ["poutute-rangi", "march"],
                    ["paenga-whawha", "april"], ["haratua", "may"], ["pipiri", "june"], ["hongongoi", "july"],
                    ["here-turi-koka", "august"], ["mahuru", "september"], ["whiringa-a-nuku", "october"],
                    ["whiringa-a-rangi", "november"], ["hakihea", "december"]]

    # Shuffling the list in a random order
    random.shuffle(maori_months)

    # Looping test for all months
    while question_amount < 12:

        # Asking user the question.
        user_answer = input(f"What is '{maori_months[question_amount][0]}' in English: ").lower()

        # Checking if the user got the question right, or wrong.
        if user_answer == maori_months[question_amount][1]:
            player_score += 1
            print(formatter("+", "You are correct"))
        else:
            print(formatter("!", "You are incorrect"))

        # Increasing the question number by 1 every time the while loop 'loops'.
        question_amount += 1
    return player_score


def feedback_giver(score_percent):
    if score_percent <= 0.4:
        print("Unlucky, you got less than 40% correct.\n"
              "Try looking at the answer sheet to help.\n"
              "")

    elif 0.401 <= score_percent <= 0.7:
        print(f"Well done! Your score was {score_percent *100}%\n"
              f"Look at the Answer sheet and try beat your score!")

    elif score_percent == 1:
        print("Well done! You scored 100%")

    else:
        print(f"Great Job! You scored {score_percent * 100}%!\n"
              "Play again and try beat your score!\n"
              "")


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


def answer_sheet():
    answers = 0
    while answers == 0:
        # Ask the user if they want to continue to the quiz.
        print("This is the answer sheet.\n"
              "This is the question and answer [question, answer]\n"
              "e.g, [Monday, Rahina]\n"
              "Enter '1' for Numbers to numbers in Māori\n"
              "Enter '2' for Numbers in Māori to numbers\n"
              "Enter '3' for Days to days in Māori\n"
              "Enter '4' for Days in Māori to days\n"
              "Enter '5' for Months to months in Māori\n"
              "Enter '6' for Months in Māori to months\n"
              "Enter 'x' to quit")
        answers = input("Choose one of the options above and press enter: ")

        if answers == '1':
            print([['1', "tahi"], ['2', "rua"], ['3', "toru"], ['4', "wha"], ['5', "rima"], ['6', "ono"],
                   ['7', "whitu"], ['8', "waru"], ['9', "iwa"], ['10', "tekau"]])
            break

        elif answers == '2':
            print([["tahi", '1'], ["rua", '2'], ["toru", '3'], ["wha", '4'], ["rima", '5'], ["ono", '6'],
                   ["whitu", '7'], ["waru", '8'], ["iwa", '9'], ["tekau", '10']])
            break

        elif answers == '3':
            print([["monday", "rahina"], ["tuesday", "ratu"], ["wednesday", "raapa"], ["thursday", "rapare"],
                   ["friday", "ramere"], ["saturday", "rahoroi"], ["sunday", "ratapu"]])
            break

        elif answers == '4':
            print([["rahina", "monday"], ["ratu", "tuesday"], ["raapa", "wednesday"], ["rapare", "thursday"],
                   ["ramere", "friday"], ["rahoroi", "saturday"], ["ratapu", "sunday"]])
            break

        elif answers == '5':
            print([["january", "kohitatea"], ["february", "hui-tanguru"], ["march", "poutute-rangi"],
                   ["april", "paenga-whawha"], ["may", "haratua"], ["june", "pipiri"], ["july", "hongongoi"],
                   ["august", "here-turi-koka"], ["september", "mahuru"], ["october", "whiringa-a-nuku"],
                   ["november", "whiringa-a-rangi"], ["december", "hakihea"]])
            break

        elif answers == '6':
            print([["kohitatea", "january"], ["hui-tanguru", "february"], ["poutute-rangi", "march"],
                   ["paenga-whawha", "april"], ["haratua", "may"], ["pipiri", "june"], ["hongongoi", "july"],
                   ["here-turi-koka", "august"], ["mahuru", "september"], ["whiringa-a-nuku", "october"],
                   ["whiringa-a-rangi", "november"], ["hakihea", "december"]])
            break

        elif answers == 'x':
            quit("goodbye")
        # If the user enters an invalid answer, output 'Please enter a valid answer'
        else:
            print("Invalid input.\n"
                  "Please enter an option from below.")
            answers = 0


def formatter(symbol, text):
    # The symbol has 3 of it on either side
    sides = symbol * 3
    # it is the 3 on either side with text in the middle
    formatted_text = f"{sides} {text} {sides}"
    # The top and bottom are the symbol repeated
    top_bottom = symbol * len(formatted_text)
    # goes back with three rows
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"

# Main routine


print("Welcome to Emmanuel's Māori Quiz\n"
      "The purpose of this program is to help people learn Māori.\n"
      "I hope you learn many things here!\n"
      "There will be a quiz of numbers 1-10 in Māori\n"
      "You can choose for the question answer to be in number/English or Māori.\n"
      "You can choose how many questions there are.\n"
      "After you complete your quiz, I will tell you how many questions you answered correctly and how you can practice.\n"
      "You can choose to do the quiz again or exit.\n"
      "")
name = input("Please enter your name:")
valid = False
while not valid:
    try:
        # Ask user for their name and age
        age = int(input("Please enter your age:"))

        # If they are too young, exit program
        if age < 5:
            quit("Sorry, you are too young.")

        # If they are too old, exit program
        elif age > 11:
            quit("Sorry, you are too old.")

        # If they are old enough, continue
        else:
            valid = True

    except ValueError:
        print("You did not enter your age\n")
continuation = input(f"Hi there, {name}, ready to learn some Māori?\n"
                     "Enter 'Y' to continue or 'X' to Exit:\n"
                     "").upper()
while continuation != 'Y':
    if continuation == 'X':
        quit("Goodbye")
    else:
        continuation = input("Invalid input. Enter 'Y' to continue or 'N' to exit:").upper()
print("Let's start the quiz!")
quiz_chooser()
yes_no()
play_again = input(f"You have your quiz, {name}!\n"
                   "Want to try the same quiz or a new one?\n"
                   "'Y' to continue or 'X' to exit:").lower()
while play_again != "x":
    if play_again == "y":
        quiz_chooser()
        yes_no()
    else:
        print("Invalid input.")
    play_again = input("Enter 'Y' to continue or 'X' to exit:").lower()
    print()
quit(formatter("~", "Goodbye"))
