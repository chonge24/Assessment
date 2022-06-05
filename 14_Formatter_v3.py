
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
# for all of these, Show the symbol that wants to format, Then the sentence that they want
print(formatter("*", "test 1"))
print()
print(formatter("!", "test 2"))
print()
print(formatter("-", "test 3"))
