# making sure the input for 'quiz_chooser' does the expected output. Will put the other stuff from other components
# together with this component in final program.
# Made 04_Quiz_Details_v2 into function


def quiz_chooser():
    choose_quiz = 0
    while choose_quiz == 0:
        # Ask the user if they want to continue to the quiz.
        print("You can choose the following quizzes:\n"
              "Enter '1' for Numbers to numbers in Māori\n"
              "Enter '2' for Numbers in Māori to numbers\n"
              "Enter '3' for Days to days in Māori\n"
              "Enter '4' for Days in Māori to days\n"
              "Enter '5' for Months to months in Māori\n"
              "Enter '6' for Months in Māori to months\n"
              "Enter 'x' to quit")
        choose_quiz = input("Choose one of the options above and press enter: ").lower()

        # If they enter '1', tell them their choice
        if choose_quiz == '1':
            print(numbers)
            print(f"Your total score was nothing. this is a trial")

        # If they enter '2', tell them their choice
        elif choose_quiz == '2':
            print(maori_numbers)
            print(f"Your total score was nothing. this is a trial")

        # If they enter '3', tell them their choice
        elif choose_quiz == '3':
            print(days)
            print(f"Your total score was nothing. this is a trial")

        # If they enter '4', tell them their choice
        elif choose_quiz == '4':
            print(maori_days)
            print(f"Your total score was nothing. this is a trial")

        # If they enter '5', tell them their choice
        elif choose_quiz == '5':
            print(months)
            print(f"Your total score was nothing. this is a trial")

        # If they enter '6', tell them their choice
        elif choose_quiz == '6':
            print(maori_months)
            print(f"Your total score was nothing. this is a trial")

        # If they enter 'x', quit program
        elif choose_quiz == 'x':
            quit("goodbye")
        # If the user enters an invalid answer, output 'Please enter a valid answer'
        else:
            print("Invalid input.\n"
                  "Please enter an option from below.")
            choose_quiz = 0


numbers = [['1', "tahi"], ['2', "rua"], ['3', "toru"], ['4', "wha"], ['5', "rima"], ['6', "ono"],
           ['7', "whitu"], ['8', "waru"], ['9', "iwa"], ['10', "tekau"]]
maori_numbers = [["tahi", '1'], ["rua", '2'], ["toru", '3'], ["wha", '4'], ["rima", '5'], ["ono", '6'],
                 ["whitu", '7'], ["waru", '8'], ["iwa", '9'], ["tekau", '10']]
days = [["monday", "rahina"], ["tuesday", "ratu"], ["wednesday", "raapa"], ["thursday", "rapare"],
        ["friday", "ramere"], ["saturday", "rahoroi"], ["sunday", "ratapu"]]
maori_days = [["rahina", "monday"], ["ratu", "tuesday"], ["raapa", "wednesday"], ["rapare", "thursday"],
              ["ramere", "friday"], ["rahoroi", "saturday"], ["ratapu", "sunday"]]
months = [["january", "kohitatea"], ["february", "hui-tanguru"], ["march", "poutute-rangi"], ["april", "paenga-whawha"],
          ["may", "haratua"], ["june", "pipiri"], ["july", "hongongoi"], ["august", "here-turi-koka"],
          ["september", "mahuru"], ["october", "whiringa-a-nuku"], ["november", "whiringa-a-rangi"], ["december", "hakihea"]]
maori_months = [["kohitatea", "january"], ["hui-tanguru", "february"], ["poutute-rangi", "march"],
                ["paenga-whawha", "april"], ["haratua", "may"], ["pipiri", "june"], ["hongongoi", "july"],
                ["here-turi-koka", "august"], ["mahuru", "september"], ["whiringa-a-nuku", "october"],
                ["whiringa-a-rangi", "november"], ["hakihea", "december"]]

# main routine
play = 'y'
if play == 'y':
    quiz_chooser()
