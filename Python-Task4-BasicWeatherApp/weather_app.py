import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    print("Error: API key not found.")
    print("Please check your .env file.")
    exit()


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()

            city_name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]

            print("\n===== WEATHER INFORMATION =====")
            print(f"City: {city_name}, {country}")
            print(f"Temperature: {temperature}°C")
            print(f"Feels Like: {feels_like}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {weather}")
            print("===============================")

        elif response.status_code == 404:
            print("\nError: City not found.")

        elif response.status_code == 401:
            print("\nError: Invalid API key.")

        else:
            print("\nError: Unable to get weather information.")
            print("Status code:", response.status_code)

    except requests.exceptions.RequestException:
        print("\nError: Could not connect to the weather service.")


print("===== BASIC WEATHER APP =====")
print("Enter a city name to get its current weather.")
print("Type 'exit' to close the application.")

while True:

    city = input("\nEnter city name: ").strip()

    if city.lower() == "exit":
        print("Weather app closed. Goodbye!")
        break

    if not city:
        print("Please enter a city name.")
        continue

    get_weather(city)