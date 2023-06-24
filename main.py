import city_selection

repeat = "?"

while repeat != "no":
    print("Enter a city name from this list to check its current weather: ")
    for keys in city_selection.city_dict:
        print(keys)
    user_city = input(" >")
    if user_city in city_selection.city_dict:
        lat = city_selection.city_dict[user_city][0]
        long = city_selection.city_dict[user_city][1]
    city_selection.get_weather(long, lat)
    repeat = input("Would you like to check the weather for a different city? \nPlease enter yes/no: ")