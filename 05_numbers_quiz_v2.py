# making 05_numbers_quiz into a quiz. tested without having a shuffle to see if it can ask questions


question_number = 0
# List of numbers
numbers = [['1', "tahi"], ['2', "rua"], ['3', "toru"], ['4', "wha"], ['5', "rima"], ['6', "ono"],
           ['7', "whitu"], ['8', "waru"], ['9', "iwa"], ['10', "tekau"]]

# While loop that repeats for all numbers
while question_number < 10:

    # Asking the user the question.
    user_answer = input(f"What is the number {numbers[question_number][0]} in Maori: ").lower()

    # Checking Users answer.
    if user_answer == numbers[question_number][1]:
        print("You are correct")
    else:
        print("You are incorrect")
    question_number += 1
