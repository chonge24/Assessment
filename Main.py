import sys
print("Welcome to Emmanuel's Māori Quiz")
print("The purpose of this program is to help people learn Māori.")
print("I hope you learn many things here!")
print("There will be a quiz of numbers 1-10 in Māori")
print("You can choose for the question to be in number or Māori.")
print("You can choose how many questions there are or if you would like us to mix the Māori numbers up.")
print("After you complete your quiz, I will tell you how many questions you answered correctly and how you can practice.")
print("You can choose to do the quiz again or exit.")
name = input("Enter your name:")
age = int(input("Enter your age:"))
if age > 11:
    sys.exit(f"Sorry, {name}, you are too old for this program")
elif age < 5:
    sys.exit(f"Sorry, {name}, you are too young for this program.")
else:
    continuation = input(f"Hi there, {name}, ready to learn some Māori? Enter 'Y' to continue or 'N' to Exit:").upper()
while continuation == 'N':
    quit("Goodbye")
if continuation == 'Y':
    print("Let's start the quiz!")
print("You can choose the following quizzes:")
print("Enter '1' for Numbers to numbers in Māori or")
print("Enter '2' for Numbers in Māori to numbers or")
print("Enter '3' for Days to days in Māori or")
print("Enter '4' for Days in Māori to days or")
print("Enter '5' for Months to months in Māori or")
print("Enter '6' for Months in Māori to months")
quiz_choice = int(input("Which test would you like:"))
if quiz_choice == 1:
    print("You have chosen Numbers to numbers in Māori.")
elif quiz_choice == 2:
    print("You have chosen numbers in Māori to numbers")
elif quiz_choice == 3:
    print("You have chosen days in English to days in Māori")
elif quiz_choice == 4:
    print("You have chosen days in Māori to days in English")
elif quiz_choice == 5:
    print("You have chosen months in English to months in Māori")
elif quiz_choice == 6:
    print("You have chosen months in Māori to months in English")
else:
    int(input("You have not entered any of the numbers representing a quiz. Please enter a number between 1 and 6:"))

