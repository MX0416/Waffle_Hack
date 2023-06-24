import requests




url = "http://api.openweathermap.org/data/2.5/air_pollution?lat={50}&lon={50}&appid={1d21e89e8a54cc7271a3bb5c38934787}"


response = requests.get(url)
json = response.json()
print(json)