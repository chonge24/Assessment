# combined 06_maori_numbers_quiz with 06_maori_numbers_quiz_v2 to test if the shuffle works with the quiz

import random

# Variables
player_score = 0
question_number = 0

# List of numbers in Maori
maori_numbers = [["tahi", '1'], ["rua", '2'], ["toru", '3'], ["wha", '4'], ["rima", '5'], ["ono", '6'],
                 ["whitu", '7'], ["waru", '8'], ["iwa", '9'], ["tekau", '10']]

# Shuffling list in a random order.
random.shuffle(maori_numbers)

# While loop that repeats for all numbers between 1-10
while question_number < 10:

    # Asking user the question
    user_answer = input(f"What is the maori word '{maori_numbers[question_number][0]}' in numbers: ")

    # Checking if the user got the answer right, or wrong.
    if user_answer == maori_numbers[question_number][1]:
        player_score += 1
        print("You are correct")
    else:
        print("You are incorrect")

    question_number += 1


# Main routine
print(f"Your score was {player_score}/10.")
