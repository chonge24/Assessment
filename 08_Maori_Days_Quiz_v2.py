# making 08_Maori_Days_Quiz into a quiz. tested without having a shuffle to see if it can ask and check questions


question_number = 0
# List of days in Maori
maori_days = [["rahina", "monday"], ["ratu", "tuesday"], ["raapa", "wednesday"], ["rapare", "thursday"],
              ["ramere", "friday"], ["rahoroi", "saturday"], ["ratapu", "sunday"]]

# While loop that repeats for all days
while question_number < 7:

    # Asking the user the question.
    user_answer = input(f"What is {maori_days[question_number][0]} in English: ").lower()

    # Checking Users answer.
    if user_answer == maori_days[question_number][1]:
        print("You are correct")
    else:
        print("You are incorrect")
    question_number += 1
