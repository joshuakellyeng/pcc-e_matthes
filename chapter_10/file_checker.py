# 10.1 Learning Python
# File Reader
from pathlib import Path

path = Path("chapter_10/text_files/learning_python.txt")
content = path.read_text()

print(content)
# 10.3 Simpler Code - Use method chaining vs using variables for shortcuts
for line in content.splitlines():
    print(line, "Lines")


