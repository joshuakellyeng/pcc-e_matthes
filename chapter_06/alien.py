# CH6 - creating dictionaries and accessing key and value pairs
# alien_0 = {'color':'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']
# print(f'You just earned {new_points} points!')

# adding new key-value pairs
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
# dictionary elements are displayed in the order they were defined

# STARTING WITH AN EMPTY DICTIONARY
# alien_0 = {}
# print(alien_0)
# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

# MODIFYING VALUES IN A DICTIONARY
 # evaluates to green
# print(alien_0['color'])
# print(f'The alien is {alien_0['color']}.') 
# updating the value of key color
# alien_0['color'] = 'yellow'
# evaluates to the updated value of yellow 
# print(f'The alien is now {alien_0['color']}.') 

# ANOTHER EXAMPLE
# alien_0 = {'x_position':0, 'y_position': 25, 'speed': 'medium'}
# print(f'Original position: {alien_0['x_position']}')
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be a fast alien.
#     x_increment = 3

# The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(f'New position: {alien_0['x_position']}')

# REMOVING KEY-VALUE PAIRS
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# simple use del statement - this removes the key-value pair permenantly
del alien_0['points']
print(alien_0)