# 1.Написать генератор, который возращает случайное значение каждый раз
# 2.Генератор, работающий как range
# 3.Генератор, работающий как map
# 4.Генератор, работающий как enumerate
# 5.Генератор, работающий как zip

import random


def frange1():
    start = 0
    finish = 10
    step = 1
    while start < finish:
        yield start
        start += step


f = frange1()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print()


# 1
def rrange():
    while True:
        yield random.random()  # случайное от 0 до 1


r = rrange()
print(next(r))
print(next(r))
print()


# 2
def frange(start, finish, step=1):
    while start < finish:
        yield start
        start += step


print(list(frange(1, 10, 2)))
print()


# 3
def mrange(lst, func):
    for i in lst:
        yield func(i)


# 5
""" 
s = 'abc'
t = (1, 2, 3)
zip(s,t)
[('a', 1), ('b', 2), ('c', 3)]
"""

print()


def zrange(lst1, lst2):
    for i in range(len(lst1)):
        yield lst1[i], lst2[i]


z = zrange('abc', '123')
for i in zrange('abc', '123'):
    print(i)
