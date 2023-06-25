import requests

latitude = 0
longitude = 0
city_name = ""

def get_coordinates(city_name):
    
    global latitude, longitude
    api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(city_name)
    response = requests.get(api_url, headers={'X-Api-Key': 'CDsYwIecXfRCxv0m4/RPJA==DIvZZ2xJbskxagOs'})

    if response.status_code == requests.codes.ok:
        result = response.json()
        latitude = result[0]["latitude"]
        longitude = result[0]["longitude"]
    else:
        print("Error:", response.status_code, response.text)

"""
  function that takes in one parameter: the name of any city.
  uses api-ninjas' data to obtain longitude and latitudes of the user's selected city, then passes the result to the longitude and latitude variables created at the top.
"""


def get_weather(long, lat):
    
    print(latitude, longitude)
    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&units=imperial&appid=1d21e89e8a54cc7271a3bb5c38934787"
    data = requests.get(url)
    result = data.json()

    #print(json.dumps(result, indent =4, sort_keys=True ))

    temp = result["main"]["temp"]
    humidity = result["main"]["humidity"]
    temp_max = result["main"]["temp_max"]
    temp_min = result["main"]["temp_min"]
    description = result["weather"][0]["description"]
    feels_like = result["main"]["feels_like"]

    print(f"In {city_name} the current temperature is {temp} degrees Fahrenheit but it feels like {feels_like}F,")
    print(f"the humidity is {humidity}g.m-3, with the max temperature being {temp_max}F and the low for the day being {temp_min}F,")

    # FIXME: how do we write the unit for humidity? its supposed to be g.m-3, which is units of grams of water vapour per cubic metre of air.

    print(f"the weather outside would be described as {description}!")

    # FIXME: this doesn't make sense when it prints out, it would read as "~~ described as clear sky"

"""
  function that takes in two parameters: longitude and latitude of any city.
  uses openweather's api to obtain weather information on the given city and prints the information.
"""