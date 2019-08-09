from random import randint
from functools import reduce


def multiplication_numbers(*numbers):
    new_value = 1
    for i in numbers:
        new_value *= i
    print()
    print(new_value)
    return reduce(lambda x, y: x * y, numbers)


if __name__ == '__main__':
    my_numbers = [randint(1, 10) for i in range(10)]
    print(my_numbers)
    print(sum(my_numbers))
    print(multiplication_numbers(1, 2, 3, 4))
