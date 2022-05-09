# Creating lists of the possible quiz answers as well as asking which quiz they would like to take #
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maori_numbers = ["tahi", "rua", "toru", "whā", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
days = ["monday", "tuesday", "thursday", "wednesday", "friday", "saturday", "sunday"]
maori_days = ["rāhina", "rātu", "rāapa", "rāpare", "rāmere", "rāhoroi", "rātapu"]
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
maori_months = ["kohitātea", "hui-tanguru", "poutū-te-rangi", "paenga-whāwhā", "haratua", "pipiri", "hōngongoi", "here-turi-kōkā", "mahuru", "whiringa-ā-nuku", "whiringa-ā-rangi", "hakihea"]
print("You can choose the following quizzes:")
print("Enter '1' for Numbers to numbers in Māori or")
print("Enter '2' for Numbers in Māori to numbers or")
print("Enter '3' for Days to days in Māori or")
print("Enter '4' for Days in Māori to days or")
print("Enter '5' for Months to months in Māori or")
print("Enter '6' for Months in Māori to months")
choice = int(input("Enter the number you want to choose:"))
while choice == 1:
    print("You have chosen Numbers to numbers in Māori")
if choice == 2:
    print("You have chosen Numbers in Māori to numbers")
elif choice == 3:
    print("You have chosen Days to days in Māori")
elif choice == 4:
    print("You have chosen: Days in Māori to days")
elif choice == 5:
    print("You have chosen: Months to months in Māori")
elif choice == 6:
    print("You have chosen: Months in Māori to months")
else:
    print("You have not chosen a number representing a learning option.")
    choice = int(input("Enter the number you want to choose:"))
