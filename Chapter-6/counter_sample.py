from collections import Counter

responses = [
    'vanilla',
    'chocolate',
    'vanilla',
    'vanilla',
    'caramel',
    'strawberry'
]


def letter_frequency(sentence):
    return Counter(sentence)


counter = letter_frequency(responses)

# most_common(lank)で上位lank位まで取得
print(counter.most_common(2))
