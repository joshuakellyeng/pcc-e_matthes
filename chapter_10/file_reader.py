# Relative and Absolute Path Files
from pathlib import Path

path = Path('chapter_10/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
print(lines)
for line in lines:
    print(line)