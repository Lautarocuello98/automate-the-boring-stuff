# Lautarocuello98
# stopwatch.py - A simple stopwatch program with aligned output

import time
import pyperclip


# Display the program's instructions
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')

input()                     # press Enter to begin

print('Started')

start_time = time.time()    # get the first lap's start time
last_time = start_time
lap_num = 1


try:
    while True:
        input()     # Wait for user to record a lap
        now = time.time()  # Capture current time once for accurate calculations
        
        # Calculate lap time and total elapsed time
        lap_time = round(now - last_time, 2)
        total_time = round(now - start_time, 2)
        last_time = now

        # Format values to keep output aligned
        total_str = f'{total_time:.2f}'.rjust(5)
        lap_str = f'{lap_time:.2f}'.rjust(5)
        lap_num_str = f'{lap_num}'.ljust(3)

        result = f"Lap #{lap_num_str} - {total_str} ({lap_str})"
        print(result)

        # Copy last lap result to clipboard
        pyperclip.copy(result)

        lap_num += 1


except KeyboardInterrupt:
    print('\nDone')