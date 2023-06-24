import requests


url = "https://api.openweathermap.org/data/2.5/forecast?lat=40.712776&lon=-74.005974&appid=1d21e89e8a54cc7271a3bb5c38934787"

response = requests.get(url)

json = response.json()

# print(response.text)

print(json)