class EvenOnly(list):

    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError('Only Integer can be added')
        if integer % 2:
            raise ValueError('Only Even Number can be added')
        super().append(integer)


def no_return():
    print("I'm about to raise Exception")
    raise Exception("This is always raised")
    print('This line will never execute')


def call_exceptor():
    print('call no_return() now')
    try:
        no_return()

        # 以下は実行されない
        print('an Exception was raised...')
    except Exception:
        print('I caught an Exception')
    else:
        print('No Exception raised')
    print('executed after caught an Exception')


def funny_division3(divider):

    try:
        if divider == 13:
            raise ValueError('13 is an unlucky number')
        return 100 / divider
    except ZeroDivisionError:
        return 'Enter a number other than zero'
    except TypeError:
        return 'Enter a integer'
    except ValueError:
        print('Please dont enter 13!')
        raise
    finally:  # except句のreturnより前に実行される
        print('always executed in the last')


class MyException(Exception):
    pass


def sample():
    try:
        raise MyException('hoge', 'fuga', 100)
    except Exception as e:
        print(e.args)
