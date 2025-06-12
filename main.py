from stats import get_book_text
from stats import get_chars_count
from stats import dict_to_list
from stats import get_words_in_string
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    words = get_words_in_string(text)
    count = get_chars_count(text)
    list = dict_to_list(count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for e in list:
        print(f"{e['char']}: {e['num']}")


main()
