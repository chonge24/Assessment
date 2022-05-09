# Asking for the name and age of child to make sure they are in primary school age. #
# Changes from the first version to specify whether they are too old or too young. #
# Changes from the second version because when I put it into the main, even if they were too old/young, it would still carry onto the next part instead of quitting
import sys
name = input("Enter your name:")
age = int(input("Enter your age:"))
if age > 11:
    sys.exit(f"Sorry, {name}, you are too old for this program")
elif age < 5:
    sys.exit(f"Sorry, {name}, you are too young for this program.")
elif 5 < age < 11:
    print(f"Hi there, {name}, ready to learn some Māori?")
else:
    age = int(input("Invalid input. Please enter your age:"))
