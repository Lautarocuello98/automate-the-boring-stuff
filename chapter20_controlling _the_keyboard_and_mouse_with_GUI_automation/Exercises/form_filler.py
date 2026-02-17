#! python3
# form_filler.py - Automatically fills in the form.

import pyautogui, time
# 631,608

form_data = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 
              'comments': 'Tell Bob I said hi.'},
             {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 
              'comments': 'n/a'},
             {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 
              'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
             {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 
              'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
             ]
time.sleep(5)


# Give the user a chance to kill the script.

print('Ensure that the browser window is active and the form is loaded!')

for person in form_data:
    pyautogui.click(642, 612)
    # Wait until the form page has loaded.
    print('>>> 3-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(3)
    pyautogui.click(642, 612)
    

    print(f"Entering {person['name']} info...")


    # Fill out the name field.
    pyautogui.write(person['name'] + '\t', 0.2)

    # Fill out the greatest fear(s) field.
    pyautogui.write(person['fear'] + '\t', 0.2)

    # Fill out the source of Wizard powers field.
    if person['source'] == 'wand':
        pyautogui.write(['down', 'enter', '\t'], 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', 'enter', '\t'], 0.5)


    # Fill out the RoboCop field.
    if person['robocop'] == 1:
        pyautogui.write([' ', '\t'], 0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t'], 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t'], 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t'], 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t'], 0.5)    


    pyautogui.write(['\t'], 0.5)

    # Fill out the Additional Comments field
    pyautogui.write(person['comments'] + '\t')

    # Click submit.
    time.sleep(0.5)
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Submitted form.')
    time.sleep(5)

    # Click the submit another response link.
    pyautogui.click(651,350)