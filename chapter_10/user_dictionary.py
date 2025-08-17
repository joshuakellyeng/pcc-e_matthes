# 10.13 User Dictionary
from pathlib import Path
import json

# path = Path('user_dictionary.json')

def get_new_username(path):
    """Prompt user for a name"""
    username = input("What is your name? ")
    game = input("What game are you currently playing? ")
    genre = input("What's your favorite genre of video games? ")
    user_info = {
        "name": username,
        "game": game,
        "genre": genre
    }
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def read_stored_user(path):
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None
    
def greet_user():
    """Greet user by name and what we know about them."""
    path = Path('user_dictionary.json')
    user_dict = read_stored_user(path)
    if user_dict:
        print(f"Welcome back, {user_dict['name']}!")
        print(f"Hope you've been playing some {user_dict['game']}.")
        print(f"Have you played any other {user_dict['genre']}'s lately?")
    else:
        user_dict = get_new_username(path)
        msg = f"We'll remember you when you return, {user_dict['name']}!"
        print(msg)


greet_user()