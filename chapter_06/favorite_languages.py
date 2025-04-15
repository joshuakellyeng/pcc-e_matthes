# A DICTIONARY OF SIMILAR OBJECTS
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }

# print(favorite_languages)
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")



# Looping Through All Key-Value Pairs
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping Through All the Keys in a Dictionary
# for name in favorite_languages.keys():
    # print(name.title())

# Looping thru keys is also the default behavoir in which we can forgo the .keys() method
# for name in favorite_languages:
#     print(name.title())

# friends = ['phil', 'sarah']

# for name in favorite_languages:
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# print(favorite_languages.keys())

# Looping Through a Dictionary’s Keys in a Particular Order

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")


# Looping Through All Values in a Dictionary
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())


# Use a set in the event values are repeated if we only want to track unique values
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

# A List in a Dictionary

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite launguage is: {languages[0].title()}")
    else:
        print(f"\n{name.title()}'s favorite launguages are:")
        for language in languages:
            print(f"\t{language.title()}")






