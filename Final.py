import random


# Function to test if they want to see answer sheet
def yes_no():
    yesno = input(f"Would you like to see the answer sheet?\n"
                  "Enter 'Y' to see,"
                  "'N' to not see, or 'X' to Exit:").upper()

    # Used while loop to keep asking if they want answer sheet
    while yesno != 'N':

        # If they enter 'X', quit program and leave goodbye message
        if yesno == 'X':
            print("Thanks for playing Emmanuel's Māori Quiz!\n"
                  "I hope you learned many things!")
            quit(formatter("~", "Goodbye"))

        # If they enter 'Y', take them to answer sheet function
        elif yesno == 'Y':
            answer_sheet()
            break

        # If they enter an invalid input, ask them to enter again
        else:
            yesno = input("Invalid input.\n"
                          "Enter 'Y' to see,\n"
                          "'N' to not see, or 'X' to Exit:").upper()


# Function for choosing quiz
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
        choose_quiz = input("Choose one of the options above.\n"
                            "Press enter: ").lower()

        # If they enter '1', take them to the numbers quiz
        if choose_quiz == '1':
            score = 0
            total_score = numbers_quiz(score)
            print(f"Your total score was {total_score}/10")
            score_percent = total_score / 10
            print()
            feedback_giver(score_percent)

        # If they enter '2', take them to the numbers in maori quiz
        elif choose_quiz == '2':
            score = 0
            total_score = maori_numbers_quiz(score)
            print(f"Your total score was {total_score}/10")
            score_percent = total_score / 10
            print()
            feedback_giver(score_percent)

        # If they enter '3' take them to the days quiz
        elif choose_quiz == '3':
            score = 0
            total_score = days_quiz(score)
            print(f"Your total score was {total_score}/7")
            score_percent = total_score / 7
            print()
            feedback_giver(score_percent)

        # If they enter '4', take them to the days in maori quiz
        elif choose_quiz == '4':
            score = 0
            total_score = maori_days_quiz(score)
            print(f"Your total score was {total_score}/7")
            score_percent = total_score / 7
            print()
            feedback_giver(score_percent)

        # If they enter '5', take them to the months quiz
        elif choose_quiz == '5':
            score = 0
            total_score = months_quiz(score)
            print(f"Your total score was {total_score}/12")
            score_percent = total_score / 12
            print()
            feedback_giver(score_percent)

        # If they enter '6', take them to the months in maori quiz
        elif choose_quiz == '6':
            score = 0
            total_score = maori_months_quiz(score)
            print(f"Your total score was {total_score}/12")
            score_percent = total_score / 12
            print()
            feedback_giver(score_percent)

        # If they enter 'x', quit the program
        elif choose_quiz == 'x':
            print("Thanks for playing Emmanuel's Māori Quiz!\n"
                  "I hope you learned many things!")
            quit(formatter("~", "Goodbye"))
        # If the user enters an invalid answer,
        # output 'Please enter a valid answer'
        else:
            print("Invalid input.\n"
                  "Please enter an option from below.")
            choose_quiz = 0


def numbers_quiz(_quiz_score):
    # Variables
    player_score = 0
    question_number = 0

    # List of numbers
    numbers = [['1', "tahi"], ['2', "rua"], ['3', "toru"],
               ['4', "wha"], ['5', "rima"], ['6', "ono"],
               ['7', "whitu"], ['8', "waru"], ['9', "iwa"], ['10', "tekau"]]

    # Shuffling the list in a random order
    random.shuffle(numbers)

    # Looping test for all numbers between 1-10.
    while question_number < 10:

        # Asking user the question.
        user_answer = input(f"What is the number\n"
                            f"'{numbers[question_number][0]}' in Maori: ").lower()

        # Checking if the user got the question right, or wrong.
        if user_answer == numbers[question_number][1]:
            player_score += 1
            print(formatter("+", "You are correct"))
        else:
            print(formatter("!", "You are incorrect"))

        # Increasing the question number by 1 each time
        question_number += 1
    return player_score


def maori_numbers_quiz(_quiz_score):
    # Variables
    player_score = 0
    question_number = 0

    # List of numbers in Maori
    maori_numbers = [["tahi", '1'], ["rua", '2'], ["toru", '3'],
                     ["wha", '4'], ["rima", '5'], ["ono", '6'],
                     ["whitu", '7'], ["waru", '8'], ["iwa", '9'], ["tekau", '10']]

    # Shuffling the list in a random order
    random.shuffle(maori_numbers)

    # Looping test for all numbers between 1-10
    while question_number < 10:

        # Asking user the question.
        user_answer = input(f"What is maori word" f"'{maori_numbers[question_number][0]}' in numbers: ")

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

    # If they score less than 40%, give them feedback and suggest to look at the answer sheet
    if score_percent <= 0.4:
        print("Unlucky, you got less than 40% correct.\n"
              "Try looking at the answer sheet to help.\n"
              "")

    # If they score between 40.1% and 70%, give them feedback and encourage them to try beat their score
    elif 0.401 <= score_percent <= 0.7:
        print(f"Well done! Your score was {score_percent *100}%\n"
              f"Look at the Answer sheet and try beat your score!")

    # If they score 100%, say they're amazing and suggest them to do another quiz.
    elif score_percent == 1:
        print("You're amazing! You scored 100%\n"
              "Try playing another quiz")

    # If they score between 70.1% and 99.99%, give them feedback and encourage to try beat their score
    else:
        print(f"Great Job! You scored {score_percent * 100}%!\n"
              "Play again and try beat your score!\n"
              "")


