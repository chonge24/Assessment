# Testing if it can print as expected


answer = input("This is the answer sheet.\n"
               "This is the question and answer [question, answer]\n"
               "e.g, [Monday, Rahina]\n"
               "Enter '1' for Numbers to numbers in Māori\n"
               "Enter '2' for Numbers in Māori to numbers\n"
               "Enter '3' for Days to days in Māori\n"
               "Enter '4' for Days in Māori to days\n"
               "Enter '5' for Months to months in Māori\n"
               "Enter '6' for Months in Māori to months\n"
               "Enter 'x' to quit:")
if answer == '1':
    print([[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"],
           [7, "whitu"], [8, "waru"], [9, "iwa"], [10, "tekau"]])
