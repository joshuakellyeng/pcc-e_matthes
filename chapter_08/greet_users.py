# Passing a List
def greet_users(names):
    """Print simple greeting to each user in the list"""
    for name in names:
        msg = f"Hi, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
