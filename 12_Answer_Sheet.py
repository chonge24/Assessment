# Testing if it can print as expected


answer = input("This is the answer sheet.\n"
               "This is the question and answer [question, answer]\n"
               "e.g, [Monday, Rahina]\n"
               "Enter '1' for Numbers to numbers in Māori\n")
# Only using '1' for testing convenience
if answer == '1':
    print([[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"],
           [7, "whitu"], [8, "waru"], [9, "iwa"], [10, "tekau"]])
