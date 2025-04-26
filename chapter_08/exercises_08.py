# 8.1 Message

def display_message():
    ''' This function simply states 
    what I am learning about in this chapter'''
    print("In Ch. 8 I am learning about writing functions and how passing arguments work.")

# display_message()

# 8.2 Favorite Book
def favorite_book(title):
    """Prints out what a users favorite book is"""
    print(f"One of my favorite books is {title.title()}.")

# favorite_book("neuromancer")

# 8.3 T-Shirt

# def make_shirt(shirt_size, message):
#     """Print the size of a tshirt and the message on it."""
#     print(f"Shirt Size: {shirt_size.upper()}")
#     print(f"Shirt Message: {message.title()}")

# make_shirt("xl", 'arch-mages')

# 8.4 Large Shirts

def make_shirt( message, shirt_size='l'):
    """Print the size of a tshirt and the message on it."""
    print(f"Shirt Size: {shirt_size.upper()}")
    print(f"Shirt Message: {message.title()}")

# make_shirt('i love python')
# make_shirt(shirt_size='m', message='i love linux')

# 8.5 Cities

def describe_city(city_name, country="spain"):
    """Displays a city and country of origins"""
    print(f"{city_name.title()} is in {country.title()}.")

# describe_city("cadiz")
# describe_city("sevilla")
# describe_city("new york city", "united states")

# 8.6 City Names

def city_country(city, country):
    """Return a string of a city and the country of origin"""
    location = f"{city.title()}, {country.title()}"
    return location

city = city_country('san juan', 'puerto rico')
# print(city)

city = city_country('sao paulo', 'brazil')
# print(city)

city = city_country('porto', 'portugal')
# print(city)

# 8.7 Album

def make_album(artist_name, album_title, tracks=None):
    album = {
        'title': album_title.title(),
        'artist': artist_name.title()
    }
    if tracks:
        album['tracks'] = tracks

    return album

album = make_album("deftones", 'around the fur')    
print(album)

album = make_album("bad bunny", 'debi tirar mas fotos')
print(album)

album = make_album('cleopatrick', 'doom',tracks=5)
print(album)

# 8.8 User Album

while True:
    print("\nWhat is your favorite album and whose it by?")
    print("(enter 'q' at any time to QUIT)")
    album_name = input("Album Name: ")
    if album_name == 'q':
        break
    artist_name = input("Artist Name: ")
    if artist_name == 'q':
        break
    album = make_album(artist_name,album_name)
    print(f"\n{album}")
print("\nThanks for responding!")