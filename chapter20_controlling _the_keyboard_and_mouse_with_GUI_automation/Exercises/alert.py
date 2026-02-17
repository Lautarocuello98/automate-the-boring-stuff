import pyautogui

name = pyautogui.prompt('What is your name?')
pyautogui.alert(f'Hello {name}')