# Chapter 20 – Controlling the Keyboard and Mouse with GUI Automation 🖱️⌨️🤖  

## Topics Covered
- Controlling the mouse using the PyAutoGUI module  
- Moving the mouse with `moveTo()` and `move()`  
- Clicking, double-clicking, and right-clicking programmatically  
- Dragging the mouse to select or move items  
- Getting screen size and mouse position  
- Adding delays and pauses to automation scripts  
- Typing text with `write()`  
- Pressing special keys with `press()`, `keyDown()`, and `keyUp()`  
- Sending keyboard shortcuts using `hotkey()`  
- Using screenshots and image recognition to locate UI elements  
- Automating repetitive GUI tasks safely  

## Goal
Automate interactions with graphical user interfaces by simulating mouse movements, clicks, and keyboard input.  
This allows scripts to control applications that do not provide APIs, enabling automation of forms, file operations, testing, and repetitive desktop workflows.

## Notes
GUI automation works by sending input events to the operating system, so timing and screen coordinates are critical.  
Delays, fail-safes, and testing in small steps are important to prevent scripts from misclicking or typing in the wrong place.  
Image recognition can make automation more robust by locating buttons or icons on the screen instead of relying only on coordinates.  
PyAutoGUI is especially useful for automating legacy software, repetitive data entry, or workflows that normally require manual clicking and typing.

## Projects

looking_busy.py (This script keeps the computer active by slightly moving the mouse every 10 seconds).

clipboard_to_read_a_text.py (This script opens Notepad, copies its text via the clipboard, and prints it in Python).

instant_messenger_bot.py (use PyAutoGUI to type messages automatically in an open window after a short delay.).
