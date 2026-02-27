# Lautarocuello98
# umbrella_check.py

import requests
from datetime import datetime

RAIN_THRESHOLD = 40
LAT = -34.60
LON = -58.38


def check_rain():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}&longitude={LON}"
        "&daily=precipitation_probability_max"
        "&timezone=auto"
    )

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
    except requests.RequestException as e:
        print("Error fetching weather data:", e)
        return

    data = res.json()
    try:
        rain = data["daily"]["precipitation_probability_max"][0]
    except (KeyError, IndexError):
        print("Unexpected API response format.")
        return
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"[{timestamp}] Chance of rain today: {rain}%")

    if rain >= RAIN_THRESHOLD:
        print("Take an umbrella.")
    else:
        print("No umbrella needed.")


if __name__ == "__main__":
    check_rain()


