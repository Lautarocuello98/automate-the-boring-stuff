import datetime
import time

print("Current time:")
now = datetime.datetime.now()
print(now)

print("\n100 days from now:")
future = now + datetime.timedelta(days=100)
print(future)

print("\nDifference example:")
old_date = datetime.datetime(2020, 1, 1)
difference = now - old_date
print("Days passed:", difference.days)

print("\nWaiting 5 seconds...")
time.sleep(5)
print("Done.")