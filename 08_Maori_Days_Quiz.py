# Printing the list to see if it will shuffle
import random
# List of days in Maori
maori_days = [["rahina", "monday"], ["ratu", "tuesday"], ["raapa", "wednesday"], ["rapare", "thursday"],
              ["ramere", "friday"], ["rahoroi", "saturday"], ["ratapu", "sunday"]]

# Mixing the list in a random order
random.shuffle(maori_days)

# testing if it shuffled properly
print(maori_days)
