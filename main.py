import sys

from stats import count_words
from stats import count_characters
from sys import argv

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    counter = count_words(book_text)
    characters = count_characters(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {counter} total words")
    print("--------- Character Count --------")
    for key in characters.keys():
        print(f"{key}: {characters[key]}")
    print("============= END ===============")

main()