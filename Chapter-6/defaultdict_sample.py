from collections import defaultdict


def letter_frequency(sentence):
    # Whenever a key is accessed that is not already in the dictionary, it calls that function, with no parameters, to create a default value.
    frequencies = defaultdict(int)

    for letter in sentence:
        frequencies[letter] += 1
    return frequencies
