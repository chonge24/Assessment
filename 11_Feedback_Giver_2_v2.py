# testing if it can generate 2 possible numbers representing user score and question amount.
# Made it a function from 11_Feedback_Giver_2_v2
# Unlikely to get 100% on this trial, but it works according to how I plan
import random


score = random.randint(7, 12)
question_amount = random.randint(1, 7)
score_percent = question_amount/score


def feedback_giver():

    # If they score less than 40%, suggest they look at the answer sheet
    if score_percent <= 0.4:
        print("Unlucky, you got less than 40% correct.\n"
              "Try looking at the answer sheet to help.\n"
              "")

    # If they score between 40.1% and 70%, encourage them and push them to beat their score
    elif 0.401 <= score_percent <= 0.7:
        print(f"Well done! Your score was {score_percent *100}%\n"
              f"Look at the Answer sheet and try beat your score!")

    # If they score 100%, suggest them to try another quiz.
    elif score_percent == 1:
        print("You're amazing at this! You scored 100%\n"
              "Try another quiz!")

    # If they score between 70% and 99.999%, encourage them to try get 100%
    else:
        print(f"Great Job! You scored {score_percent * 100}%!\n"
              "Play again and try get 100%!\n"
              "")


feedback_giver()
