# Lautarocuello98
# stopwatch.py — A simple CLI stopwatch with lap tracking, aligned output,
# clipboard copy, and automatic lap logging to a text file.

import time
from pathlib import Path
import pyperclip


print("Press ENTER to start the stopwatch.")
print("Press ENTER again to record a lap.")
print("Press Ctrl+C to quit.\n")

input()

print("Started...\n")

start_time = time.time()
last_time = start_time
lap_num = 1

log_file = Path("stopwatch_laps.txt")
log_file.write_text("Stopwatch session\n\n", encoding="utf-8")

try:
    while True:
        input()  # Wait for ENTER to record a lap

        now = time.time()
        lap_time = now - last_time
        total_time = now - start_time
        last_time = now

        result = f"Lap {lap_num:<3} - {total_time:>6.2f} ({lap_time:>6.2f})"
        print(result)

        # Copy latest lap to clipboard
        pyperclip.copy(result)

        # Append lap to log file
        with log_file.open("a", encoding="utf-8") as file:
            file.write(result + "\n")

        lap_num += 1

except KeyboardInterrupt:
    print(f"\nDone. Laps saved to: {log_file}")