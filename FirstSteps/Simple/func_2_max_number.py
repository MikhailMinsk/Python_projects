# Написать функцию, которая принимает 3
# аргумента - числа, найти среди них два максимальных,
# вывести в консоль

def funcTwoMax(x, y, z):
    """
    two max  from three numbers
    """
    List = [x, y, z]
    List.sort()
    return List[0], List[1]


if __name__ == '__main__':
    print(funcTwoMax(5, 7, 9))
