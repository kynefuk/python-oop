

class WeirdSortee:
    def __init__(self, string, number, sort_by_num):
        self.string = string
        self.number = number
        self.sort_by_num = sort_by_num

    # 独自クラスをソートできるようにするには__lt__を定義する
    # less than [object]を判定
    def __lt__(self, object):
        if self.sort_by_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
        return f"{self.string}:{self.number}"