## object

```
o = object() <br>
o.x = 5
```

* 全てのクラスはobjectを継承しているため上記のようにobjectに属性を持たせると、余分にメモリを消費してしまうため、objectクラスのインスタンスへの属性追加はエラーとなる。


## namedtuple
* 通常のタプルだと、要素にインデックスでアクセスすることになるためマジックナンバーを避けるためにアクセスしたい要素ごとに定数を作るなど、色々とめんどくさい
* namedtupleだと、要素名にドットでアクセスできて便利
* namedtupleはイテラブルなのでインデックスでもアクセス化
* [namedtupleで美しいpythonを書く！（翻訳）](https://qiita.com/Seny/items/add4d03876f505442136)


## dataclass
* make_dataclass()か@dataclassで定義する
* 普通のクラスを書くより楽にコンテナを作れる(__init__などを書く必要がないため)
* dataclassはイテラブルではない点に注意

## dictionary
* 内部的にはオブジェクトは属性をdictで保持している(__dict__でアクセスできる)

## defaultdict
* Whenever a key is accessed that is not already in the dictionary, it calls that function, with no parameters, to create a default value.
