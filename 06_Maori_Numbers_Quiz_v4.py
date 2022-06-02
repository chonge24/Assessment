# 06_maori_numbers_quiz_v3 made into a function so it is easier to repeat in the final

import random


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


# Main routine
score = 0
total_score = maori_numbers_quiz(score)
print(f"Your total score was {total_score}/10")
