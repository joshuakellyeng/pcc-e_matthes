# 10.8 Cats & Dogs
from pathlib import Path

# Correct Path
# cat_path = Path('./text_files/cats.txt')
# Error Triggering Path
cat_path = Path('./text_files/cat.txt')
dog_path = Path('./text_files/dogs.txt')

try:
    cat_content = cat_path.read_text()
    dog_content = dog_path.read_text()
except FileNotFoundError:
    print("Sorry this file seems to be missing.")
else:
    for line in dog_content.splitlines():
        print(line)

    for line in cat_content.splitlines():
        print(line)