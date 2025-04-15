# CHAPTER 3 LISTS

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)

# access list items using the index and bracket notation
# print(bicycles[0])

# you can combine string methods with bracket notation also
# print(bicycles[0].title())

# you can access the contents of a list in reverse order using negative numbers for example index -1 will always return the last element of a list, -2 the 2nd to last item and -3 the 3rd respectively
print(bicycles[-1].title())

message = f'My first bicycle was a {bicycles[0].title()}.'
print(message)
