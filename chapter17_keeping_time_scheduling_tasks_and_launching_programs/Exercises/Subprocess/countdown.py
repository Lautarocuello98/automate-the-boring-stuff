#! python3
# countdown.py - A simple countdown script.

import time
import subprocess

time_left = 5

while time_left > 0:
    print(time_left, end='\n')
    time.sleep(1)
    time_left -= 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)