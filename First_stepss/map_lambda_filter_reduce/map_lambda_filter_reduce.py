from math import *


def work(value):
    return value * 2


print((lambda x: pow(1 / tan(x * pi / 3), 2) - sqrt(fabs(x)) - pow(3.4, pow(x, 2) - 10) + log(pow(x, 2) + 3))(
    float(input('input x: '))))
print("____________________________________________________")
t = [1, 2, 5, 10]
m = (map(work, t))
print(m)
print(list(m))
print(list(map(work, t)))
print("____________________________________________________")

m1 = map(lambda x: x * 2, t)
print(m1)
print(list(m1))
print(list(map(lambda x: x * 2, t)))
print("____________________________________________________")

print(list(filter(lambda v: v > 0, [-1, -5, -9, 20, 3, 0])))
print("____________________________________________________")

s = [1, 2, 3, 4, 1, 2, 3, 7]
print(list(set(s)))
print(list(filter(lambda x: x != 2, s)))
print("____________________________________________________")

from functools import reduce

r = [1, 5, 7, 9]
result = reduce(lambda x, y: x + y, r)
result1 = reduce(lambda x, y: x * y, r)
print(result, result1)
print("____________________________________________________")


def my_func(f, arg):
    return f(arg)


print(my_func(lambda x: 7 * x * x, 10))
print("____________________________________________________")

print((lambda x: x ** 2 + 7 * x + 4)(-4))
print("____________________________________________________")

print(list(filter(lambda x: x % 2 != 0, r)))
