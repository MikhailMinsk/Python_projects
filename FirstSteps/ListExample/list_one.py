List_ = [3, 'hello', 7, 4, 'привет', 4, 3, -1]

if 'привет' in List_:
    print('привет' * 10)
print('_________________________________________')

H = List_
print(H is List_)  # проверка на идентичность списков, т.е. один и тот же это список или нет
# если поменять H , то поменяется и L, и наоборот,т.к. они указывают на один и тот же список
print(H)
print(List_)
print('_________________________________________')

# для создания нового объекта используется глубокое копирование :
import copy

H = copy.deepcopy(List_)
H[2] = -100
H[0] = -100
print(H)
print(List_)
print('_________________________________________')

List_ = [2, 'hello', 6, 5, 'привет', 4, 3, -1]
print(List_[:3])
print(List_[:])
print(List_[::2])
print(List_[::-1])  # список с конца
print(List_[:-1])
print(List_[-1:])