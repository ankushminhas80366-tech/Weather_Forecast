# Weather Forecast

Simple Python script that fetches the current temperature and wind speed for a city using the free Open-Meteo APIs.

## How it works

1. Takes a city name (hardcoded as `"Delhi"` in the example).
2. Calls the Open-Meteo Geocoding API to get the city's latitude and longitude.
3. Uses those coordinates with the Open-Meteo Forecast API to get current temperature (°C) and wind speed (m/s).
4. Prints the results.

## Requirements

- Python 3
- `requests` library (`pip install requests`)

## Usage

```bash
python main.py
```

To check another city, change the argument in the last line of `main.py`:

```python
get_weather("London")
```
