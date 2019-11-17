import hashlib


class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


class PermissionError(Exception):
    pass


class NotLoggedInError(AuthException):
    pass


class NotPermittedError(AuthException):
    pass


class User(object):

    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        """
        パスワードのハッシュを行う
        """

        hash_string = self.username + password
        hash_string = hash_string.encode('utf8')

        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """
        入力されたパスワードが正しいかチェックする
        """

        encrypted = self._encrypt_pw(password)

        return encrypted == self.password


class Authenticator(object):
    """
    ユーザ追加・認証を行う
    """
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        """
        ユーザの追加を行う
        """

        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)

        self.users[username] = User(username, password)

    def login(self, username, password):
        """
        ユーザのログインを実行する
        """

        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False


class Authorizor(object):
    """
    ユーザへの認可を行う
    """
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        """
        権限の種類を追加する
        """

        try:
            # perm_nameが既に存在するかチェック
            self.permissions[perm_name]
        except KeyError:
            # perm_nameが無ければ作成する
            self.permissions[perm_name] = set()
        else:
            raise PermissionError('Permission exists')

    def permit_user(self, perm_name, username):
        """
        ユーザに権限を追加する
        """

        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError('Permission does not exists')
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        """
        ユーザが権限を持っているかチェックする
        """

        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)

        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError('Permission does not exist')
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True


authenticator = Authenticator()

authorizor = Authorizor(authenticator)
