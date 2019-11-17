import collections
from dataclasses import dataclass, make_dataclass


Stock = collections.namedtuple('Stock', ('symbol', 'current', 'high', 'low'))

# make_dataclassでデータクラスを定義
DClass = make_dataclass('DClass', ('symbol', 'current', 'high', 'low'))

dclass = DClass(1, 2, 3, 4)

# データクラスはミュータブルなので属性値の変更が可能
dclass.symbol = 'hoge'

# 属性の追加も可能
dclass.extra = 'extra'


# @dataclassを付けることで、 __init__や__str__などを自動生成してくれる。
@dataclass
class StockedDecorated:
    name: str
    current: float
    high: float = 0.0  # デフォルト値
    low: float = 0.0   # デフォルト値
