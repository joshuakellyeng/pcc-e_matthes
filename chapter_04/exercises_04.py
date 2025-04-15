# 4.1
fave_pizzas = ['pepperoni', 'hawaiian', 'italian sausage', 'cheese', 'bayou-beast', 'margarita']

# for type_of_pizza in fave_pizzas:
    # print(f'I like {type_of_pizza} pizza.')
# 
# print("I really love pizza!\n")

# 4.2

types_of_cats = ['lion', 'ocelot', 'linx']
# for cat in types_of_cats:
    # print(f'The {cat} is a type of cat but might not make a great pet.')

# print('While they all may look like cuddly cats these felines make terrible pets.\n')

# 4.3
to_twenty = [num for num in range(1,21)]
# print(to_twenty)

# 4.4
to_one_million = [num for num in range(1,1_000_001)]
# print(to_one_million)

# 4.5
# print(min(to_one_million))
# print(max(to_one_million))
# print(sum(to_one_million))

# 4.6

odd_nums = [num for num in range(1,21,2)]
# print(odd_nums)

# 4.7
by_threes = [num for num in range(3,31,3)]
# print(by_threes)

# 4.8 
cubes = []
# for value in range(1,11):
    # cubed = value**3
    # cubes.append(cubed)
    # print(cubes)

# 4.9
cube_comprehension = [value**3 for value in range(1,11)]
# print(cube_comprehension)

# 4.10
# print(fave_pizzas)
# i - first 3
# print(f'The first three items in the list are: {fave_pizzas[:3]}\n')
# ii - middle 3
# print(f"Three items from the middle of the list are: {fave_pizzas[2:5]}\n")
# iii - last 3
# print(f"The last three items in the list are: {fave_pizzas[-3:]}\n")

# 4.11
friends_pizzas = fave_pizzas[:]

fave_pizzas.append('buffalo chicken')
friends_pizzas.append('goat curry')

# print(fave_pizzas)
# print(friends_pizzas)

# 4.12

# for pizza in fave_pizzas:
#     print(pizza.title())

# print('\n')

# for pizza in friends_pizzas:
#     print(pizza.title())

# 4.13
buffet_foods = ('rice', 'chicken', 'salad', 'shrimp', 'ice cream')
print('\n')
# i
for food in buffet_foods:
    print(food)
# ii
# buffet_foods[0] = 'puddin'
# iii
buffet_foods = ('lasagna', 'macaroni', 'salad', 'shrimp', 'ice cream')
for food in buffet_foods:
    print(food.title())

# 4.14
# Skim thru https://python.org/dev/peps/pep-0008

# 4.15
# i
# set up editor to insert 4 spaces for 1 tab vs code does this out the box
# ii
# set ruler in settings to 80 to measure the character limit per line according
# to PEP 8
# iii
# Don't use blank lines excessively (duh)