"""
Дан список целых чисел. Определить количество четных элементов и
количество элементов, оканчивающихся на цифру 5.
"""

from random import randint

L = [randint(1, 50) for i in range(1000)]
print(L)

count2, count5 = 0, 0
for i in range(len(L)):
    if L[i] % 2 == 0:
        count2 += 1
    elif L[i] % 10 == 5:
        count5 += 1
    else:
        continue

print('количество четных элементов списка', count2)
print('количество элементов, оканчивающихся на 5', count5)

"""или 
print(sum(1 for x in L if x % 2 == 0))
print(sum(1 for x in L if x % 10 == 5))
"""
