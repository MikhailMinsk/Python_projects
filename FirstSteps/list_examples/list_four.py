"""L = [-8, 8, 6.0, 5, 'строка', -3.1]
Определить сумму чисел, входящих в список L"""


List = [-8, 8, 6.0, 5, 'строка', -3.1]
sum_ = 0
for i in List:
    if type(i) in [float, int]:
        sum_ = sum_ + i
print(sum_)

