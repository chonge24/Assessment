import random
def guess_check(question, answer):
    global score
    question_amount = int(input("How many questions would you like:"))
    attempt = 0
    question = true

    while question and attempt > 2:
        if question.lower() == answer.lower():
            print("Correct")
            score += 1
            question = false
        else:
            if attempt < 1:
                print("Incorrect")
                attempt += 1
maori_numbers = ["tahi", "rua", "toru", "whā", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
x = random.choice(maori_numbers)
print(f"what is {x}?")
