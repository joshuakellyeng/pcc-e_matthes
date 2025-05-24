from random import randint
from random import choice

d20 = randint(1,20)
print("D20 Roll Result:", d20)

players = ['beau', 'caleb', 'veth', 'yasha', 'cadeuces', 'fjord', 'jester']

first_up = choice(players)
print(first_up.title())
