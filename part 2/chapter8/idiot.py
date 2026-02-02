import pyinputplus as pyip

while True:
    prompt = 'want to know how to keep an idiot bussy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break
print('Thank you have a nice day!')