#!/usr/bin/python3


import requests
import json


api_key = "c9b10045ffec1ed3b67f9e67daeb3700"
lat = "48.208176"
lon = "16.373819"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

response = requests.get(url)
data = json.loads(response.text)

current = data["current"]
weather = current["weather"][0]["main"]

lluvia  = "Rain"

if weather == lluvia:
	print("llevate un paraguitas mi niño")
else:
	print("no pasa nada, para la playa todo el mundo")

	
