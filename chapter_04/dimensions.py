# Tuples - an immutable list
dimensions = (200,50)

# print(dimensions[0])
# print(dimensions[1])

# dimensions[0] = 250
# Traceback (most recent call last):
#   File "/home/joshua-kelly/Desktop/python-books/python_work/chapter_04/dimensions.py", line 7, in <module>
    # dimensions[0] = 250
    # ~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
# tuples are defined by the presence of commas, 
# It doesn’t often make sense to build a tuple with one element, but this can happen when tuples are generated automatically.
# my_t = (3,)
# print(type(my_t))
# print(my_t)

# looping thru touples
print('\nOriginal dimensions:')
for dimension in dimensions:
    print(dimension)

print('\nModified dimensions:')
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)