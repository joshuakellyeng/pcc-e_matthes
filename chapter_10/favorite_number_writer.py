# 10.11 Favorite Number
from pathlib import Path
import json


def get_fave_number():
    """Stores a users favorite number."""
    path = Path('fave_number.json')
    fave_num = input("What is your favorite number? ")
    contents = json.dumps(fave_num)
    path.write_text(contents)
    print("Thanks! I'll remember that number.")
    


get_fave_number()
