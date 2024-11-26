def main():
    """python script excercise manipulating .txt files"""
    path_to_book = "./books/frankenstein.txt"
    text = get_book_text(path_to_book)
    num_words = get_word_count(text)
    char_dict = char_count(text)
    print(
        f"--- BEGIN REPORT OF books/frankenstein.txt ---\n{num_words} words found in document\n"
    )
    for key, val in dict(sorted(char_dict.items())).items():
        print(f"The {key} character was found {val} times")
    print("--- END REPORT ---")


def get_book_text(path):
    """returns text from a book in books/"""
    with open(path, encoding="utf-8") as f:
        return f.read()


def char_count(text):
    """returns count of unique chars in a string"""
    unique_char = {}
    for char in text.lower():
        if "a" <= char <= "z":
            if char in unique_char:
                unique_char[char] += 1
            else:
                unique_char[char] = 1
    return unique_char


def get_word_count(text):
    """returns number of words in a document"""
    words = text.split()
    return len(words)


if __name__ == "__main__":
    main()
