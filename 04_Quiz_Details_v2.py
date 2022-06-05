'''Creating lists of the possible quiz answers as well as asking which quiz they would like to take
Changes made from version 1 to remove the accents on the quiz answers as it is difficult for some computers to type them
Removed numerous print statements to make it a singular print '''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maori_numbers = ["tahi", "rua", "toru", "whā", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
days = ["monday", "tuesday", "thursday", "wednesday", "friday", "saturday", "sunday"]
maori_days = ["rahina", "ratu", "raapa", "rapare", "ramere", "rahoroi", "ratapu"]
months = ["january", "february", "march", "april", "may", "june", "july",
          "august", "september", "october", "november", "december"]
maori_months = ["kohitatea", "hui-tanguru", "poutute-rangi", "paenga-whawha", "haratua", "pipiri", "hongongoi",
                "here-turi-koka", "mahuru", "whiringa-a-nuku", "whiringa-a-rangi", "hakihea"]
print("You can choose the following quizzes:\n"
      "Enter '1' for Numbers to numbers in Māori\n"
      "Enter '2' for Numbers in Māori to numbers\n"
      "Enter '3' for Days to days in Māori\n"
      "Enter '4' for Days in Māori to days\n"
      "Enter '5' for Months to months in Māori\n"
      "Enter '6' for Months in Māori to months")
choice = input("Which test would you like:")

# If they enter '1', tell them their choice
if choice == '1':
    print("You have chosen Numbers to numbers in Māori.")

    # If they enter '2', tell them their choice
elif choice == '2':
    print("You have chosen numbers in Māori to numbers")

# If they enter '3', tell them their choice
elif choice == '3':
    print("You have chosen days in English to days in Māori")

# If they enter '4', tell them their choice
elif choice == '4':
    print("You have chosen days in Māori to days in English")

# If they enter '5', tell them their choice
elif choice == '5':
    print("You have chosen months in English to months in Māori")

# If they enter '6', tell them their choice
elif choice == '6':
    print("You have chosen months in Māori to months in English")

# If they enter something not representing any choices, ask them to enter again.
else:
    choice = input("You have not entered any of the numbers representing a quiz. Please enter a number between 1 and 6:")
