import transport
from transport import TrainStatus
from transport import Transport
from weather import WeatherCondition
import datetime
import time

acceptable_weather_types = [WeatherCondition.CLEAR, WeatherCondition.CLOUDS, WeatherCondition.DRIZZLE]
acceptable_train_statues = [TrainStatus.OK, TrainStatus.LATE]

def recommend_transport(outbound_weather, return_weather, outbound_train_journeys, latest_departure_timestamp):
    if not (is_weather_acceptible(outbound_weather) and is_weather_acceptible(return_weather)):
        print("Recommending CAR for transport as weather is not acceptable")
        return Transport.CAR
    acceptible_train_journeys = list(filter(lambda x: is_train_status_acceptible(x), outbound_train_journeys))
    
    if len(acceptible_train_journeys) == 0:
        print("Recommending CAR for transport as no acceptable train journeys are available")
        return Transport.CAR

    if not any(is_acceptible_departure_time(x, latest_departure_timestamp) for x in acceptible_train_journeys):
        print("Recommending CAR for transport as no acceptable train journey before latest departure time available")
        return Transport.CAR
    
    print("Recommending TRAIN as weather and departure times are acceptable")
    return Transport.TRAIN

def is_weather_acceptible(weather_report):
    return weather_report.type in acceptable_weather_types

def is_train_status_acceptible(train_journey):
    return train_journey.status in acceptable_train_statues

def is_acceptible_departure_time(train_journey, latest_departure_timestamp):
    hour, minute = train_journey.departure_time.split(':')
    time_of_interest = datetime.datetime.now().replace(hour=int(hour), minute=int(minute))
    departure_timestamp = int(time.mktime(time_of_interest.timetuple()))

    return departure_timestamp < latest_departure_timestamp