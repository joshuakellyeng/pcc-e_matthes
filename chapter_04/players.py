players = ['charles', 'martina', 'michael', 'florence', 'eli']
# this is called slicing a list its not inclusive
print(players[0:3])

print(players[1:4])

# omitting the first index starts slice at beginning
print(players[:4])

# similarly ommiting the second index value grabs everything after the first index
print(players[2:])

# using this can print the last x items of a list for example 
# this keeps working regardless of the size of the list regardless or if its size changes
print(players[-3:])
# prints the last 3 items in a given list

# Looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())