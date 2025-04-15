# Copying Lists

# original
my_foods = ['pizza', 'falafel', 'carrot cake']
# the copy
friends_foods = my_foods[:]

# prove they are seperate lists by adding to them 
my_foods.append('cannoli')
friends_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

