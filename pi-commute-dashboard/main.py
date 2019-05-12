import argparse
import transport
import weather
import unicorn

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

args = parser.parse_args()

road_traffic = transport.RoadTraffic(args.transportApiId[0], args.transportApiKey[0])
car_journey = road_traffic.GetJourney(args.fromPostcode[0], args.toPostcode[0])
print(car_journey)

trains = transport.Trains(args.transportApiId[0], args.transportApiKey[0])
departures = trains.GetDepartures(args.fromStation[0], args.toStation[0], args.operator[0])
print(departures)

weather = weather.Weather(args.openWeatherMapApiKey[0])

forecast_departure = weather.GetWeatherForecast(args.fromCity[0], args.departureHour[0])
forecast_return = weather.GetWeatherForecast(args.toCity[0], args.returnHour[0])

unicorn.show_weather_report(forecast_departure)
unicorn.show_weather_report(forecast_return)

unicorn.show_train_departures(departures)
unicorn.show_car_journey(car_journey)