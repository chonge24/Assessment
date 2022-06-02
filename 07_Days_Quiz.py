# Printing the list to see if it will shuffle
import random
# List of days
days = [["monday", "rahina"], ["tuesday", "ratu"], ["wednesday", "raapa"], ["thursday", "rapare"],
        ["friday", "ramere"], ["saturday", "rahoroi"], ["sunday", "ratapu"]]

# Mixing the list in a random order
random.shuffle(days)

# testing if it shuffled properly
print(days)
