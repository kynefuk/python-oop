from operator import attrgetter, itemgetter


l = [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]

# tuple[1]の値を元に降順にソート
l.sort(key=itemgetter(1), reverse=True)


class Score:
    def __init__(self, name, math, english):
        self.name = name
        self.math = math
        self.english = english


a = Score('a', math=80, english=90)
b = Score('b', math=60, english=100)
c = Score('c', math=75, english=50)

score_list = [a, b, c]

# keyにはlambdaよりitemgetter/attrgetterの方が読みやすい
score_list.sort(key=attrgetter('math'))
