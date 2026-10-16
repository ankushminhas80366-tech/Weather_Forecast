# Weather Forecast 🌤️

A simple and lightweight Python script that fetches the **current temperature** and **wind speed** for any city in the world using the free [Open-Meteo](https://open-meteo.com/) APIs.

No API key required!

---

## ✨ Features

- Get current temperature in °C
- Get current wind speed in m/s
- Works for any city worldwide
- Uses free Open-Meteo Geocoding + Forecast APIs
- Clean and easy-to-read output
- No API key needed

---

## 📋 Requirements

- Python 3.6 or higher
- `requests` library

Install the required package:

```bash
pip install requests
```

---

## 🚀 How to Use

1. Clone the repository:

```bash
git clone https://github.com/ankushminhas80366-tech/Weather_Forecast.git
cd Weather_Forecast
```

2. Run the script:

```bash
python main.py
```

By default it checks the weather for **Delhi**.

### Check weather for another city

Open `main.py` and change the last line:

```python
get_weather("London")      # or any city you want
get_weather("New York")
get_weather("Tokyo")
get_weather("Mumbai")
```

Then run the script again.

---

## 📸 Example Output

```
The current temperature in Delhi, India is 28.5°C
The current wind speed in Delhi, India is 3.2 m/s
```

---

## 🔧 How It Works

1. **Geocoding**: The script first calls the Open-Meteo Geocoding API to convert the city name into latitude and longitude.
2. **Weather Data**: Using those coordinates, it calls the Open-Meteo Forecast API to get the current temperature (`temperature_2m`) and wind speed (`wind_speed_10m`).
3. **Display**: It prints a clean, human-readable summary including the country name.

---

## 📁 Project Structure

```
Weather_Forecast/
├── main.py          # Main script
└── README.md        # This file
```

---

## 🛠️ Technologies Used

- **Python 3**
- **requests** – for making HTTP requests
- **Open-Meteo APIs** – free weather and geocoding services

---

## 📌 Notes

- The script uses the first matching result from the geocoding API.
- If the city name is not found, it will display a friendly error message.
- Temperature is always in Celsius and wind speed is in meters per second.

---

## 🤝 Contributing

Feel free to fork this repository, make improvements, and submit a pull request!

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
