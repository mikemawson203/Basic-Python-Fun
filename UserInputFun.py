def weather_condition(temperature):
    if temperature > 22:
        return "Too Warm"
    else:
        return "Perfect"


user_input = float(input('what is the temperature of the house: '))
print(weather_condition(user_input))
