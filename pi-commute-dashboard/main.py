import argparse
import transport

parser = argparse.ArgumentParser(description='Start pi-commute-dashboard')
parser.add_argument('--transportApiId', type=str, nargs=1, required=True)
parser.add_argument('--transportApiKey', type=str, nargs=1, required=True)
parser.add_argument('--fromPostcode', type=str, nargs=1, required=True)
parser.add_argument('--toPostcode', type=str, nargs=1, required=True)
parser.add_argument('--fromStation', type=str, nargs=1, required=True)
parser.add_argument('--toStation', type=str, nargs=1, required=True)
parser.add_argument('--operator', type=str, nargs=1, required=True)

args = parser.parse_args()

road_traffic = transport.RoadTraffic(args.transportApiId[0], args.transportApiKey[0])
print(road_traffic.GetJourney(args.fromPostcode[0], args.toPostcode[0]))

trains = transport.Trains(args.transportApiId[0], args.transportApiKey[0])
print(trains.GetDepartures(args.fromStation[0], args.toStation[0], args.operator[0]))