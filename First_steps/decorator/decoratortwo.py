# + Написать декоратор, который отменяет выполнение любой декорированной функций и
# будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!
# + Реализовать декоратор, который измеряет скорость выполнения функций.
# + Реализовать декоратор, который будет считать, сколько раз выполнялась функция
# + Реализовать декоторатор, который будет логгировать процесс выполнения функции:
# создан декоратор, начато выполнение функции, закончено выполнение функции
# + Реализовать декоратор, который будет перехватывать все исключения в функции.
# Если они случились, нужно просто писать в консоль сообщение об ошибке

from time import time
from functools import wraps

# @wraps(f) используется для сохранения контекста декорируемой функции в декораторе __doc__ и остальное

# def func_count(func):
#     def func_count():

count_of_func = {}


def time_count(func):
    @wraps(func)
    def time_wrap(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        return print('Run time is : ', round(time() - start, 5))

    return time_wrap


def func_canceled(func):
    @wraps(func)
    def canceled_wrap():
        print(func.__name__, 'is CANCELED')
        print()

    return canceled_wrap


def logger_func(func):
    print('decorator is create')

    @wraps(func)
    def logger_wrap(*args, **kwargs):
        print('Func {} is start'.format(func.__name__))
        func(*args, **kwargs)
        print('func {} is finish'.format(func.__name__))

    return logger_wrap


def count_func(func):
    @wraps(func)
    def count_wrap(*args,**kwargs):
        if func.__name__ in count_of_func.keys():
            value = int(count_of_func.get(func.__name__)) + 1
            count_of_func.update({func.__name__: value})
        else:
            count_of_func.update({func.__name__: 1})

    return count_wrap


def exception_func(func):
    @wraps(func)
    def exception_wrap(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as er:
            print('Found error : ', repr(er))

    return exception_wrap


@func_canceled
def some_func():
    print('some print')


@time_count
@logger_func
def some_func2():
    s = [i for i in range(1, 10000) if i % 2 != 0]
    s = list(map(lambda x: x * 2, s))
    print('This func something doing', s)

@count_func
def some_func3():
    print('tratata')

if __name__ == '__main__':
    some_func()
    some_func2()
    some_func3()
    print(count_of_func)