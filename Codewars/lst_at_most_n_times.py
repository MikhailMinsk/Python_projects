def func(lst, max_e):
    """
    Given a list lst and a number N, create a new list that contains
    each number of lst at most N times without reordering.
    For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
    drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3,
    which leads to [1,2,3,1,2,3].

    Учитывая список lst и число N, создайте новый список, который содержит каждое число lst
    не более N раз без переупорядочения. Например, если N = 2, а ввод [1,2,3,1,2,1,2,3],
    вы берете [1,2,3,1,2], отбрасываете следующее [1,2 ], так как это приведет к тому,
    что 1 и 2 будут в результате 3 раза, а затем - 3, что приводит к [1,2,3,1,2,3].
    """
    new_lst = []
    for i in lst:
        if new_lst.count(i) < max_e and new_lst.count(i) < lst.count(i):
            for j in lst:
                if new_lst.count(j) < max_e:
                    new_lst.append(j)
    return new_lst


if __name__ == '__main__':
    print(func([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3))
