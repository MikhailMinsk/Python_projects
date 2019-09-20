"""
Create two functions to encode and then decode a string using the Rail Fence Cipher.
This cipher is used to encode a string by placing each character successively in a diagonal
along a set of "rails". First start off moving diagonally and down. When you reach the bottom,
reverse direction and move diagonally and up until you reach the top rail.
Continue until you reach the end of the string. Each "rail" is then read left to right
to derive the encoded string. You can optionally include or dis-include punctuation.

Создайте две функции для кодирования, а затем декодируйте строку с использованием Rail Fence Cipher.
Этот шифр используется для кодирования строки путем последовательного размещения каждого символа
по диагонали вдоль набора «рельсов». Сначала начните движение по диагонали и вниз. Когда вы достигнете
дна, поменяйте направление и двигайтесь по диагонали вверх, пока не дойдете до верхней направляющей.
Продолжайте, пока не дойдете до конца строки. Каждый «рельс» затем читается слева направо,
чтобы получить закодированную строку. Вы можете по желанию включить или отключить пунктуацию.
"""


def change_char(string, n):
    from itertools import chain
    count1 = 0
    count2 = 1
    new_list = [[] for i in range(n)]
    for char in string:
        new_list[count1].append(char)
        if (count1 == n - 1 and count2 > 0) or (count1 == 0 and count2 < 0):
            count2 *= -1
        count1 += count2

    return chain.from_iterable(new_list)


def encode_rail_fence_cipher(string, n):
    return ''.join(change_char(string, n))


def decode_rail_fence_cipher(string, n):
    new_list = [''] * len(string)
    for c, i in zip(string, change_char(range(len(string)), n)):
        new_list[i] = c
    return ''.join(new_list)


if __name__ == '__main__':
    string = "Hello, World!"
    n = 4
    str_encode = encode_rail_fence_cipher(string, n)
    print(str_encode)
    print(decode_rail_fence_cipher(str_encode, n))
    save = [[] for _ in range(n)]
    print(save)
