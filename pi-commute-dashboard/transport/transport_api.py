import requests
import json
from dateutil import parser
from enum import Enum
import collections

def make_car_request(api_id, api_key, from_postcode, to_postcode):
    url = "http://transportapi.com/v3/uk/car/journey/from/postcode:{0}/to/postcode:{1}.json?app_id={2}&app_key={3}".format(from_postcode, 
        to_postcode, 
        api_id, 
        api_key)
    response = requests.get(url)

    parsed_json = json.loads(response.text)
    shortest_route = sorted(parsed_json['routes'], key=(lambda x: get_seconds_from_time(x['duration'])))[0]
    
    CarJourney = collections.namedtuple('CarJourney', 'time_in_seconds distance from_name to_name')
    return CarJourney(time_in_seconds=get_seconds_from_time(shortest_route['duration']), 
                        distance=shortest_route['distance'], 
                        from_name=shortest_route['from_point_name'], 
                        to_name=shortest_route['to_point_name'])

def get_seconds_from_time(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def make_train_request(api_id, api_key, from_station, to_station, operator):
    url = "http://transportapi.com/v3/uk/train/station/{0}/live.json?app_id={1}&app_key={2}&calling_at={3}&operator={4}".format(
        from_station,  
        api_id, 
        api_key,
        to_station,
        operator)
    response = requests.get(url)

    parsed_json = json.loads(response.text)
    departures = parsed_json['departures']['all']
    
    return [create_train_departure(d, from_station, to_station) for d in departures]

def create_train_departure(raw_departure, origin, destination):
    TrainDeparture = collections.namedtuple('TrainDeparture', 'status departure_time')
    return TrainDeparture(status=parse_train_status(raw_departure['status']),
                            departure_time=raw_departure['expected_departure_time'])

def parse_train_status(status):
    if status == 'LATE':
        return TrainStatus.LATE
    if status == 'CANCELLED':
        return TrainStatus.CANCELLED
    if status == 'ON TIME' or status == 'STARTS HERE' or status == 'EARLY':
        return TrainStatus.OK

    return TrainStatus.UNKNOWN
    
class TrainStatus(Enum):
    OK = 1
    LATE = 2
    CANCELLED = 3
    UNKNOWN = 4