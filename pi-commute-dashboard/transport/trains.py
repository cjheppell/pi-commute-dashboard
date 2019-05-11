from .transport_api import make_train_request

class Trains:
    def __init__(self, transport_api_id, transport_api_key):
        self.api_id = transport_api_id
        self.api_key = transport_api_key
    
    def GetDepartures(self, from_station, to_station, operator):
        departures = make_train_request(self.api_id, self.api_key, from_station, to_station, operator)
        return departures