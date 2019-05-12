from .openweathermap_api import make_current_weather_request, make_weather_forecast_request
import time
import datetime

class Weather:
    def __init__(self, transport_api_key):
        self.api_key = transport_api_key
    
    def GetCurrentWeather(self, location):
        weather_report = make_current_weather_request(self.api_key, location)
        return weather_report

    def GetWeatherForecast(self, location, hour_of_interest):
        time_of_interest = datetime.datetime.now().replace(hour=hour_of_interest, minute=0)
        timestamp = int(time.mktime(time_of_interest.timetuple()))
        weather_report = make_weather_forecast_request(self.api_key, location, timestamp)
        return weather_report