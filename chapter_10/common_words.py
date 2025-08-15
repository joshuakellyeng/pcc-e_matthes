# 10.10 Common Words
from pathlib import Path

# Files
the_whale_path = './text_files/the_whale.txt'
les_mis_path = './text_files/les_mis.txt'
alice_path = './text_files/alice.txt'

# Initial Attempt
def common_word_counter(file_path, word):
    """Count how many times word appears in the text."""
    path = Path(file_path)
    try:
        content = path.read_text()
    except FileNotFoundError:
        pass
    else:
        word_count = content.lower().count(word)
        msg = f"The word '{word}' appears about {word_count} times in this text."
        print(msg)

common_word_counter(the_whale_path, "the")
common_word_counter(les_mis_path, "then")
common_word_counter(alice_path, "there")
print('\n')
common_word_counter(the_whale_path, "then ")

# Textbook Solution
def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    # Note: This is a really simple approximation, and the number returned
    #   will be higher than the actual count.
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)
