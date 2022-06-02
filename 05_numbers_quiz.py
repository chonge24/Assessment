# Printing the list to see if it will shuffle
import random
# List of numbers
numbers = [['1', "tahi"], ['2', "rua"], ['3', "toru"], ['4', "wha"], ['5', "rima"], ['6', "ono"],
           ['7', "whitu"], ['8', "waru"], ['9', "iwa"], ['10', "tekau"]]

# Mixing the list in a random order
random.shuffle(numbers)

# testing if it shuffled properly
print(numbers)
