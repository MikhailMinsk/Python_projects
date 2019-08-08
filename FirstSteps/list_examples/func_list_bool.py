# Написать функцию, которая принимает два аргумента.
# Первый - список чисел, второй - булевый флаг.
# Если флаг действителен - возвращаем новый список с
# нечетными числами из входного списка, если флаг отрицателен -
# возвращаем новый список с четными числами из входного списка
from random import randint


def func_list_bool(list_, bool_):
    """
    Return new list with odd numbers if flag is True.
    Else return new list with even numbers.
    :param List: list numbers
    :param bool: flag
    :return: new list
    """
    if bool_:
        new_list = [i for i in list_ if i % 2 != 0]
        return new_list
    new_list = [i for i in list_ if i % 2 == 0]
    return new_list


if __name__ == '__main__':
    Lst = [randint(1, 50) for i in range(20)]
    print(Lst)
    bool_value = int(input('Input 1 or 0: '))
    print(func_list_bool(Lst, bool_value))
