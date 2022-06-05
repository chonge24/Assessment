# Made 11_Feedback_Giver_1_v3 into a function, so it can be repeated easier
import random
player_score = random.randint(1, 12)
print(player_score)


def feedback_giver(score):

    # If they score less than 3, tell them to look at the answer sheet
    if score <= 3:
        print("You did not do very well.\n"
              "Look at the Answer sheet")

    # If they score between 4 and 7, tell them to look at the answer sheet and aim for 8+
    elif 4 <= score <= 7:
        print("You did well\n"
              "Look at the answers and try aim for 8 or more")

    # If they score 8 or more, tell them they did an amazing job
    else:
        print("You scored more than 8!\n"
              "Amazing Job!")

# Main Routine


play = 'y'
if play == 'y':
    feedback_giver(player_score)
