import requests
import json
from dateutil import parser
from enum import Enum
import collections
from .weather_condition import WeatherCondition

def make_current_weather_request(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}".format(location, 
        api_key)
    response = requests.get(url)

    parsed_json = json.loads(response.text)
    weather = parsed_json['weather']

    temp_kelvin = parsed_json['main']['temp']
    weather_type = parsed_json['weather'][0]['main']
    time = parsed_json['dt']
    return _make_weather_report(temp_kelvin, weather_type, time)

def make_weather_forecast_request(api_key, location, time_of_interest):
    url = "https://api.openweathermap.org/data/2.5/forecast?q={0}&appid={1}".format(location, 
        api_key)
    response = requests.get(url)

    parsed_json = json.loads(response.text)
    three_hourly_forecasts = parsed_json['list']
    closest_forecast_of_interest = min(three_hourly_forecasts, key=lambda x: abs(x['dt'] - time_of_interest))
    
    print(closest_forecast_of_interest)
    temp_kelvin = closest_forecast_of_interest['main']['temp']
    weather_type = closest_forecast_of_interest['weather'][0]['main']
    time = closest_forecast_of_interest['dt']
    return _make_weather_report(temp_kelvin, weather_type, time)

def _make_weather_report(temperature_kelvin, weather_type, time):
    WeatherReport = collections.namedtuple('WeatherReport', 'temp_c type time')
    return WeatherReport(temp_c=_celsius_from_kelvin(temperature_kelvin),
                        type=_parse_weather_type(weather_type),
                        time=time)

def _parse_weather_type(weather_type):
    weather_type = weather_type.lower()

    if weather_type == 'thunderstorm':
        return WeatherCondition.THUNDERSTORM
    if weather_type == 'drizzle':
        return WeatherCondition.DRIZZLE
    if weather_type == 'rain':
        return WeatherCondition.RAIN
    if weather_type == 'snow':
        return WeatherCondition.SNOW
    if weather_type == 'clear':
        return WeatherCondition.CLEAR
    if weather_type == 'clouds':
        return WeatherCondition.CLOUDS
    
    return WeatherCondition.UNKNOWN

def _celsius_from_kelvin(kelvin):
    return kelvin - 273.15