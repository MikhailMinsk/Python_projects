def encode_rail_fence_cipher(string, n):
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
    if n == 1 or n == 0:
        return string
    elif n == 2:
        return string[::2] + string[1::2]
        # return ''.join([i for i in string if not string.index(i) % 2]) + ''.join(
        #     [i for i in string if string.index(i) % 2])
    elif n == 3:
        print(string[::4])
        print(string[1::2])
        print(string[2::4])
    else:
        for i in range(n + 1):
            print(string[i::4])




def decode_rail_fence_cipher(string, n):
    if n == 1 or n == 0:
        return string
    elif n == 2:
        pass


if __name__ == '__main__':
    string = "Hello, World!"
    n = 3
    str_encode = encode_rail_fence_cipher(string, n)
    print(str_encode)
    print(decode_rail_fence_cipher(str_encode, n))
