import re

string ="Hey! What's up bro3?"
new_string = re.sub(r"[^a-zA-Z0-9]", "",string)
print(new_string)