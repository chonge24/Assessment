# function to formant
# This collects the symbol wanted and the text also
def formatter(symbol, text):
    # The symbol has 3 of it on either side
    sides = symbol * 3
    # it is the 3 on either side with text in the middle
    formatted_text = f"{sides} {text} {sides}"
    # The top and bottom are the symbol repeated
    top_bottom = symbol * len(formatted_text)
    # goes back with three rows
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
# Asks what needs to be formatted
text1 = input("What to you want to be formatted: ")
# Ask what symbol they want
symbol_ = input("What symbol do you want to have: ")
print()
# Shows the final project
print(formatter(symbol_, text1))
