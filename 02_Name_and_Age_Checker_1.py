# 02_Name_and_Age_Checker Trial 1
# Asking for the name and age of child to make sure they are in primary school age. #
name = input("Enter your name:")
age = int(input("Enter your age:"))
if age > 11 or age < 5:
    print(f"Sorry, {name}, you are not in range of Primary school age")
print(f"Hi there, {name}, ready to learn some Māori?")
