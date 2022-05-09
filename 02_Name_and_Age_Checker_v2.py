# Asking for the name and age of child to make sure they are in primary school age. #
# Changes from the first version to specify whether they are too old or too young. #
name = input("Enter your name:")
age = int(input("Enter your age:"))
if age > 11:
    print(f"Sorry, {name}, you are too old for this program")
elif age < 5:
    print(f"Sorry, {name}, you are too young for this program.")
else:
    print(f"Hi there, {name}, ready to learn some Māori?")
