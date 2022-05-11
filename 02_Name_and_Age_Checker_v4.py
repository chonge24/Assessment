# Asking for the name and age of child to make sure they are in primary school age. #
# Changes from the first version to specify whether they are too old or too young. #
# Changes from the second version because when I put it into the main, even if they were too old/young, it would still carry onto the next part instead of quitting #
# Changes from the third version to make sure that if the age input was letters (abc) or symbols (!@#) it would come up with 'invalid input. please enter age:'. I also removed the specification of 'too young' or 'too old' so that people cannot change their age older/younger #
import sys
name = input("Enter your name:")
age = input("Enter your age:")
while type(age) != int:
    age = int(input("Invalid input. Please enter your age:"))
if 5 <= age <= 11:
    continuation = input(f"Hi there, {name}, ready to learn some Māori? Enter 'Y' to continue or 'N' to Exit:").upper()
else:
    sys.exit(f"Sorry, {name} you are not of primary school age.")
