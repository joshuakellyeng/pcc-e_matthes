# MODIFYING LISTS

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# CHANGES THE VALUE OF ELEMENTS ON THE LIST W? BRACKET NOTATION
# motorcycles[0] = 'ducati'

# APPEND METHOD - ADDS TO END OF LIST
# motorcycles.append('ducati')

# BUILDING LISTS DYNAMICALLY
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')


# INSERT METHOD - ADD ELEMENTS IN ANY POSITION .insert(position, element)
motorcycles.insert(0, 'ducati')

# REMOVING ELEMENTS FROM LISTS W/ del
# CANT ACCESS VALUE OF ELEMENTS REMOVED USING DEL
# print(motorcycles)

# del motorcycles[0]
# del motorcycles[1]


# REMOVING ELEMENTS WITH POP METHOD
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# YOU CAN POP ITEMS FROM ANYWHERE IN THE LIST BY PROVIDING AN INDEX
# first_owned = motorcycles.pop(0)
# print(f'The first motorcycle I owned was a {first_owned.title()}.')

# If your not planning on using the at all del is a fine way to remove an item from a list
# But if you do plan on using the item in some capacity .pop() would be a better choice

# REMOVING AN ITEM BY VALUE
print(motorcycles)
# if you only know the value of the item you want to remove you can use the .remove() method
# motorcycles.remove('ducati')

# another way is to pass a value
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')

# something to note the remove() method only deletes the first occurence pf the value specified. if there is more you'll have to combine it with a loop.


# print(motorcycles)
