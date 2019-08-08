def decor(func):
    def wrap():
        print('=======')
        func()
        print('=======')

    return wrap()


# def print_text():
#     print('Some text')
#
#
# print(decor(print_text))
# print_text = decor(print_text)
# print(print_text)


# fucking None

@decor
def print_t():
    print('Yxxx!')


print()


# ---------------------------------------

def decor2(some_func):
    def inn(x, y):
        result = some_func(x, y)
        print('result is:', result)
        return result

    return inn


def sum(x, y):
    return x + y


def mult(x, y):
    return x * y


s = decor2(sum)
s_result = s(10, 11)
print(s_result)
print()


# ------------------------------------------
def some_decorator(func):
    def inner(text):
        print('Some is going to', func.__name__)
        func(text)

    return inner


@some_decorator
def shout(text):
    print(text.upper(), '!!!')


@some_decorator
def whisper(text):
    print(text.lower(), "...")


@some_decorator
def say(something):
    something += ',- was said.'
    print(something)


say('hi')
whisper('hello')
shout('i am here')


# ----------------------------------------------------

# запускать в консоли
def some_decorator(func):
    def inner(text):
        print('Some is going to', func.__name__)
        func(text)

    return inner


some_decorator(str)("some!")  # двойной вызов возможен, тк декоратор возвращает функцию
# в которую мы передаем параметр , есть пример бесконечной функции
