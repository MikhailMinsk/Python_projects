"""
Задан список из целых чисел. Определить процентно
"""

from random import randint

L = [randint(1, 50) for i in range(1000)]
print(L)

count = 0
for i in range(len(L)):
    if L[i] > sum(L) / len(L):
        count += 1

print('процент чисел больших среднеарифметическиго в списке = ', count / (len(L) / 100), '%')
