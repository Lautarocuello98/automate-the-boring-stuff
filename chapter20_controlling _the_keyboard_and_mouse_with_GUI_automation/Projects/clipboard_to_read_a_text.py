#! python3
# clipboard_to_read_a_text.py 
# This script automatically opens Notepad, activates the window, selects and copies all the text using the clipboard,
# reads it in Python, and prints it to the console.


import pyautogui
import pyperclip
import time
import os


os.system("notepad")

# Give time to open Notepad and type something

# Get Notepad window
win = None
while win is None:
    windows = pyautogui.getWindowsWithTitle('Notepad')
    if windows:
        win = windows[0]
    else:
        time.sleep(0.5)
win.activate()
win.maximize()

time.sleep(1)

# Click inside text area
pyautogui.click(300, 300)

# Select all and copy
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

# Read clipboard
text = pyperclip.paste()
win.close()

print(text)
