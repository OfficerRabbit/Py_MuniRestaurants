import requests
import json
from pprint import pprint
from sodapy import Socrata

url = "https://data.muni.org/resource/mdfi-bspc.geojson"

response = requests.get(url)

#response = requests.get(url, headers=headers)

if response.ok:
    muni_data_json = response.text

with open('.\Muni_Data_GeoJSON.json', 'w') as outfile:
    outfile.write(muni_data_json)

