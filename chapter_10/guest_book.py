# 10.5 Guest Book
from pathlib import Path

prompt = "\nHi what's your name? \n"
prompt += "Enter 'quit' if you are the last guest.\n"

path = Path('chapter_10/text_files/guest_book.txt')

guest_list = []
# Collecting guest names.
while True:
        guest_name = input(prompt)
        if guest_name == 'quit':
            break
        else:
            print(f"\nThank you for joining us this evening {guest_name}!")
            guest_list.append(guest_name)

# Build a string where "\n" is added after each name.
file_string = ''
for name in guest_list:
    file_string += f"{name}\n"

path.write_text(file_string)