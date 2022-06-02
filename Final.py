import sys
import random


def yes_no(question_text):
    while True:

        # Ask the user if the have played before
        answer = input(question_text).upper()

        # If they say yes, output 'Program Continues'
        if answer == "Y" or answer == "YES":
            answer = "Yes"
            return answer

        # If they say no, output 'Display Instructions'
        elif answer == "N" or answer == "NO":
            answer = "No"
            quit("Goodbye")

        # Otherwise - show error
        else:
            print("Invalid input. Enter 'Y' to continue or 'N' to exit")


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
        choose_quiz = input("Choose one of the options above and press enter: ")

        if choose_quiz == '1':
            score = 0
            total_score = numbers_quiz(score)
            print(f"Your total score was {total_score}/10")
            print()
            feedback_giver(total_score)

        elif choose_quiz == '2':
            score = 0
            total_score = maori_numbers_quiz(score)
            print(f"Your total score was {total_score}/10")
            print()
            feedback_giver(total_score)

        elif choose_quiz == '3':
            score = 0
            total_score = days_quiz(score)
            print(f"Your total score was {total_score}/7")
            print()
            feedback_giver(total_score)

        elif choose_quiz == '4':
            score = 0
            total_score = maori_days_quiz(score)
            print(f"Your total score was {total_score}/7")
            print()
            feedback_giver(total_score)

        elif choose_quiz == '5':
            score = 0
            total_score = months_quiz(score)
            print(f"Your total score was {total_score}/12")
            print()
            feedback_giver(total_score)

        elif choose_quiz == '6':
            score = 0
            total_score = maori_months_quiz(score)
            print(f"Your total score was {total_score}/12")
            print()
            feedback_giver(total_score)

        elif choose_quiz == 'x':
            quit("goodbye")
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
            print("you are correct")
        else:
            print("You are incorrect")

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
            print("you are correct")
        else:
            print("You are incorrect")

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
            print("you are correct")
        else:
            print("You are incorrect")

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
            print("you are correct")
        else:
            print("You are incorrect")

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
            print("you are correct")
        else:
            print("You are incorrect")

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
            print("you are correct")
        else:
            print("You are incorrect")

        # Increasing the question number by 1 every time the while loop 'loops'.
        question_amount += 1
    return player_score


def feedback_giver(score):
    if score <= 3:
        print("You did not do very well.\n"
              "Look at the Answer sheet")
    elif 4 <= score <= 7:
        print("You did well\n"
              "Look at the answers and try aim for 8 or more")
    else:
        print("You scored more than 8!\n"
              "Good Job!")

# Main routine


print("Welcome to Emmanuel's Māori Quiz\n"
      "The purpose of this program is to help people learn Māori.\n"
      "I hope you learn many things here!\n"
      "There will be a quiz of numbers 1-10 in Māori\n"
      "You can choose for the question answer to be in number/English or Māori.\n"
      "You can choose how many questions there are.\n"
      "After you complete your quiz, I will tell you how many questions you answered correctly and how you can practice.\n"
      "You can choose to do the quiz again or exit.\n")
name = input("Enter your name:")
age = input("Enter your age:")
while type(age) != int:
    age = int(input("Invalid input. Please enter your age:"))
if 5 <= age <= 11:
      print("You are of Primary school age.")
else:
    sys.exit(f"Sorry, {name} you are not of primary school age.")
continuation = yes_no("Do you want to continue?\n"
                      "Enter 'Y' to Continue or 'N' to exit.")
quiz_chooser()
