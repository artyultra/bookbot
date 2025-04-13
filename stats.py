def get_num_words(text):
    """returns number of words in a document"""
    words = text.split()
    return len(words)


def char_count(text):
    """returns count of unique chars in a string"""
    unique_char = {}
    for char in text.lower():
        if char.isalpha():
            if char in unique_char:
                unique_char[char] += 1
            else:
                unique_char[char] = 1
    char_list = [{"char": char, "count": count} for char, count in unique_char.items()]

    def sort_on(dict):
        return dict["count"]

    char_list.sort(key=sort_on, reverse=True)

    sorted_dict = {}
    for item in char_list:
        sorted_dict[item["char"]] = item["count"]
    return sorted_dict
