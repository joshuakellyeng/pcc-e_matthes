# 10.11 Favorite Number
from pathlib import Path
import json

def recall_fave_number():
    """Recalls a users favorite number."""
    path = Path('fave_number.json')
    contents = path.read_text()
    fave_number = json.loads(contents)
    print(f"I know your favorite number! It's {fave_number}.")

recall_fave_number()