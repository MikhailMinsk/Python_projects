def func(*letters):
    """
    Your task is to add up letters to one letter.
    The function will be given a variable amount of arguments, each one being a letter to add.

    Ваша задача - сложить буквы в одну букву.
    Функция получит переменное количество аргументов, каждый из которых будет буквой для добавления.
    """

    count = 0
    for letter in letters:
        count += (ord(letter) - 96)
    if count > 26:
        count = count % 26
        if count == 0:
            return 'z'  # wtf ) Its codewar ...
        return str(chr(count + 96))
    elif count == 0:
        return 'z'
    return str(chr(count + 96))


if __name__ == '__main__':
    func('a', 'b', 'c')
    func('z', 'b', 'c')
    func('z', 'a')
    func("f", "k", "h", "g", "x")
    func()
