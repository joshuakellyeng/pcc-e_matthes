# 5.1
# DEMO Conditional Test
car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')

# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

# Task write 10 more

family=['naomi', 'koa', 'deb', 'gen', 'viana']
nephew = family[1]
niece = family[0]
baby_sis = family[-1]
big_sis = family[2]
lil_sis = family[-2]

# print('Is my nephew named koa?: ',nephew == 'koa')
# print('Is my niece named naomi?: ',niece == 'naomi')
# print('Is my big sis named deb?: ', big_sis == 'deb')
# print('My baby sis is not carla!: ', baby_sis != 'carla')
# print('My lil sis is named charlie.: ', lil_sis == 'charlie')

# print('koa' in family, "should be true")
# print('carl' in family, 'should be false')
# print('bob' not in family, 'should be true')
# print('deb' not in family, 'should be false')
# print('gen' not in family, 'should be false')

# 5.2
# if nephew in family or niece in family:
#     print("Yeah they're family")

# print(nephew in family or niece in family)
# print('bob' in family or 'joe' in family)
# print('deb' in family and 'gen' in family)
# print('joe' in family and 'gen' in family)
# print(nephew.title() == family[0])

# 5.3
# Passes
alien_color = 'red'
# if alien_color == 'red':
#     print('Player has earned 10 points!')

# Fails
alien_color = 'yellow'
# if alien_color == 'green':
#     print('Player has earned 5 points!')

# 5.4
# if condition met
alien_color = 'green'
# if alien_color == 'green':
#     print('Player just earned 5 point for shooting the alien!')
# else:
#     print('Player just earned 10 points!')
# else condition
alien_color = 'red'
# if alien_color == 'green':
#     print('Player just earned 5 point for shooting the alien!')
# else:
#     print('Player just earned 10 points!')

# 5.5
alien_color = 'blue'
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15
# print(f'Player has earned {points} points!')

# 5.6
age = 3
if age < 2:
    person = 'baby'
elif age < 4:
    person = 'toddler'
elif age < 13:
    person = 'kid'
elif age < 20:
    person = 'teenager'
elif age < 65:
    person = 'adult'
else:
    person = 'elder'
# print(f'This person is a(n) {person}.')

# 5.7
fave_fruits = ['dragonfruit', 'mangoes', 'mandarines']

# if 'mangoes' in fave_fruits:
#     print('You really like mangoes!')
# if 'dragonfruit' in fave_fruits:
#     print('You really like dragonfruit!')
# if 'mandarines' in fave_fruits:
#     print('You really like mandarines!')
# if 'coconuts' in fave_fruits:
#     print('You really like coconuts!')
# if 'guava' in fave_fruits:
#     print('You really like guava!')

# 5.8
usernames = ['overabusiveness','synthetik','black_jones', 'captain_booty', 'admin']

# for username in usernames:
#     if username == 'admin':
#         print(f'Hello {username}, would you like a status report?')
#     else:
#         print(f'Hello {username}, thank you for logging in again.')

# 5.9
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'Hello {username}, would you like a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again.')
else:
    print("We need to find some users!")

# 5.10

current_users = ['OVERABUSIVENESS','Synthetik','BLACK_J0NES', 'captain_booty', 'Joker']

new_users = ['mercurial', 'noob_veteran', 'kirah_hellrose', 'overabusiveness', 'joker']

current_users_lower = [user.lower() for user in current_users]


for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'Sorry but the username: {new_user} is already in use.')
    else:
        print(f'Username: {new_user} is currently available.')

# 5.11
ordinal_nums = [num for num in range(1,10)]
print(ordinal_nums)
for num in ordinal_nums:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')
        

# 5.12
# styling python use spaces for readibility even if the code runs with no spaces
# this
# if age < 4: 
# is better than:
# if age<4:

# 5.13
# I'd like to create an online patient portal
# I'd like to create healthcare techknowledgy that is agnostic to goverments and countries. Systems anyone use to share information between organizations and help give patients better healthcare on a global scale.