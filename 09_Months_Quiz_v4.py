# 08_Maori_Days_Quiz_v3 made into a function so it is easier to repeat in the final

import random


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


# Main routine
score = 0
total_score = months_quiz(score)
print(f"Your total score was {total_score}/12")
