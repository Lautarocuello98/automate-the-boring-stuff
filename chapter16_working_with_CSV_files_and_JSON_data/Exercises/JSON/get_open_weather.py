#! python3
# get_open_weather.py - Prints the weather for a location from the command line.

API_KEY = 'api_here'

import json
import requests
import sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print ('Usage: get_open_weather.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API


url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"

response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weather_data = json.loads(response.text)

# Print weather descriptions
print(f"Weather forecast for {location}\n")
print("Today:")
print(weather_data['list'][0]['weather'][0]['description'],
      "-", weather_data['list'][0]['main']['temp'], "°C")

print("\nTomorrow:")
print(weather_data['list'][8]['weather'][0]['description'],
      "-", weather_data['list'][8]['main']['temp'], "°C")

print("\nDay after tomorrow:")
print(weather_data['list'][16]['weather'][0]['description'],
      "-", weather_data['list'][16]['main']['temp'], "°C")