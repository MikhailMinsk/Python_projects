# + При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]
# + При помощи map превратить все числа из массива [3, 4, 90, -2] в строки
# + При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки
# + При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value']
from functools import reduce

res = list(map(lambda x: x % 5, [1, 4, 5, 30, 88]))
print(res)
res = list(map(lambda x: str(x), [3, 4, 90, -2]))
print(res)
res = list(filter(lambda x: not isinstance(x, str), ['some', 1, 'v', 40, '3a', str]))
print(res)
res = reduce(lambda x, y: x + y, list(len(x) for x in ['some', 'other', 'value']))
print(res)