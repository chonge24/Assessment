# making 06_maori_numbers_quiz into a quiz. tested without having a shuffle to see if it can ask and check questions


question_number = 0
# List of numbers in Maori
maori_numbers = [["tahi", '1'], ["rua", '2'], ["toru", '3'], ["wha", '4'], ["rima", '5'], ["ono", '6'],
                 ["whitu", '7'], ["waru", '8'], ["iwa", '9'], ["tekau", '10']]

# While loop that repeats for all numbers 1-10
while question_number < 10:

    # Asking the user the question.
    user_answer = input(f"What is the maori word {maori_numbers[question_number][0]} in numbers: ")

    # Checking Users answer.
    if user_answer == maori_numbers[question_number][1]:
        print("You are correct")
    else:
        print("You are incorrect")
    question_number += 1
