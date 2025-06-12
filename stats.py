def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_words_in_string(str):
    split_str = str.split()
    return len(split_str)


def get_chars_count(str):
    map = {}
    for char in str:
        c = char.lower()
        if c in map:
            map[c] += 1
        else:
            map[c] = 1
    return map


def sort_on(dict):
    return dict["num"]


def dict_to_list(dict):
    list = []
    for char in dict:
        list.append({"char": char, "num": dict[char]})
    list.sort(reverse=True, key=sort_on)
    return list
