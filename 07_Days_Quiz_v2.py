# making 07_days_quiz into a quiz. tested without having a shuffle to see if it can ask and check questions


question_number = 0
# List of days
days = [["monday", "rahina"], ["tuesday", "ratu"], ["wednesday", "raapa"], ["thursday", "rapare"],
        ["friday", "ramere"], ["saturday", "rahoroi"], ["sunday", "ratapu"]]

# While loop that repeats for all days
while question_number < 7:

    # Asking the user the question.
    user_answer = input(f"What is '{days[question_number][0]}' in Maori: ").lower()

    # Checking Users answer.
    if user_answer == days[question_number][1]:
        print("You are correct")
    else:
        print("You are incorrect")
    question_number += 1
