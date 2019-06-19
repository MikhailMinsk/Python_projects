"""
Задан список из целых чисел. Определить количество участков списка,
на котором элементы монотонно возрастают (каждое следующее число больше предыдущего).
"""

from random import randint
from itertools import groupby

L = [randint(1, 50) for i in range(100)]
s = ''
for i in range(len(L)):
    if L[i - 1] < L[i]:
        s += '+'
    else:
        s += '-'
g = groupby(s)
"""группирует элементы по значению.
 Значение получается применением функции key к элементу
  (если аргумент key не указан, то значением является сам элемент)."""
out = [k for k, v in g if k == '+']
print('result:', len(out))

"""import random
lst = [random.randint(0, 20) for el in range(40)]
print(lst)
result=0
count=0
for j in range(len(lst)-2):
    if lst[j+2] > lst[j+1] > lst[j]:
        count+=1
    elif count>=1 and lst[j+1] > lst[j+2]:
        result+=1
        count=0
if lst[-1] > lst[-2] > lst[-3]:
    result+=1
print(result)"""
