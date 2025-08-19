# 11.01 City, Country
# def city_country(city, country):
#     """Generate a formatted city and country of origin."""
#     origin = f"{city}, {country}"
#     return origin.title()

# 11.02 Population
def city_country(city, country, population=0):
    """Generate a formatted city and country of origin."""
    if population:
        origin = f"{city.title()}, {country.title()} - population {population}"
    else:
        origin = f"{city.title()}, {country.title()}"
    return origin