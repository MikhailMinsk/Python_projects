# Написать функцию, которая принимает любое количество позиционных
# аргументов - строк и один парматер по-умолчанию glue, который
# равен ':'. Соединить все строки таким образом, чтобы в результат попали
# все строки, длинее 3 символов. Для соединения между любых двух строк вставлять glue


def some_func(*some_strings, glue=':'):
    """
    some kind of documentation
    """
    # new_list = [i for i in some_strings if len(i) > 3]
    new_str = ''
    for i in some_strings:
        if len(i) > 3:
            if new_str == '':
                new_str += i
            else:
                new_str += glue + i
    return print(new_str)


if __name__ == '__main__':
    some_func('qeqweq', 'qweq', 'qw')
    print(1, 2, 3, sep=':')
