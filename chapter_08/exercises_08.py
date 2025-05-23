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

# def make_album(artist_name, album_title, tracks=None):
#     album = {
#         'title': album_title.title(),
#         'artist': artist_name.title()
#     }
#     if tracks:
#         album['tracks'] = tracks

#     return album

# album = make_album("deftones", 'around the fur')    
# print(album)

# album = make_album("bad bunny", 'debi tirar mas fotos')
# print(album)

# album = make_album('cleopatrick', 'doom',tracks=5)
# print(album)

# 8.8 User Album

# while True:
#     print("\nWhat is your favorite album and whose it by?")
#     print("(enter 'q' at any time to QUIT)")
#     album_name = input("Album Name: ")
#     if album_name == 'q':
#         break
#     artist_name = input("Artist Name: ")
#     if artist_name == 'q':
#         break
#     album = make_album(artist_name,album_name)
#     print(f"\n{album}")
# print("\nThanks for responding!")

# 8.9 Mwssages
text_messages = ['Hello Friend', "Yo what's up!", "Good Morning!"]

def show_messages(messages):
    for message in messages:
        print(message)

# show_messages(text_messages)

# 8.10 Sending Messages
text_messages = ['Hello Friend', "Yo what's up!", "Good Morning!"]
sent_messages = []

def show_messages(messages):
    """Prints messages from a list individually"""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Simulates the sending of a message from list and adds to a new list"""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# send_messages(text_messages, sent_messages)
# print("Text Messages: ",text_messages)
# print("Sent Messages: ",sent_messages)

# 8.11 Archived Messages

def show_messages(messages):
    """Prints messages from a list individually"""
    print("\nShowing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Simulates the sending of a message from list and adds to a new list"""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

show_messages(text_messages)
send_messages(text_messages[:], sent_messages)

print("\nFinal Lists:")
print("Curr. Message List:", text_messages)
print("Sent Message List:", sent_messages)

# 8.12 Sandwiches

def make_sandwich(*args):
    """Prints a summary of the sandwich being ordered"""
    print("\nThis customer wants the following on their sandwich:")
    for arg in args:
        print(f"- {arg}")

make_sandwich('mayo', 'lettuce', 'tomato', 'bacon')
make_sandwich('ham', 'egg')
make_sandwich('tuna', 'cheese')

# 8.13 User Profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_profile('Joshua', 'Kelly', class_type='artificer', proficiencies=["tinker's tools", 'arcana', 'sage'], languages=['python', 'javascript'])

print("\n")
# print(user_profile)

# 8.14 Cars
def make_car(make, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['make'] = make
    car_info['model'] = model

    return car_info

car=make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)

# 8.15 Printing Models
#  See `printing_functions.py`

# 8.16 Imports

# import person 
# new_person = person.build_person('Ulfric','Stormcloak')

# from person import build_person
# new_person = build_person('Ulfric','Stormcloak')

from person import build_person as bp
new_person = bp('Ulfric', 'Stormcloak')

print(new_person)