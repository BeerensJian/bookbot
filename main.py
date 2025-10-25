from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print(book_path)
    text = get_book_text(book_path)
    wordcount = count_words(text)
    letter_counts = count_characters(text)
    characters = sort_characters(letter_counts)
    print_report(book_path, wordcount, characters)


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in chars_sorted_list:
        print(f"{char['char']}: {char['count']}")
    print("============= END ===============")


main()
