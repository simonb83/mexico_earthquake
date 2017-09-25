import json
import sys


filename = sys.argv[1]
with open(filename) as f:
    geodata = json.loads(f.read())

coords = []

for feature in geodata['features']:
    # del feature['properties']['name']
    # del feature['properties']['profile_image_url']
    # del feature['properties']['screen_name']
    # del feature['properties']['text']
    # del feature['properties']['url']
    coords.append(feature['geometry']['coordinates'])

print(json.dumps(coords))