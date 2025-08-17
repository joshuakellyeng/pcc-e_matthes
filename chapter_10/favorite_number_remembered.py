# 10.12 Favorite Number Remembered
from pathlib import Path
import json

path = Path('fave_number.json')

def fave_num_remembered():
    if path.exists():
        contents = path.read_text()
        fave_number = json.loads(contents)
        print(f"I know your favorite number! It's {fave_number}.")
    else:
        fave_num = input("What is your favorite number? ")
        contents = json.dumps(fave_num)
        path.write_text(contents)
        print("Thanks! I'll remember that number.")

fave_num_remembered()

# Book Solution
# path = Path('favorite_number.json')
# try:
#     contents = path.read_text()
# except FileNotFoundError:
#     number = input("What's your favorite number? ")
#     contents = json.dumps(number)
#     path.write_text(contents)
#     print("Thanks, I'll remember that.")
# else:
#     number = json.loads(contents)
#     print(f"I know your favorite number! It's {number}.")