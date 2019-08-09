"""
Найти элемент, наиболее близкий к среднему значению всех элементов списка.
"""


from random import randint

L = [randint(0, 50) for i in range(100)]

for i in range(len(L)):
    k = min(L, key=lambda x: abs(x - sum(L) / 100))
print('среднее значение списка = ', sum(L) / 100)
print('ближайшее значение к среднему = ', k)
print('расположение ближайшего среднего в списке = ', L.index(k))
