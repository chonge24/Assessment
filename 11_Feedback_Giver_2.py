# testing if it can generate 2 possible numbers representing user score and question amount.
import random


score = random.randint(7, 12)
question_amount = random.randint(1, 7)
score_percent = question_amount/score

# Multiplying by 100 to get the percentage
print(score_percent * 100)