def quiz_again(question_text):
    while True:

        # Ask the user if they want to play again
        answer = input(question_text).lower()

        # If they enter 'y', continue
        if answer == "y":
            return answer

        # If they enter 'x', quit and leave a goodbye message
        elif answer == "x":
            print("Thanks for playing Emmanuel's Māori Quiz!\n"
                  "I hope you learned many things!")
            quit(formatter("~", "Goodbye"))

        # else tell them input is invalid
        else:
            print("Invalid input. Enter 'y' to continue or 'x' to exit")


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
              "Enter 'x' to quit\n"
              "Enter 'n' when you finish looking")
        answers = input("Choose one of the options above and press enter: ").lower()

        # If they enter '1', print the answer sheet for Numbers to numbers in Māori
        if answers == '1':
            print([['1', "tahi"], ['2', "rua"], ['3', "toru"], ['4', "wha"], ['5', "rima"], ['6', "ono"],
                   ['7', "whitu"], ['8', "waru"], ['9', "iwa"], ['10', "tekau"]])
            break

        # If they enter '2', print the answer sheet for Numbers in Māori to numbers
        elif answers == '2':
            print([["tahi", '1'], ["rua", '2'], ["toru", '3'], ["wha", '4'], ["rima", '5'], ["ono", '6'],
                   ["whitu", '7'], ["waru", '8'], ["iwa", '9'], ["tekau", '10']])
            break

        # If they enter '3', print the answer sheet for Days to days in Māori
        elif answers == '3':
            print([["monday", "rahina"], ["tuesday", "ratu"], ["wednesday", "raapa"], ["thursday", "rapare"],
                   ["friday", "ramere"], ["saturday", "rahoroi"], ["sunday", "ratapu"]])
            break

        # If they enter '4', print the answer sheet for Days in Māori to days
        elif answers == '4':
            print([["rahina", "monday"], ["ratu", "tuesday"], ["raapa", "wednesday"], ["rapare", "thursday"],
                   ["ramere", "friday"], ["rahoroi", "saturday"], ["ratapu", "sunday"]])
            break

        # If they enter '5', print the answer sheet for Months to months in Māori
        elif answers == '5':
            print([["january", "kohitatea"], ["february", "hui-tanguru"], ["march", "poutute-rangi"],
                   ["april", "paenga-whawha"], ["may", "haratua"], ["june", "pipiri"], ["july", "hongongoi"],
                   ["august", "here-turi-koka"], ["september", "mahuru"], ["october", "whiringa-a-nuku"],
                   ["november", "whiringa-a-rangi"], ["december", "hakihea"]])
            break

        # If they enter '6', print the answer sheet for Months in Māori to months
        elif answers == '6':
            print([["kohitatea", "january"], ["hui-tanguru", "february"], ["poutute-rangi", "march"],
                   ["paenga-whawha", "april"], ["haratua", "may"], ["pipiri", "june"], ["hongongoi", "july"],
                   ["here-turi-koka", "august"], ["mahuru", "september"], ["whiringa-a-nuku", "october"],
                   ["whiringa-a-rangi", "november"], ["hakihea", "december"]])
            break
        # If they enter 'x', exit program, saying "goodbye"
        elif answers == 'x':
            quit("goodbye")

        # When they finish looking at the answers, they press 'n', leading onto the next part of program
        elif answers == 'n':
            print()

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


# Print welcome messages
print("Welcome to Emmanuel's Māori Quiz\n"
      "The purpose of this program is to help primary school children learn Māori.\n"
      "I hope you learn many things here!\n"
      "There will be quizzes about numbers, days, or months!\n"
      "You can choose for the question answer to be in number/English or Māori.\n"
      "After you complete your quiz, I will tell you how many questions you answered correctly and how you can practice.\n"
      "You can choose to do the quiz again or exit.\n"
      "")

# Ask for their name and age
name = input("Please enter your name:")
valid = False
while not valid:
    try:
        # Ask user for their name and age
        age = int(input("Please enter your age:"))

        # If they are too young, exit program
        if age < 5:
            quit(formatter(":", "Sorry, you are too young."))

        # If they are too old, exit program
        elif age > 11:
            quit(formatter(":", "Sorry, you are too old."))

        # If they are old enough, continue
        else:
            valid = True
    # If they did not enter an integer, tell them they did not enter their age.
    except ValueError:
        print(formatter("#", "You did not enter your age"))

# Asking if they want to continue
continuation = input(f"Hi there, {name}, ready to learn some Māori?\n"
                     "Enter 'Y' to continue or 'X' to Exit:\n"
                     "").upper()

# If they enter 'Y', continue
while continuation != 'Y':

    # If they enter 'X', quit program
    if continuation == 'X':
        quit(formatter("~", "Goodbye"))

    # If they do not enter 'Y' or 'X", tell them invalid input and ask them to enter again.
    else:
        continuation = input("Invalid input. Enter 'Y' to continue or 'N' to exit:").upper()
print(formatter("-", "Let's start the quiz!"))
quiz_chooser()
yes_no()

# Asking if they want to play again.
play_again = input(f"You have finished your first quiz, {name}!\n"
                   "Want to try the same quiz or a new one?\n"
                   "'Y' to continue or 'X' to exit:").lower()

# If they enter 'x', quit program and leave goodbye message.
while play_again != "x":

    # If they enter 'y' take them back to quiz chooser to play another quiz
    if play_again == "y":
        quiz_chooser()
        yes_no()

    # If they do not enter 'x' or 'y', say invalid input and ask them to enter again.
    else:
        print("Invalid input.")
    play_again = input("You have finished a quiz! Enter 'Y' to continue or 'X' to exit:").lower()
    print()
print("Thanks for playing Emmanuel's Māori Quiz!\n"
      "I hope you learned many things!")
quit(formatter("~", "Goodbye"))
