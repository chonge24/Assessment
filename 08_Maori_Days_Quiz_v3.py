# combined 08_Maori_Days_Quiz with 08_Maori_Days_Quiz_v2 to test if the shuffle works with the quiz

import random

# Variables
player_score = 0
question_number = 0

# List of maori days
maori_days = [["rahina", "monday"], ["ratu", "tuesday"], ["raapa", "wednesday"], ["rapare", "thursday"],
              ["ramere", "friday"], ["rahoroi", "saturday"], ["ratapu", "sunday"]]

# Shuffling list in a random order.
random.shuffle(maori_days)

# While loop that repeats for all days
while question_number < 7:

    # Asking user the question
    user_answer = input(f"What is '{maori_days[question_number][0]}' in English: ").lower()

    # Checking if the user got the answer right, or wrong.
    if user_answer == maori_days[question_number][1]:
        player_score += 1
        print("You are correct")
    else:
        print("You are incorrect")

    question_number += 1


# Main routine
print(f"Your score was {player_score}/7.")
