def forecast(*args):
    tuples = (arg for arg in args)
    weather_in_locations = {"Sunny": [], "Cloudy": [], "Rainy": []}

    for city, forecast in tuples:
        weather_in_locations[forecast].append(city)

    final_result = ""

    for key, value in weather_in_locations.items():
        sorted_v = sorted(value)
        for city in sorted_v:
            final_result += f"{city} - {key}"
            final_result += "\n"
    return final_result