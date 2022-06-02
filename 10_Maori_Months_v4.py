# 08_Maori_Days_Quiz_v3 made into a function so it is easier to repeat in the final

import random


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


# Main routine
score = 0
total_score = maori_months_quiz(score)
print(f"Your total score was {total_score}/12")
