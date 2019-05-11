from .transport_api import make_car_request

class RoadTraffic:
    def __init__(self, transport_api_id, transport_api_key):
        self.api_id = transport_api_id
        self.api_key = transport_api_key
    
    def GetJourney(self, start_postcode, destination_postcode):
        car_journey = make_car_request(self.api_id, self.api_key, start_postcode, destination_postcode)
        return car_journey