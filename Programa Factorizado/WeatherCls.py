#!/usr/bin/python3

import json
import requests


url = "https://api.openweathermap.org/data/2.5/onecall?lat=28.4853&lon=-16.32014&appid=c9b10045ffec1ed3b67f9e67daeb3700&units=metric"

class weather:

    def __init__(self):

        self.response = requests.get(url)

    def rain(self): 

        self.data = json.loads(self.response.text)
        self.current = self.data["current"]["weather"][0]["main"]

        return self.current

        
    
