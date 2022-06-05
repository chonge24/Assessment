# Putting together 11_Feedback and 11_Feedback_Giver_1_v2 together for a fully functioning Feedback Giver
import random
score = random.randint(1, 12)
print(score)
if score <= 3:
    print("You did not do very well.\n"
          "Try looking at the Answer sheet")
elif 4 <= score <= 7:
    print("You did well\n"
          "Look at the answers and try aim for 8 or more")
else:
    print("You scored more than 8!\n"
          "Did you get all of them right?")
