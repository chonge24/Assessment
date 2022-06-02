# making 08_Maori_Days_Quiz into a quiz. tested without having a shuffle to see if it can ask and check questions


question_number = 0
# List of months in Maori
maori_months = [["kohitatea", "january"], ["hui-tanguru", "february"], ["poutute-rangi", "march"],
                ["paenga-whawha", "april"], ["haratua", "may"], ["pipiri", "june"], ["hongongoi", "july"],
                ["here-turi-koka", "august"], ["mahuru", "september"], ["whiringa-a-nuku", "october"],
                ["whiringa-a-rangi", "november"], ["hakihea", "december"]]


# While loop that repeats for all months
while question_number < 12:

    # Asking the user the question.
    user_answer = input(f"What is '{maori_months[question_number][0]}' in English: ").lower()

    # Checking Users answer.
    if user_answer == maori_months[question_number][1]:
        print("You are correct")
    else:
        print("You are incorrect")
    question_number += 1
