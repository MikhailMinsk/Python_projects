"""создать функцию, которая в массиве находит сумму двух чисел, равную данному и возвращает тру или фолс"""
from random import randint


def func(number, mas):
    """The function that in the array finds the sum of two numbers
    equal to the given one and returns a true or a false"""

    count = 0
    for i in range(len(mas)):
        for j in range(len(mas)):
            if mas[i] + mas[j] == number:
                count += 1
    if count > 0:
        return True
    else:
        return False


def main():
    mas1 = [randint(-15, 50) for i in range(100)]
    input_number = int(input('Enter a number : '))
    print(mas1)
    print(func(input_number, mas1))


if __name__ == '__main__':
    main()
