# 6.1 Person

person = {
    'first_name': 'Linus',
    'last_name': 'Torvalds',
    'age': 55,
    'city': 'Helsinki'
    }

# print(f'The creator of Linux is a man by the name of {person['first_name']} {person["last_name"]}.')
# print(f"He was born in {person['city']} and is currently {person['age']} years old.")

# 6.2 Favorite Numbers
fave_numbers = {
    'crytal': 420,
    'janelle' : 1_000_000,
    'jael' : 32,
    'steve': 21,
    'chris': 90
}
# Looping through a dictionary
# for person in fave_numbers:
#     print(f"{person.title()}'s favorite number is: {fave_numbers[person]}")

# 6.3 Glossary
glossary = {
    'dictionary': 'a method of storing data in key value pairs.',
    'list': 'a data structure to store a collection of data.',
    'variables': 'a box that stores a type of data.',
    'function': 'a program that executes a block of code when called.',
    'boolean': 'a data type that is only ever True or False.',
    # 6.4 Glossary 2
    'string': 'a data type that is a series of characters.',
    'integer': 'a data type that is only exclusively whole numbers.',
    'float': 'a data type which uses decimals.',
    'modulo': 'an arithmetic operation used in division that only returns the remainder.',
    'set': 'a data structure that keeps of unique values and ignores any duplicates.'
}

# for word, definition in glossary.items():
#     print(f"\n{word.title()}:\n{definition.capitalize()}")

# 6.5 Rivers

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtse': 'china',
    'mississippi': 'usa',
    'mackenzie': 'canada'
}

# for river, country in rivers.items():
#     print(f'The {river.title()} runs through {country.title()}.')

# for river in rivers:
#     print(river.title())

# for country in rivers.values():
#     print(country.title())

# 6.6 Polling

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'naomy': 'java',
    'bronze': 'python',
    }

squad = ['naomy', 'abe', 'bronze', 'dex']
# a.
# for voter in favorite_languages:
#     print(f"Hi {voter.title()}")

#     if voter in squad:
#         language = favorite_languages[voter].title()
#         print(f"\tYo {voter.title()}! We know you love {language}! Thanks for voting in our poll!")
# b.
# for friend in squad:
    # if friend not in favorite_languages.keys():
    #     print(f"Hey {friend.title()}! Please don't forget to submit your vote.")


# 6.7 People
people =[]

ltorvalds = {
        'first_name': 'Linus',
        'last_name': 'Torvalds',
        'age': 55,
        'city': 'Helsinki',
        'created': 'Linux',
    }

people.append(ltorvalds)

sjobs = {
        'first_name': 'Steve',
        'last_name': 'Jobs',
        'age': 56,
        'city': 'San Francisco',
        'created': 'MacOS',
    }

people.append(sjobs)

bgates = {
        'first_name': 'Bill',
        'last_name': 'Gates',
        'age': 69,
        'city': 'Seattle',
        'created': 'Microsoft Windows',
    }

people.append(bgates)

# for person in people:
#     # print(f'\nPerson: {person}')
#     full_name = f"{person['first_name']} {person['last_name']}"
#     print(f"\n{full_name} famously known for creating {person['created']} \nwas born in {person['city']} and is currently {person['age']} years old.")


# 6.8 Pets
pets = []

pet_01 = {
    'name': 'cody',
    'species': 'dog',
    'breed': 'siberian husky',
    'fur_color': 'white',
    'size': 'large',
    'owner': 'genesis'
}

pet_02 = {
    'name': 'juno',
    'species': 'dog',
    'breed': 'siberian husky/chow mix',
    'fur_color': 'cream',
    'size': 'medium',
    'owner': 'deborah'
}

pet_03 = {
    'name': 'china',
    'species': 'dog',
    'breed': 'american pitbull terrier',
    'fur_color': 'white and black spotted',
    'size': 'medium',
    'owner': 'steve'
}

pets.append(pet_01)
pets.append(pet_02)
pets.append(pet_03)

# for pet in pets:
#     print(f"\n{pet['owner'].title()} has a {pet['species']} named {pet['name'].title()}, who is a {pet['breed'].title()} with {pet['fur_color']} fur and {pet['size']} sized.")

# 6.9 Favorite Places

favorite_places = {
    'josh': ['cadiz', 'santo domingo', 'new orleans'],
    'chris': ['springfield', 'san diego', 'new york city'],
    'jordan': ['san diego', 'asbury park', 'new york city']
}

# for person, places in favorite_places.items():
#     print(f"\n{person.title()}'s favorite places are:")
#     for place in places:
#         print(f"\t{place.title()}")

# 6.10 Favorite Numbers
fave_numbers_1 = {
    'crytal': [420, 123, 1337],
    'janelle' : [1_000_000, 1_000_000_000],
    'jael' : [32, 100, 42],
    'steve': [21, 69, 1111],
    'chris': [90, 1000, 411, 311]
}

# for person, numbers in fave_numbers_1.items():
#     print(f"{person.title()}'s favorite numbers are: ")
#     for number in numbers:
#         print(f"- {number}")

# 6.11 Cities

cities = {
    'cadiz': {
        'country': 'spain',
        'population': 114_442,
        'fact': 'is one of the oldest continuously inhabited cities in Western Europe'
    },
    'santo domingo': {
        'country': 'dominican republic',
        'population': 1_029_000,
        'fact': 'is the oldest permanent city established by Europeans in the Western Hemisphere'
    },
    'new orleans': {
        'country': 'USA',
        'population': 364_136,
        'fact': 'is widely considered the birthplace of jazz music'
        
    }
}

for city,details in cities.items():
    print(f"\n{city.title()} is a city in\n {details['country'].title()} has a population of {details['population']} and \n{details['fact']}.")

# 6.12 Extensions

bgates['company'] = "Microsoft"
sjobs['company'] = "Apple"
ltorvalds['company'] = 'The Linux Foundation'

bgates['created'] = ['Windows PC', 'Microsoft Office Suite']
sjobs['created'] = ['iPod', 'iPad', 'iMac']
ltorvalds['created'] = ['Linux Kernal', 'Git Version Control System']

print(people)

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\nDuring {full_name}'s time at {person['company']} they worked on and developed these products:")
    for item in person['created']:
        print(f"- {item}")