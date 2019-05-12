import argparse
import transport
import weather
import unicorn
import recommendation
import datetime
import time

parser = argparse.ArgumentParser(description='Start pi-commute-dashboard')
parser.add_argument('--transportApiId', type=str, nargs=1, required=True)
parser.add_argument('--transportApiKey', type=str, nargs=1, required=True)
parser.add_argument('--openWeatherMapApiKey', type=str, nargs=1, required=True)
parser.add_argument('--fromPostcode', type=str, nargs=1, required=True)
parser.add_argument('--toPostcode', type=str, nargs=1, required=True)
parser.add_argument('--fromStation', type=str, nargs=1, required=True)
parser.add_argument('--toStation', type=str, nargs=1, required=True)
parser.add_argument('--operator', type=str, nargs=1, required=True)
parser.add_argument('--fromCity', type=str, nargs=1, required=True)
parser.add_argument('--toCity', type=str, nargs=1, required=True)
parser.add_argument('--departureHour', type=int, nargs=1, required=True)
parser.add_argument('--returnHour', type=int, nargs=1, required=True)
parser.add_argument('--latestDepartureHour', type=int, nargs=1, required=True)

args = parser.parse_args()

trains = transport.Trains(args.transportApiId[0], args.transportApiKey[0])
departures = trains.GetDepartures(args.fromStation[0], args.toStation[0], args.operator[0])
print(departures)

weather = weather.Weather(args.openWeatherMapApiKey[0])

forecast_departure = weather.GetWeatherForecast(args.fromCity[0], args.departureHour[0])
forecast_return = weather.GetWeatherForecast(args.toCity[0], args.returnHour[0])

latest_departure_time = datetime.datetime.now().replace(hour=args.latestDepartureHour[0], minute=0)
latest_departure_timestamp = int(time.mktime(latest_departure_time.timetuple()))

recommended_transport = recommendation.recommend_transport(forecast_departure, forecast_return, departures, latest_departure_timestamp)
print('Recommended transport: {0}'.format(recommended_transport))

unicorn.show_summary(recommended_transport)

unicorn.show_weather_report(forecast_departure, is_return=False)
unicorn.show_weather_report(forecast_return, is_return=True)

unicorn.show_train_departures(departures)