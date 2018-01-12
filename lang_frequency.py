from collections import Counter
import sys
import re


def load_data(filepath):
    with open(filepath, encoding="utf-8") as file:
        return file.read()


def get_most_frequent_words(text, words_count=10):
    words = re.findall(r"[a-zа-я\-]+", text.lower())
    return Counter(words).most_common(words_count)


def print_words(most_common):
    for word, count in most_common:
        print("{} - {} повторений".format(word, count))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        exit("Ошибка: Отсутствует путь к файлу")

    try:
        text = load_data(filepath)
    except FileNotFoundError:
        exit("Ошибка: файл не найден")

    print("Самые популярные слова в файле:")
    print_words(get_most_frequent_words(text))
