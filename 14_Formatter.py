symbol = "*"
text = "Welcome to the maori language quiz game"
sides = symbol * 3

formatted_text = f"{sides} {text} {sides}"
top_bottom = symbol * len(formatted_text)

print(top_bottom)
print(formatted_text)
print(top_bottom)
