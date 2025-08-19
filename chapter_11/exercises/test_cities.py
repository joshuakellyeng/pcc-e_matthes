from city_functions import city_country

def test_city_country():
    """Does city and countries like 'Santiago Chile' work?"""
    formatted_origin = city_country('santiago', 'chile')
    assert formatted_origin == "Santiago, Chile"

def test_city_country_population():
    """Does adding a population to the city work?"""
    formatted_origin = city_country('santiago', 'chile', population=5000000)
    assert formatted_origin == "Santiago, Chile - population 5000000"