banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish.')

# in and not in is a way to check thru lists in python that returns a boolean value
print(user not in banned_users)