# 08_Maori_Days_Quiz_v3 made into a function so it is easier to repeat in the final

import random


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
        user_answer = input(f"What is the maori word '{maori_days[question_number][0]}' in English: ").lower()

        # Checking if the user got the question right, or wrong.
        if user_answer == maori_days[question_number][1]:
            player_score += 1
            print("you are correct")
        else:
            print("You are incorrect")

        # Increasing the question number by 1 every time the while loop 'loops'.
        question_number += 1
    return player_score


# Main routine
score = 0
total_score = maori_days_quiz(score)
print(f"Your total score was {total_score}/7")
