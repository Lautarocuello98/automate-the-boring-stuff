import pyautogui

fw = pyautogui.getActiveWindow()
print(fw.isMaximized)
print(fw.isMinimized)

print(fw.isActive)
fw.minimize()
print(fw.isMinimized)

import time
time.sleep(2)
fw.maximize()
fw.close()