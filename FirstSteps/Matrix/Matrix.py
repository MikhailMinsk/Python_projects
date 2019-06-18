"""
Создайте матрицу (список из вложенных списков) размера N x M (фиксируются в программе),
заполненную случайными целыми числами.

Вывести номер строки, содержащей максимальное число одинаковых элементов.

Найти произведениеэлементов матрицы, лежащих ниже главной диагонали.

Найти сумму элементов матрицы, лежащих выше главной диагонали.
"""

from random import randint

matrix = [[randint(1, 5) for elem in range(6)] for line in range(8)]
print()
repeats = [max(line.count(elem) for elem in line) for line in matrix]
print('Строка с максимальным количеством одинаковых элементов :', repeats.index(max(repeats)))
print()
for i in matrix:
    print(i)
print()
print()

array = [[randint(1, 10) for elem in range(3)] for line in range(3)]
summa_viwe = 0
proizv_nige = 1
for i in range(len(array)):
    for j in range(len(array[i])):
        if i > j:  # для элементов ниже главной диагонали
            proizv_nige *= array[i][j]
        elif i < j:  # для элементов выше
            summa_viwe += array[i][j]
        else:
            continue
for i in array:
    print(i)
print('сумма выше главной диагонали равна = ', summa_viwe)
print('произведение ниже главной диагонали равна = ', proizv_nige)

"""
for i in range(n):
    a[i][i] = 1 ---- главная диагональ
    
for i in range(n):
    for j in range(i + 1, n):
        a[i][j] = 0  ----- выше диагонали

for i in range(n):
    for j in range(0, i):
        a[i][j] = 2 ---- ниже диагонали

for i in range(N):
    sumMain += matrix[i][i] --- сумма главной диагонали
    sumSecondary += matrix[i][N-i-1] --- сумма обратной диагонали
"""
