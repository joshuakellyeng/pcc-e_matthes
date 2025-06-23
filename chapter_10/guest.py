# 10.4 Guest 
from pathlib import Path

guest_name = input("What is your name? \n")

path = Path('chapter_10/text_files/guest.txt')
path.write_text(guest_name)

