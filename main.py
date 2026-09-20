import requests
def get_weather(city_name):
    
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&format=json"
    response = requests.get(url)
    data = response.json()

    if "results" not in data:
        print(f"Could not find coordinates for {city_name}.")
        return
    
    lat=data["results"][0]["latitude"]
    lon=data["results"][0]["longitude"]
    country=data['results'][0].get("country", '')

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    temp=weather_data['current']['temperature_2m']
    wind=weather_data['current']['wind_speed_10m']

    print(f"The current temperature in {city_name.title()}, {country} is {temp}°C")
    print(f"The current wind speed in {city_name.title()}, {country} is {wind} m/s")

get_weather("Delhi")