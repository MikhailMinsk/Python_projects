# Написать функцию, которая принимает любое количество аргументов чисел.
# Среди них она находит максимальное и минимальное. И возвращает оба

def max_min(*nubmers):
    """
    чето делает
    """
    return 'max:{!r},min:{!r}'.format(min(nubmers), max(nubmers))


if __name__ == '__main__':
    print(max_min(2, 7, 9, 25, 1, 3))
    help(max_min)
