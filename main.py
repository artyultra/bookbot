from stats import get_num_words, char_count
import sys


def main():
    """python script excercise manipulating .txt files"""
    path_to_book = ""
    if 1 < len(sys.argv) == 2:
        path_to_book = "./" + f"{sys.argv[1]}"
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(path_to_book)
    num_words = get_num_words(text)
    char_dict = char_count(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, val in char_dict.items():
        print(f"{key}: {val}")
    print("============= END ===============")


def get_book_text(path):
    """returns text from a book in books/"""
    with open(path, encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    main()
