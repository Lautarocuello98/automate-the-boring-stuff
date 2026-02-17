import pyautogui

im = pyautogui.screenshot()
print(im.size)



im.save('screenshot.png')
