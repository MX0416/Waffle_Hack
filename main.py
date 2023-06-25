import city_selection as c

repeat = "?"

while repeat != "no":
    print("Enter a city name to check its current weather! ")
    user_city = input(" >")
    c.city_name = user_city
    c.get_coordinates(user_city)
    c.get_weather(c.longitude, c.latitude)
    repeat = input("\n \nWould you like to check the weather for a different city? \nPlease enter yes/no: ")
    while repeat != "yes" and repeat != "no":
        repeat = input("Please enter yes or no: ")
    if repeat == "no":
        print("\nThank you for using this program! ")