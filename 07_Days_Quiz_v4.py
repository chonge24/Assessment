# 07_Days_Quiz_v3 made into a function so it is easier to repeat in the final

import random


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


# Main routine
score = 0
total_score = days_quiz(score)
print(f"Your total score was {total_score}/7")
