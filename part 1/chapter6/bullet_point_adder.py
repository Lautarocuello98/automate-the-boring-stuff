#! python3
# bullet_point_adder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # Loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]  # Add star to each line

text = '\n'.join(lines)
pyperclip.copy(text)
