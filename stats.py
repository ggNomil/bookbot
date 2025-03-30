def count_words(text):
    counter = 0
    split_text = text.split()
    for word in split_text:
        counter += 1
    return counter

def sort_dictionary(dictionary):
    sorted_dictionary = sorted(dictionary.items(), key=lambda item: item[1])
def count_characters(text):
    appearances = {}
    lowercase_text = text.lower()
    lowercase_text = lowercase_text.split()
    for word in lowercase_text:
        for char in word:
            if char in appearances:
                appearances[char] += 1
            elif char not in appearances:
                appearances[char] = 1

    appearances_sorted = dict(sorted(appearances.items(), key=lambda item: item[1], reverse=True))
    return appearances_sorted