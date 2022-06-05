# 02_Name_and_Age_Checker Trial 1
# Asking for the name and age of child to make sure they are in primary school age. #
# Changes from the first version to specify whether they are too old or too young. #
name = input("Enter your name:")
age = int(input("Enter your age:"))

# If they are too old, exit program.
if age > 11:
    print(f"Sorry, {name}, you are too old for this program")

# If they are too young, exit program.
elif age < 5:
    print(f"Sorry, {name}, you are too young for this program.")

# If they are of Primary school age, they can continue.
else:
    print(f"Hi there, {name}, ready to learn some Māori?")
