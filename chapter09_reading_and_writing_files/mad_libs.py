keywords = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

with open('input.txt', 'r') as t:
    text = t.read()

for word in keywords:
    while word in text:
        replacement = input(f'Enter a {word.lower()}: ')
        text = text.replace(word, replacement, 1)
print(text)

with open('output.txt', 'w') as r:
    r.write(text)

