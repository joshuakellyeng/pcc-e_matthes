# ORGANIZING LISTS
# sort method sorts lists in alphabetical order and can never revert to original order
cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# can also sort in reverse order
# cars.sort(reverse=True)
# print(cars)

# SORTING A LIST TEMPORARILY W/ THE sorted() GLOBAL FUNCTION
# print("Here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)

# sorting in reverse order with the .reverse() method
print(cars)
cars.reverse()
print(cars)

# finding the length of a list with len() global function
print(len(cars))