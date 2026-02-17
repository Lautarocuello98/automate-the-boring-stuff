# looking_busy.py
# This script keeps the computer active by slightly moving the mouse every 10 seconds.

import pyautogui
import time

while True:
    pyautogui.moveRel(1, 0)
    pyautogui.moveRel(-1, 0)
    time.sleep(10)
