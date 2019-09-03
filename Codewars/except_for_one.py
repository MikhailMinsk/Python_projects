def func(arr):
    """
    There is an array with some numbers. All numbers are equal except for one. Try to find it!

    Есть массив с некоторыми числами. Все числа равны, кроме одного. Попробуйте найти это!
    """

    if arr.count(min(arr)) == 1:
        n = min(arr)
        return n
    n = max(arr)
    return n


if __name__ == '__main__':
    print(func([1, 1, 1, 2, 1, 1]))
    print(func([0, 0, 0.55, 0, 0]))
