#! python3
# phoneAndEmail.py - finds phone numbers and email addresses on the clipboard.

import pyperclip
import re

# Create phone number regex.
phoneRegex = re.compile(r'''
    (?:\+?\d{1,3}[\s.-]?)?      # código de país
    (?:\(?\d{2,4}\)?[\s.-]?)?   # prefijo / área
    (?:\d{2,4}[\s.-]?){2,3}     # bloques del número
    (?:\s*(?:ext|x|ext.)\s*\d{2,5})?  # extensión
''', re.VERBOSE)



# Create email regex.
emailRegex = re.compile(
    r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
)


# find all matches in clipboard text

text = str(pyperclip.paste())

matches = []

for phone in phoneRegex.findall(text):
    matches.append(phone)

for email in emailRegex.findall(text):
    matches.append(email)

#copy the results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')