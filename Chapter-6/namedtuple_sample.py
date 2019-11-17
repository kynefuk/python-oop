from collections import namedtuple

Stock = namedtuple('Stock', ['symbol', 'current', 'high', 'low'])

stock = Stock(1, 2, 3, 4)

# インスタンス化する時はHoge()
# インスタンスの識別子？は「Fuga」となる
Hoge = namedtuple('Fuga', ('symbol', 'current', 'high', 'low'))