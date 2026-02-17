import pyautogui
for i in range(5):      # move mouse in a square
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

for i in range(5):
    pyautogui.move(100, 0, duration=0.25)   # right
    pyautogui.move(0, 100, duration=0.25)   # down   
    pyautogui.move(-100, 0, duration=0.25)  # left
    pyautogui.move(0, -100, duration=0.25)  # up