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
    """

    def __init__(self, phone="", **kwargs):
        print("Friend's __init__ started")
        print("Friend's super().__init__ started")
        super().__init__(**kwargs)
        print("Friend's super().__init__ finished")
        self.phone = phone
        print("Friend's __init__ finished")


class AudioFile:

    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception('Invalid file format')
        self.filename = filename


class MP3File(AudioFile):

    ext = 'mp3'

    def play(self):
        print(f'{self.ext} is playing')


class WavFile(AudioFile):

    ext = 'wav'

    def play(self):
        print(f'{self.ext} is plyaing')


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
            attrs = set(dir(C))

            # classBの抽象メソッド・プロパティがclassAの要素に含まれる場合はサブクラスと判定する
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented


class Wav(MediaLoader):
    # このクラスは抽象メソッド・プロパティを実装していないため
    # オブジェクトを生成できない
    pass


class Ogg(MediaLoader):
    # 抽象メソッド・プロパティを実装しているのでオブジェクトを生成できる
    ext = 'ext'

    def play(self):
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