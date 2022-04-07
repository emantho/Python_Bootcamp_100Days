travel_log = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Lille", "Guijon"],
        "total_visits": 12,
    },
    {
        "Country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]

# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇

new_country = {}


def add_new_country(country_visited, times_visited, cities_visited):
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = times_visited
    travel_log.append(new_country)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
