# 3.1
friends = ['Larry', 'Sam', 'Cliff', 'James', 'Erwin' ]
# print(friends[0])
# print(friends[1])
# print(friends[2])
# print(friends[3])
# print(friends[4])

# 3.2

# print(f'Hey {friends[4]}, wanna play something on Steam?')
# print(f'Hey {friends[3]}, wanna play something on Steam?')
# print(f'Hey {friends[2]}, wanna play something on Steam?')
# print(f'Hey {friends[1]}, wanna play something on Steam?')
# print(f'Hey {friends[0]}, wanna play something on Steam?')

# 3.3

bicycles = ['State Bicycle Co. ', 'Poseidon Redwood', 'Marin Gestalt 2', 'Fuji Feather']

# print(f'I would like to own a {bicycles[-1]} bicycle.')
# print(f'I would like to own a {bicycles[-2]} bicycle.')
# print(f'I would like to own a {bicycles[-3]} bicycle.')
# print(f'I would like to own a {bicycles[-4]} bicycle.')

# 3.4 

dinner_guests = ['Neil Degrasse Tyson', 'Malcolm X', 'Fred Hampton', 'Philip K Dick', 'Isaac Asimov']
# print(f"{dinner_guests[0]}, it would be an honor if you'd be my guest and join me for dinner.")
# print(f"{dinner_guests[4]}, it would be an honor if you'd be my guest and join me for dinner.")
# print(f"{dinner_guests[2]}, it would be an honor if you'd be my guest and join me for dinner.")
# print(f"{dinner_guests[1]}, it would be an honor if you'd be my guest and join me for dinner.")
# print(f"{dinner_guests[3]}, it would be an honor if you'd be my guest and join me for dinner.")

# 3.5
# print(f"It's unfortunate that Mr. {dinner_guests[-1]} can't make it.")

# dinner_guests[-1] = 'Ada Lovelace'
# print(dinner_guests)
# print(f"{dinner_guests[4]}, it would be an honor if you'd be my guest and join me for dinner.")
# print(f"{dinner_guests[0]}, it would be an honor if you'd be my guest and join me for dinner.")
# print(f"{dinner_guests[3]}, it would be an honor if you'd be my guest and join me for dinner.")
# print(f"{dinner_guests[1]}, it would be an honor if you'd be my guest and join me for dinner.")
# print(f"{dinner_guests[2]}, it would be an honor if you'd be my guest and join me for dinner.")

# 3.6
# dinner_guests.insert(0, 'James Baldwin')
# dinner_guests.insert(3, 'LeVar Burton')
# dinner_guests.append('Maya Angelou')

# print(dinner_guests)

# print(f"Welcome {dinner_guests[0]}, I've acquired us a larger table for the evening.")
# print(f"Welcome {dinner_guests[3]}, I've acquired us a larger table for the evening.")
# print(f"Welcome {dinner_guests[1]}, I've acquired us a larger table for the evening.")
# print(f"Welcome {dinner_guests[5]}, I've acquired us a larger table for the evening.")
# print(f"Welcome {dinner_guests[2]}, I've acquired us a larger table for the evening.")
# print(f"Welcome {dinner_guests[4]}, I've acquired us a larger table for the evening.")
# print(f"Welcome {dinner_guests[6]}, I've acquired us a larger table for the evening.")

# 3.7
# print("My apologies friends I can only have 2 guest for dinner at this moment.")
# print(f"Sorry {dinner_guests.pop(0)}, looks like we'll have to reschedule.")
# print(f"Sorry {dinner_guests.pop(1)}, looks like we'll have to reschedule.")
# print(f"Sorry {dinner_guests.pop(3)}, looks like we'll have to reschedule.")
# print(f"Sorry {dinner_guests.pop(-1)}, looks like we'll have to reschedule.")
# print(f"Sorry {dinner_guests.pop(-1)}, looks like we'll have to reschedule.")
# print(f"Sorry {dinner_guests.pop(-1)}, looks like we'll have to reschedule.")
# print(dinner_guests)

# print(f"Please have a seat, {dinner_guests[0]} and {dinner_guests[1]}.")
# del dinner_guests[-1]
# del dinner_guests[0]
# print(dinner_guests)

# 3.8
places_to_visit = ['japan', 'portugal', 'peru', 'new zealand', 'brazil', 'ivory coast']

print('original: ',places_to_visit)

print('sorted: ',sorted(places_to_visit))
print('still original: ',places_to_visit)

print('reversed: ',sorted(places_to_visit, reverse=True))
print('still original: ',places_to_visit)

places_to_visit.reverse()
print('current reversed state: ',places_to_visit)
places_to_visit.reverse()
print('back to original state: ', places_to_visit)

places_to_visit.sort()
print(places_to_visit)

places_to_visit.sort(reverse=True)
print(places_to_visit)

# 3.9
total_num_of_guests = len(dinner_guests)
print(f'I am having a total number of {total_num_of_guests} guests this evening.')

# 3.10

my_favorite_tech = ['Sony A6000', 'Lenovo T480', 'Kindle', 'Lenovo Legion Go']
# Access via indexing
print('My favorite tech for photography is: ', my_favorite_tech[0])
# access via indexing w. negative numbers
print('My favorite tech for gaming is: ', my_favorite_tech[-3])
# append() adds to end of list
my_favorite_tech.append('Tozo OpenEgo Earbuds')
# insert() takes an index and then value to add to the list
my_favorite_tech.insert(0, 'IPhone 14 Pro')
print(my_favorite_tech)
# pop removes the last value on a list and returns it/ can be used to store the popped value
earbuds = my_favorite_tech.pop()
print(earbuds)

# sorted global function makes a copy of your list and sorts w.o affecting the original

print('sorted copy: ',sorted(my_favorite_tech))
print('original: ',my_favorite_tech)
print('sorted reverse copy: ',sorted(my_favorite_tech, reverse=True))
print('still original: ',my_favorite_tech)

# permanant reverse with the list method reverse()
my_favorite_tech.reverse()
print(my_favorite_tech)
# permanant sort with list method sort()
my_favorite_tech.sort()
print(my_favorite_tech)

# permanant sort with list method sort() thats reversed
my_favorite_tech.sort(reverse=True)
print(my_favorite_tech)

# find the length of lists with len() global method
my_favorite_tech.append(earbuds)
print(my_favorite_tech)
print(len(my_favorite_tech))

# 3.11 
# deliberate error to showcase IndexError
# print(my_favorite_tech[6])

