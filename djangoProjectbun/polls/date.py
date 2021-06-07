import json
from datetime import datetime, timezone
from pprint import pprint

import arrow
import requests

# Get first hour of today
from django.http import HttpResponse
from polls.models import Weather

import polls.models

response = requests.get(
    'https://api.stormglass.io/v2/weather/point',
    params={
        'lat': 34.7507,
        'lng': 29.70554,
        'params': ','.join(['airTemperature', 'pressure', 'windDirection', 'windSpeed',
                            'visibility', 'waterTemperature', 'cloudCover']),
        'source': 'sg'
    },
    headers={
        'Authorization': '7336f1a2-c6ea-11eb-80ed-0242ac130002-7336f21a-c6ea-11eb-80ed-0242ac130002'
    }
)

json_data = response.json()


# print(json_data) am comentat o pentru a nu mi afisa de fiecare data cand rulez datele in consola


def getData():
    return json_data


jsonData = getData()
dictionare = jsonData['hours']
# pprint(jsonData) am comentat o pentru a nu mi afisa de fiecare data cand rulez datele in consola

for i in dictionare:
    # aici imi ia datele dupa care mi le introduce in db
    a = i['airTemperature']["sg"]
    b = i['cloudCover']["sg"]
    c = i['pressure']["sg"]
    d = i['visibility']["sg"]
    e = i['waterTemperature']["sg"]
    f = i['windDirection']["sg"]
    g = i['windSpeed']["sg"]

    datedb = Weather(a, b, c, d, e, f, g)
    datedb.save()
