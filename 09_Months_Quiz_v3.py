# combined 08_Maori_Days_Quiz with 08_Maori_Days_Quiz_v2 to test if the shuffle works with the quiz

import random

# Variables
player_score = 0
question_number = 0

# List of months
months = [["january", "kohitatea"], ["february", "hui-tanguru"], ["march", "poutute-rangi"], ["april", "paenga-whawha"],
          ["may", "haratua"], ["june", "pipiri"], ["july", "hongongoi"], ["august", "here-turi-koka"],
          ["september", "mahuru"], ["october", "whiringa-a-nuku"], ["november", "whiringa-a-rangi"], ["december", "hakihea"]]

# Shuffling list in a random order.
random.shuffle(months)

# While loop that repeats for all months
while question_number < 12:

    # Asking user the question
    user_answer = input(f"What is '{months[question_number][0]}' in English: ").lower()

    # Checking if the user got the answer right, or wrong.
    if user_answer == months[question_number][1]:
        player_score += 1
        print("You are correct")
    else:
        print("You are incorrect")

    question_number += 1


# Main routine
print(f"Your score was {player_score}/12.")
