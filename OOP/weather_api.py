import os
from dataclasses import dataclass
from requests.exceptions import ConnectionError, ReadTimeout, HTTPError
import requests


API_KEY = os.getenv("API_KEY")


class WeatherAPI:
    API_URL = f"https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_weather(self, city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        try:
            response = requests.get(self.API_URL,params=params, timeout=1)
            response.raise_for_status()
        except ConnectionError:
            return 'Connection is not established.'
        except ReadTimeout:
            return 'Timeout for this request.'
        except HTTPError:
            return '404 Client Error: Not Found for url'
        else:
            if response.status_code == 200:
                data = response.json()
                result = Weather(
                    data['name'],
                    data['main']['temp'],
                    data['main']['humidity'],
                    data['wind']['speed']
                )
                return result
            return response.status_code

@dataclass
class Weather:
    city: str
    temperature: int
    humidity: int
    wind_speed: int

    def __str__(self):
        return (f"📍 City: {self.city}\n"
                f"🌡 Temperature: {self.temperature}°C\n"
                f"💧 Humidity: {self.humidity}%\n"
                f"💨 Wind Speed: {self.wind_speed} m/s")

api = WeatherAPI(API_KEY)
print(api.get_weather('London'))
