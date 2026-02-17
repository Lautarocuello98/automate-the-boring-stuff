import pyautogui

# Locate the picture in the screen
try:
    b = pyautogui.locateOnScreen('submit.png')
    print(b)
except:
    print('Image could not be found.')

print(list(pyautogui.locateAllOnScreen('submit.png')))

# Click in that cordinates and in that picture
pyautogui.click((14, 8, 21, 23))
pyautogui.click(('submit.png'))