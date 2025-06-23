# 10.2 Learning C

from pathlib import Path

path = Path('chapter_10/text_files/learning_python.txt')

content = path.read_text()

for line in content.splitlines():
    new_line = line.replace('Python', 'C')
    print(new_line)
