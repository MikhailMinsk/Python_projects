def func(string):
    """
    In this kata you have to create all permutations of an input string
    and remove duplicates, if present. This means, you have to shuffle
    all letters from the input in all possible orders.

    В этом ката вы должны создать все перестановки входной строки и
    удалить дубликаты, если они есть. Это означает, что вы должны
    перетасовать все буквы из ввода во всех возможных порядках.
    """
    from itertools import permutations
    new_list = [''.join(i) for i in permutations(string)]
    return list(set(new_list))


if __name__ == '__main__':
    print(func('aabb'))
    print(func('cdefg'))
    print(func('abc'))
