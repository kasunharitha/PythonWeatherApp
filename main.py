import requests

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
API_KEY = 'bla bla bla'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

# Get the user's location input (e.g., city name)
city_name = input("Enter city name: ")

# Construct the API URL
url = BASE_URL + f'q={city_name}&appid={API_KEY}'

# Send an HTTP GET request to the API
response = requests.get(url)

# Parse the JSON data returned by the API
data = response.json()

# Check if the API request was successful
if data["cod"] == 200:
    # Extract and display relevant weather information
    weather_info = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    print(f"Weather: {weather_info}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
else:
    # Handle API request failure
    print("Unable to fetch weather data.")

