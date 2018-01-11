from collections import Counter
from pprint import pprint

from os.path import isfile


def load_data(filepath):
    with open(filepath, encoding="utf-8") as file:
        return "".join(file.readlines())


def get_most_frequent_words(text):
    return Counter(text.lower().split()).most_common(10)


if __name__ == '__main__':
    while True:
        filepath = input("Enter the file path: ")
        if isfile(filepath):
            break
        else:
            print("There is no file at the specified path")

    text = load_data(filepath)

    print("The most popular words in this file:")
    pprint(get_most_frequent_words(text))
