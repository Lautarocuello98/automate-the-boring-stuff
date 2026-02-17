import pyautogui

fw = pyautogui.getActiveWindow()
print(fw)
print(f'title: {fw.title}')
print(f'size: {fw.size}')
print(fw.left, fw.top, fw.right, fw.bottom)
print(f'topleft: {fw.topleft}')
print(f'area: {fw.area}')
