# Printing the list to see if it will shuffle
import random
# List of numbers in Maori
maori_numbers = [["tahi", '1'], ["rua", '2'], ["toru", '3'], ["wha", '4'], ["rima", '5'], ["ono", '6'],
                 ["whitu", '7'], ["waru", '8'], ["iwa", '9'], ["tekau", '10']]

# Mixing the list in a random order
random.shuffle(maori_numbers)

# testing if it shuffled properly
print(maori_numbers)
