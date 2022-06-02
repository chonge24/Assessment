# Printing the list to see if it will shuffle
import random
# List of months in Maori
maori_months = [["kohitatea", "january"], ["hui-tanguru", "february"], ["poutute-rangi", "march"],
                ["paenga-whawha", "april"], ["haratua", "may"], ["pipiri", "june"], ["hongongoi", "july"],
                ["here-turi-koka", "august"], ["mahuru", "september"], ["whiringa-a-nuku", "october"],
                ["whiringa-a-rangi", "november"], ["hakihea", "december"]]


# Mixing the list in a random order
random.shuffle(maori_months)

# testing if it shuffled properly
print(maori_months)
