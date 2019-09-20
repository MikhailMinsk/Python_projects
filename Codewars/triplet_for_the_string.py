def func(trip):
    """
    There is a secret string which is unknown to you.
    Given a collection of random triplets from the string, recover the original string.
    A triplet here is defined as a sequence of three letters such that each letter occurs
    somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".
    As a simplification, you may assume that no letter occurs more than once in the secret string.
    You can assume nothing about the triplets given to you other than that they are valid triplets
    and that they contain sufficient information to deduce the original string. In particular,
    this means that the secret string will never contain letters that do not occur in one of the
    triplets given to you.

    Есть секретная строка, которая вам неизвестна. Учитывая набор случайных триплетов из строки,
    восстановить исходную строку.
    Триплет здесь определяется как последовательность из трех букв, так что каждая буква встречается
    где-то перед следующей в данной строке. «whi» - триплет для строки «whatisup».
    В качестве упрощения вы можете предположить, что ни одна буква не встречается в секретной строке
    более одного раза.
    Вы ничего не можете предположить о предоставленных вам триплетах, кроме того, что они являются
    допустимыми триплетами и содержат достаточно информации для вывода исходной строки. В частности,
    это означает, что секретная строка никогда не будет содержать букв, которые не встречаются ни в
    одной из предоставленных вам триплетов.
    """
    secret = ''
    new_list = []
    [[new_list.append(elem) for elem in line] for line in trip]
    new_list = list(set(new_list))
    print(new_list)
    for char in new_list:
        for line in trip:
            if char in line:
                if line.index(char) == 3:
                    pass

    return secret


def recoverSecret(triplets):
    new_list = list(set([elem for line in triplets for elem in line]))
    while True:
        j = 0
        for line in triplets:
            a = new_list.index(line[0])
            b = new_list.index(line[1])
            c = new_list.index(line[2])
            if a > b or b > c:
                j += 1
                a, b, c = sorted([a, b, c])
                new_list[a], new_list[b], new_list[c] = line[0], line[1], line[2]
        if j == 0:
            return ''.join(new_list)


if __name__ == '__main__':
    triplets = [
        ['t', 'u', 'p'],
        ['w', 'h', 'i'],
        ['t', 's', 'u'],
        ['a', 't', 's'],
        ['h', 'a', 'p'],
        ['t', 'i', 's'],
        ['w', 'h', 's']
    ]
    print(func(triplets))
    print(recoverSecret(triplets))
