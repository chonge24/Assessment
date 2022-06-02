# combined 07_Days_Quiz with 07_Days_Quiz_v2 to test if the shuffle works with the quiz

import random

# Variables
player_score = 0
question_number = 0

# List of days
days = [["monday", "rahina"], ["tuesday", "ratu"], ["wednesday", "raapa"], ["thursday", "rapare"],
        ["friday", "ramere"], ["saturday", "rahoroi"], ["sunday", "ratapu"]]

# Shuffling list in a random order
random.shuffle(days)

# While loop that repeats for all days
while question_number < 7:

    # Asking user the question
    user_answer = input(f"What is '{days[question_number][0]}' in Maori: ").lower()

    # Checking if the user got the answer right, or wrong.
    if user_answer == days[question_number][1]:
        player_score += 1
        print("You are correct")
    else:
        print("You are incorrect")

    question_number += 1


# Main routine
print(f"Your score was {player_score}/7.")
