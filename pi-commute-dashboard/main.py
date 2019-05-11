import argparse

parser = argparse.ArgumentParser(description='Start pi-commute-dashboard')
parser.add_argument('--transportApiId', type=str, nargs=1, required=True)
parser.add_argument('--transportApiKey', type=str, nargs=1, required=True)

args = parser.parse_args()
print(args.transportApiId)
print(args.transportApiKey)