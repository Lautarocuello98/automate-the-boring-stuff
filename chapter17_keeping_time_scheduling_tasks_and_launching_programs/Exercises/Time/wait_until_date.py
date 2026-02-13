import datetime
import time

target = datetime.datetime(2026, 10, 31, 0, 0, 0)

while datetime.datetime.now() < target:
    time.sleep(1)

print("Llegó la fecha")