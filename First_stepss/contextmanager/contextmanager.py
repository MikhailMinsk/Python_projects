# 1. Дан класс:
# class Lock(object):
#     def __init__(self):
#         self.lock = False
# Сделать менеджер контекста, который может переопределить
# значение lock на True внутри блока контекста.

# 2. Сделать менеджер контекста, который бы проглатывал все исключения вызванные
# в теле и писал их в консоль, пример использования:
# with no_exceptions():
#     1 / 0 # => logs: ZeroDivisionError
# print('Done!') # => continues execution

# +3. Сделать менеджер контекста, который бы мог измерять время выполнения блока кода,
# пример использования:
# with TimeIt() as t:
#     some_long_function()
# print('Execution time was:', t.time)

from contextlib import contextmanager
from time import time, sleep


@contextmanager
def unlocker(some_class):
    some_class.lock = True
    yield some_class
    print('Unlocked!')


@contextmanager
def say_exception():
    try:
        yield
    except Exception as ex:
        print('I found exception: {}'.format(ex))


class TimeMeter():
    def __enter__(self):
        self.started = time()
        return self

    def __exit__(self, *args):
        self.ended = time()
        self.result = self.ended - self.started

class TimeIt():

    def __enter__(self):
        self.started = time()
        return self

    def __exit__(self, *args):
        self.ended = time()
        self.result = self.ended - self.started


@contextmanager
def print_result():
    print('Function start !')
    yield
    print('Function ends')
    print('_' * 30 + '\n')


if __name__ == '__main__':
    with print_result():
        with say_exception():
            x = 1 / 0
        with say_exception():
            y = 'a' / 25


    class Lock(object):
        def __init__(self):
            self.lock = False


    lock = Lock()

    with print_result():
        with unlocker(lock):
            print(lock.lock)

    with print_result():
        with TimeMeter() as timeter:
            sleep(0.5)
        print('Time waiting is:', timeter.result)
