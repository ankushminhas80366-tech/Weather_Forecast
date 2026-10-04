import requests


def get_weather(city_name):
    """Look up a city and print its current temperature and wind speed.

    Open-Meteo needs coordinates, so this does two requests:
    geocode the city name, then fetch the forecast for those lat/lon.
    """
    # Step 1: turn the city name into latitude and longitude.
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&format=json"
    response = requests.get(url)
    data = response.json()

    # The geocoding API omits "results" when nothing matches the name.
    if "results" not in data:
        print(f"Could not find coordinates for {city_name}.")
        return

    # Use the top match only (count=1).
    lat = data["results"][0]["latitude"]
    lon = data["results"][0]["longitude"]
    country = data["results"][0].get("country", "")

    # Step 2: current conditions at those coordinates.
    # temperature_2m is in C; wind_speed_10m is in m/s.
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
        "&current=temperature_2m,wind_speed_10m"
    )
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    temp = weather_data["current"]["temperature_2m"]
    wind = weather_data["current"]["wind_speed_10m"]

    print(f"The current temperature in {city_name.title()}, {country} is {temp}°C")
    print(f"The current wind speed in {city_name.title()}, {country} is {wind} m/s")


# Example call. Change the city name to look up somewhere else.
get_weather("Delhi")
