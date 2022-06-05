# Made a new function to give them an option of seeing or not seeing the answer sheet.
# Made yes_no() based on 03_Yes_Or_No_Checker_v3 but with different variable.
def yes_no():
    yesno = input(f"Would you like to see the answer sheet?\n"
                  "Enter 'Y' to see, 'N' to not see, or 'X' to Exit:").upper()

    # Used a while loop for when the answer is not 'Y'.
    while yesno != 'Y':

        # If they enter 'X', quit program.
        if yesno == 'X':
            quit("Goodbye")

        elif yesno == 'N':
            continue
        else:
            yesno = input("Invalid input. Enter 'Y' to continue or 'N' to exit:").upper()
    answer_sheet()


def answer_sheet():
    answers = 0
    while answers == 0:
        # Ask the user if they want to continue to the quiz.
        print("This is the answer sheet.\n"
              "This is the question and answer [question, answer]\n"
              "e.g, [Monday, Rahina]\n"
              "Enter '1' for Numbers to numbers in Māori\n"
              "Enter '2' for Numbers in Māori to numbers\n"
              "Enter '3' for Days to days in Māori\n"
              "Enter '4' for Days in Māori to days\n"
              "Enter '5' for Months to months in Māori\n"
              "Enter '6' for Months in Māori to months\n"
              "Enter 'x' to quit")
        answers = input("Choose one of the options above and press enter: ")

        if answers == '1':
            print([['1', "tahi"], ['2', "rua"], ['3', "toru"], ['4', "wha"], ['5', "rima"], ['6', "ono"],
                   ['7', "whitu"], ['8', "waru"], ['9', "iwa"], ['10', "tekau"]])
            break

        elif answers == '2':
            print([["tahi", '1'], ["rua", '2'], ["toru", '3'], ["wha", '4'], ["rima", '5'], ["ono", '6'],
                   ["whitu", '7'], ["waru", '8'], ["iwa", '9'], ["tekau", '10']])
            break

        elif answers == '3':
            print([["monday", "rahina"], ["tuesday", "ratu"], ["wednesday", "raapa"], ["thursday", "rapare"],
                   ["friday", "ramere"], ["saturday", "rahoroi"], ["sunday", "ratapu"]])
            break

        elif answers == '4':
            print([["rahina", "monday"], ["ratu", "tuesday"], ["raapa", "wednesday"], ["rapare", "thursday"],
                   ["ramere", "friday"], ["rahoroi", "saturday"], ["ratapu", "sunday"]])
            break

        elif answers == '5':
            print([["january", "kohitatea"], ["february", "hui-tanguru"], ["march", "poutute-rangi"],
                   ["april", "paenga-whawha"], ["may", "haratua"], ["june", "pipiri"], ["july", "hongongoi"],
                   ["august", "here-turi-koka"], ["september", "mahuru"], ["october", "whiringa-a-nuku"],
                   ["november", "whiringa-a-rangi"], ["december", "hakihea"]])
            break

        elif answers == '6':
            print([["kohitatea", "january"], ["hui-tanguru", "february"], ["poutute-rangi", "march"],
                   ["paenga-whawha", "april"], ["haratua", "may"], ["pipiri", "june"], ["hongongoi", "july"],
                   ["here-turi-koka", "august"], ["mahuru", "september"], ["whiringa-a-nuku", "october"],
                   ["whiringa-a-rangi", "november"], ["hakihea", "december"]])
            break

        elif answers == 'x':
            quit("goodbye")
        # If the user enters an invalid answer, output 'Please enter a valid answer'
        else:
            print("Invalid input.\n"
                  "Please enter an option from below.")
            answers = 0
