# making 08_Maori_Days_Quiz into a quiz. tested without having a shuffle to see if it can ask and check questions


question_number = 0
# List of months
months = [["january", "kohitatea"], ["february", "hui-tanguru"], ["march", "poutute-rangi"], ["april", "paenga-whawha"],
          ["may", "haratua"], ["june", "pipiri"], ["july", "hongongoi"], ["august", "here-turi-koka"],
          ["september", "mahuru"], ["october", "whiringa-a-nuku"], ["november", "whiringa-a-rangi"], ["december", "hakihea"]]

# While loop that repeats for all months
while question_number < 12:

    # Asking the user the question.
    user_answer = input(f"What is '{months[question_number][0]}' in Maori: ").lower()

    # Checking Users answer.
    if user_answer == months[question_number][1]:
        print("You are correct")
    else:
        print("You are incorrect")
    question_number += 1
