import requests
import json


url = "https://api.openweathermap.org/data/2.5/weather?lat=44.977753&lon=-93.265015&units=imperial&appid=1d21e89e8a54cc7271a3bb5c38934787"

data = requests.get(url)

result = data.json()

# print(response.text)

print(json.dumps(result, indent =4, sort_keys=True ))

temp = result["main"]["temp"]
humidity = result["main"]["humidity"]
temp_max = result["main"]["temp_max"]
temp_min = result["main"]["temp_min"]
city_name = result["name"]
description = result["weather"][0]["description"]
feels_like = result["main"]["feels_like"]




print(humidity)