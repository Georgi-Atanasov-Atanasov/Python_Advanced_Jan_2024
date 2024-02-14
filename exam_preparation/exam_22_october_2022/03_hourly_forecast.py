def forecast(*args):
    sunny_locations = []
    cloudy_locations = []
    rainy_locations = []
    for location, weather in args:
        if weather == "Sunny":
           sunny_locations.append(location)
        elif weather == "Cloudy":
            cloudy_locations.append(location)
        elif weather == "Rainy":
            rainy_locations.append(location)
    result = []
    for location in sorted(sunny_locations):
        result.append(f"{location} - Sunny\n")

    for location in sorted(cloudy_locations):
        result.append(f"{location} - Cloudy\n")
    for location in sorted(rainy_locations):
        result.append(f"{location} - Rainy\n")
    return (''.join(result))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

