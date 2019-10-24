class Contact:
    all_contacts = []
    st = 'hogefuga'

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __str__(self):
        # クラス変数には[クラス名.クラス変数]でアクセスできる
        return Contact.st

    def get_st(self):
        # インスタンスメソッドでは[self.クラス変数]でアクセスできる
        return self.st


class Friend(Contact):

    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone