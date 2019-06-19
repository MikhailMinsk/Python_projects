"""
Дан список из 20 элементов. Найти пять соседних элементов, сумма значений которых максимальна.
"""

from random import randint

L = [randint(1, 50) for i in range(20)]
print(L)

max_sum = 0
for i in range(len(L) - 4):
    temp = (L[i] + L[i + 1] + L[i + 2] + L[i + 3] + L[i + 4])
    if max_sum < temp:
        max_sum = temp

print('максимальная сумма в 5ти чисел под ряд в списке = ', max_sum)
