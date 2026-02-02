#English to Pig Latin translator
print('Enter the English message to translate into Pig Latin: ')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # a list of the words in pig latin
for word in message.split():
    #separate the no letters
    prefixnoletter = ''

    while len(word) > 0 and not word[0].isalpha():
        prefixnoletter += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixnoletter)
        continue

    #separate the non-letter at the end of this word:
    suffixnonletters = ''
    while not word[-1].isalpha():
        suffixnonletters += word[-1] + suffixnonletters
        word = word[:-1]

    #remember if the word was in uppercase or title case:
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # make the word lowercase for translation.

    #separate the consonants at the starts of this word:
    prefixconsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixconsonants += word[0]
        word = word[1:]


    #add the pig latin ending to the word:
    if prefixconsonants != '':
        word += prefixconsonants + 'ay'
    else:
        word += 'yay'


    #set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    #add the non-letters back to the start or end of the word.
    pigLatin.append(prefixnoletter + word + suffixnonletters)
    
    #join all the words back together into a single string:
print(' '.join(pigLatin))