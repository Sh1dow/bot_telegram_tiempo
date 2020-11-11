#!/usr/bin/python3
# -*- coding_ utf-8 -*-

import requests
import json

url = "https://api.openweathermap.org/data/2.5/onecall?lat=28.4853&lon=-16.32014&app    id=c9b10045ffec1ed3b67f9e67daeb3700&units=metric"

class weather:
    def __init__():
        url = "https://api.openweathermap.org/data/2.5/onecall?lat=28.4853&lon=-16.32014&app    id=c9b10045ffec1ed3b67f9e67daeb3700&units=metric"

    def tiempo():
        response = requests.get(url)
        data = json.loads(response.text)

        current = data["current"]["weather"][0]["main"]

        return current

