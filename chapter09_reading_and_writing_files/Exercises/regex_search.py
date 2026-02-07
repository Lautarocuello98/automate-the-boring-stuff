import re
import os

# ask the regular expression
regex = re.compile(input("Enter a regular expression: "))

# look all files in this folder
for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        with open(filename) as f:
            for line in f:
                # search the regex in each lines
                if regex.search(line):
                    print(f'{filename}: {line} \n', end='')