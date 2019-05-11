import requests
import json
from dateutil import parser
import typing

def make_car_request(api_id, api_key, from_postcode, to_postcode):
    url = "http://transportapi.com/v3/uk/car/journey/from/postcode:{0}/to/postcode:{1}.json?app_id={2}&app_key={3}".format(from_postcode, 
        to_postcode, 
        api_id, 
        api_key)
    response = requests.get(url)

    parsed_json = json.loads(response.text)
    shortest_route = sorted(parsed_json['routes'], key=(lambda x: get_seconds_from_time(x['duration'])))[0]
    
    return CarJourney(get_seconds_from_time(shortest_route['duration']), 
                        shortest_route['distance'], 
                        shortest_route['from_point_name'], 
                        shortest_route['to_point_name'])

class CarJourney(typing.NamedTuple):
    time_in_seconds: int
    distance: int
    from_name: str
    to_name: str

def get_seconds_from_time(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)