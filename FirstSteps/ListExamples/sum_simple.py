"""
Дан список, состоящий из чисел.
Найти сумму простых чисел в списке.
"""
from random import randint

L = [randint(0, 100) for i in range(1000)]


def sum_prostix(list1):
    def prostoe(a):
        return all(a % i for i in range(2, a))
    sum = 0
    for i in range(len(list1)):
        if prostoe(list1[i]):
            sum += list1[i]
    return sum


print('Сумма простых чисел в последовательности = ', sum_prostix(L))