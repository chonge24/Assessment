# Made 11_Feedback_v3 into a function, so it can be repeated easier
import random
player_score = random.randint(1,12)
print(player_score)


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

# Main Routine


play = 'y'
if play == 'y':
    feedback_giver(player_score)
