def main():
    path = "/Users/michaelricardo/workspace/github.com/MikeRick101/bookbot/books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    letter_dict = count_letters(text)
    dict_list = list_of_dict(letter_dict)
    dict_list.sort(reverse=True,key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print_list(dict_list)
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    words = string.split()
    return len(words)

def count_letters(string):
    lower_string = string.lower()
    valid_letters = "abcdefghijklmnopqrstuvwxyz"
    letter_dict = {}
    for letter in lower_string:
        if letter not in valid_letters:
            continue
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def list_of_dict(dict):
    letter_count_list = []
    for key in dict:
        temp_dict = {}
        temp_dict["letter"] = key
        temp_dict["num"] = dict[key]
        letter_count_list.append(temp_dict)
    return letter_count_list

def sort_on(dict):
    return dict["num"]

def print_list(list):
    for dict in list:
        letter = dict["letter"]
        num = dict["num"]
        print(f"The {letter} character was found {num} times")
main()
