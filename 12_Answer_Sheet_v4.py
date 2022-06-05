# Added 'n' input to the function so there is a way to exit the function without quitting program.
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
              "Enter 'x' to quit\n"
              "Enter 'n' when you finish looking")
        answers = input("Choose one of the options above and press enter: ").lower()

        # If they enter '1', print the answer sheet for Numbers to numbers in Māori
        if answers == '1':
            print([['1', "tahi"], ['2', "rua"], ['3', "toru"], ['4', "wha"], ['5', "rima"], ['6', "ono"],
                   ['7', "whitu"], ['8', "waru"], ['9', "iwa"], ['10', "tekau"]])
            break

        # If they enter '2', print the answer sheet for Numbers in Māori to numbers
        elif answers == '2':
            print([["tahi", '1'], ["rua", '2'], ["toru", '3'], ["wha", '4'], ["rima", '5'], ["ono", '6'],
                   ["whitu", '7'], ["waru", '8'], ["iwa", '9'], ["tekau", '10']])
            break

        # If they enter '3', print the answer sheet for Days to days in Māori
        elif answers == '3':
            print([["monday", "rahina"], ["tuesday", "ratu"], ["wednesday", "raapa"], ["thursday", "rapare"],
                   ["friday", "ramere"], ["saturday", "rahoroi"], ["sunday", "ratapu"]])
            break

        # If they enter '4', print the answer sheet for Days in Māori to days
        elif answers == '4':
            print([["rahina", "monday"], ["ratu", "tuesday"], ["raapa", "wednesday"], ["rapare", "thursday"],
                   ["ramere", "friday"], ["rahoroi", "saturday"], ["ratapu", "sunday"]])
            break

        # If they enter '5', print the answer sheet for Months to months in Māori
        elif answers == '5':
            print([["january", "kohitatea"], ["february", "hui-tanguru"], ["march", "poutute-rangi"],
                   ["april", "paenga-whawha"], ["may", "haratua"], ["june", "pipiri"], ["july", "hongongoi"],
                   ["august", "here-turi-koka"], ["september", "mahuru"], ["october", "whiringa-a-nuku"],
                   ["november", "whiringa-a-rangi"], ["december", "hakihea"]])
            break

        # If they enter '6', print the answer sheet for Months in Māori to months
        elif answers == '6':
            print([["kohitatea", "january"], ["hui-tanguru", "february"], ["poutute-rangi", "march"],
                   ["paenga-whawha", "april"], ["haratua", "may"], ["pipiri", "june"], ["hongongoi", "july"],
                   ["here-turi-koka", "august"], ["mahuru", "september"], ["whiringa-a-nuku", "october"],
                   ["whiringa-a-rangi", "november"], ["hakihea", "december"]])
            break
        # If they enter 'x', exit program, saying "goodbye"
        elif answers == 'x':
            quit("goodbye")

        # When they finish looking at the answers, they press 'n', leading onto the next part of program
        elif answers == 'n':
            print()

        # If the user enters an invalid answer, output 'Please enter a valid answer'
        else:
            print("Invalid input.\n"
                  "Please enter an option from below.")
            answers = 0
