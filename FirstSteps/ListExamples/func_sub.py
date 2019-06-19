"""
Напишите функцию, которая возвращает разность между наибольшим и
 наименьшим значениями из списка целых случайных чисел.
"""

from random import randint

L = [randint(-50, 50) for i in range(1000)]


def raznost(list1):
    return max(list1) - min(list1)


def otricatelnie(list1):
    count = 0
    for i in range(min(list1), max(list1)):
        if list1[i] < 0:
            count += 1
    return count


print('Разность между самым большим числом и минимальным = ', raznost(L))
print('Количество отрицательных чисел между максимальным и минимальным = ', otricatelnie(L))
