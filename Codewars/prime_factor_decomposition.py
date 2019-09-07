def func(n):
    """
    Given a positive number n > 1 find the prime factor decomposition of n.
    The result will be a string with the following form :

    По положительному числу n> 1 найти разложение простого множителя n.
    Результатом будет строка со следующей формой:
     "(p1**n1)(p2**n2)...(pk**nk)"
    """
    res = []
    out = []
    m = 2
    while m * m <= n:
        if n % m == 0:
            res.append(m)
            n //= m
        else:
            m += 1
    if n > 1:
        res.append(n)
    for num in res:
        if res.count(num) == 1:
            out.append('(' + str(num) + ')')
        else:
            out.append('(' + str(num) + '**' + str(res.count(num)) + ')')
    out = list(dict.fromkeys(out))
    return ''.join(out)


if __name__ == '__main__':
    print(func(7775460))
