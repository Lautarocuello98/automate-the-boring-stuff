#! python3
# umbrella_reminder.py
# Waits until 08:00 and then checks if rain is expected today

import requests
import datetime
import time

# Coordinates for Liberia, Guanacaste
url = "https://api.open-meteo.com/v1/forecast?latitude=10.63&longitude=-85.44&daily=precipitation_probability_max&timezone=auto"

hour = int(input("At what hour do you want program the program?\n"))
minutes = int(input("And the minutes..?\n"))
print("Programed")
while True:
    now = datetime.datetime.now()

    if now.hour == hour and now.minute == minutes:
        print("Starting checking...")

        try:
            res = requests.get(url, timeout=10)
            res.raise_for_status()
        except requests.RequestException as e:
            print("Error getting weather:", e)
            exit()

        data = res.json()
        rain_probability = data["daily"]["precipitation_probability_max"][0]

        print(f"Chance of rain today: {rain_probability}%")

        if rain_probability >= 40:
            print("Take an umbrella today.")
        else:
            print("It doesn't seem it's going to rain.")

        # Wait 61 seconds so it doesn't repeat multiple times
        time.sleep(61)

    # Check the time every 30 seconds
    time.sleep(30)
