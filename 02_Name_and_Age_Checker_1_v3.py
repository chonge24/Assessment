# 02_Name_and_Age_Checker Trial 1
# Asking for the name and age of child to make sure they are in primary school age. #
# Changes from the first version to specify whether they are too old or too young. #
# Changes from the second version because when I put it into the main, even if they were too old/young,
# it would still carry onto the next part instead of quitting
# Because of the inclusion of elif 5 < age < 11, the others had to be moved, so the inputs '5' and '11' would work.
import sys
name = input("Enter your name:")
age = int(input("Enter your age:"))

# If they are too old, exit program.
if age >= 12:
    sys.exit(f"Sorry, {name}, you are too old for this program")

# If they are too young, exit program.
elif age <= 4:
    sys.exit(f"Sorry, {name}, you are too young for this program.")

# If they are in Primary school age, continue program.
elif 5 < age < 11:
    print(f"Hi there, {name}, ready to learn some Māori?")

# If answer is invalid, ask them to enter again.
else:
    age = input("Invalid input. Please enter your age:")
