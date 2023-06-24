import requests
import json


# Lat then Long
city_dict = {"Minneapolis" : [44.977489, -93.264374], "Seattle" : [47.6062, 122.3321], "New York" : [40.7128, 74.0060]}

user_city = "n"

while user_city != ("quit" or city_dict.keys()):
    print("Choose a pre dertimend citys weather or quit")
    for keys in city_dict:
        print(keys)
    
    user_city = input("")

lat = city_dict["user_city"][0]
long = city_dict["user_city"][1]

url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&units=imperial&appid=1d21e89e8a54cc7271a3bb5c38934787"
data = requests.get(url)
result = data.json()



#print(json.dumps(result, indent =4, sort_keys=True ))

temp = result["main"]["temp"]
humidity = result["main"]["humidity"]
temp_max = result["main"]["temp_max"]
temp_min = result["main"]["temp_min"]
city_name = result["name"]
description = result["weather"][0]["description"]
feels_like = result["main"]["feels_like"]


print("In " + city_name + " current temp is " + temp + " but it feels like" + feels_like)
print("The humidity is " + humidity + " with the max temperature being " + temp_max + " and the low for the day being " + temp_min)
print("The weather outside would be described as " + description)

