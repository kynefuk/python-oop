import abc


class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1


class LeftSubClass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Left Subclass")
        self.num_left_calls += 1


class RightSubClass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Rigt Subclass")
        self.num_right_calls += 1


class SubClass(LeftSubClass, RightSubClass):
    num_sub_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        self.num_sub_calls += 1


"""
SubClassのcall_me()を実行すると以下の処理が行われる
1. LeftSubClassのcall_me()のsuper().call_me()でRightSubClassのcall_me()が実行
2. RightSubClassのcall_me()のsuper().call_me()でBaseClassのcall_me()が実行
3. RightSubClassのcall_me()の後続処理
4. LeftSubClassのcall_me()の後続処理
5. SubClassのcall_me()の後続処理
"""

#########################


class Contact:
    all_contacts = []

    def __init__(self, name="", email="", **kwargs):
        print("Contact's __init__ started")
        print("Contact's super().__init__ started")
        super().__init__(**kwargs)
        print("Contact's super().__init__ finished")
        self.name = name
        self.email = email
        self.all_contacts.append(self)
        print("Contact's __init__ finished")


class AddressHolder:
    def __init__(self, street="", city="", state="", code="", **kwargs):
        print("AddressHolder's __init__ started")
        print("AddressHolder's super().__init__ started")
        super().__init__(**kwargs)
        print("AddressHolder's super().__init__ finished")
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        print("AddressHolder's __init__ finished")


class Friend(Contact, AddressHolder):

    """
    Friendをインスタンス化すると、
    Friendのinitのsuper().initでContactのinitが呼び出され
    Contactのinitのsuper().initでAddressHolderのinitが呼び出される。
    **kwargsで展開して親クラスのinitに渡してあげている
    """

    def __init__(self, phone="", **kwargs):
        print("Friend's __init__ started")
        print("Friend's super().__init__ started")
        super().__init__(**kwargs)
        print("Friend's super().__init__ finished")
        self.phone = phone
        print("Friend's __init__ finished")


"""
多重継承する際にパラメータが異なる親クラスのinitを実行できるように
各クラスのinitのパラメータはキーワード引数とし、**argsを展開して
渡すことで引数をうまく処理できるようにする
"""

#####################################


class MediaLoader(metaclass=abc.ABCMeta):

    # 抽象メソッド
    @abc.abstractmethod
    def play(self):
        pass

    # 抽象プロパティ
    @abc.abstractproperty
    def ext(self):
        pass

    # MediaLoaderクラスを継承していなくても
    # play()とextを持っていれば、MediaLoaderクラスのサブクラスとして認識する
    # issubclass(classA, classB)で、ClassB側の__subclasshook__が呼び出される
    @classmethod
    def __subclasshook__(cls, C):
        # classBのclsがMediaLoaderであること
        if cls is MediaLoader:
            # classAの全要素(メソッド・プロパティ)を取得
            # dir()で引数のオブジェクトの有効な属性のリストを取得する
            attrs = set(dir(C))

            # classBの抽象メソッド・プロパティがclassAの要素に含まれる場合はサブクラスと判定する
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented


class MP3(MediaLoader):
    # 抽象メソッド・プロパティを実装しているのでオブジェクトを生成できる
    ext = 'ext'

    def play(self):
        pass


class Wav(MediaLoader):
    # このクラスは抽象メソッド・プロパティを実装していないため
    # オブジェクトを生成できない
    pass


class Hoge():
    # MediaLoaderクラスを継承していないが
    # play()とextを持っているため、MediaLoaderのサブクラスと認識できる
    ext = 'hoge'

    def play(self):
        pass


class Hage():
    # extを持っていないためMediaLoaderのサブクラスと認識されない
    def play(self):
        pass


class Fuga():
    # play()を持っていないためMediaLoaderのサブクラスと認識されない
    ext = 'fuga'


class MyBaseClass:
    def __init__(self, value):
        self.value = value


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2


class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        # この書き方だと、PlusTwo.__init__でBaseClassのvalueがリセットされる
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)


class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 2


class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super().__init__(value)
