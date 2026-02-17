# instant_messenger_bot.py
# This script uses PyAutoGUI to automatically type messages in an open window. It waits a few seconds so you can focus the target window,
# clicks inside it, and then types several messages, pressing Enter after each one.

from __future__ import annotations

import time
import datetime as dt
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05

WINDOW_TITLE = "Notepad" 
RECIPIENTS = ["Alice", "Bob", "Charlie"]
MESSAGE = "Demo ping from my bot."

def log(msg: str) -> None:
    print(f"[{dt.datetime.now().strftime('%H:%M:%S')}] {msg}")

def main() -> None:
    log("Starting in 5 seconds. Open Notepad and leave it visible.")
    pyautogui.countdown(5)

    # Find the window (first match)
    wins = pyautogui.getWindowsWithTitle(WINDOW_TITLE)
    if not wins:
        raise SystemExit(f"Couldn't find a window with '{WINDOW_TITLE}' in the title.")

    win = wins[0]
    win.activate()
    time.sleep(0.2)

    # Maximize (optional but convenient)
    try:
        win.maximize()
        time.sleep(0.2)
    except Exception:
        pass

    # Click roughly in the middle so the caret is placed inside the text area
    x = win.left + win.width // 2
    y = win.top + win.height // 2
    pyautogui.click(x, y)

    log("Typing messages...")
    try:
        for name in RECIPIENTS:
            pyautogui.write(f"To {name}: {MESSAGE}")
            pyautogui.press("enter")
            time.sleep(0.5)
        log("Done.")
    except KeyboardInterrupt:
        log("Stopped by Ctrl+C.")

if __name__ == "__main__":
    main()