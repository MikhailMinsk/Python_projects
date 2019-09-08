def func(password):
    """
    You need to write regex that will validate a password to make sure it meets the following criteria:
    At least six characters long
    contains a lowercase letter
    contains an uppercase letter
    contains a number
    Valid passwords will only be alphanumeric characters.

    Вам нужно написать регулярное выражение, которое проверит пароль,
     чтобы убедиться, что оно соответствует следующим критериям:
    Не менее шести символов
    содержит строчную букву
    содержит заглавную букву
    содержит номер
    Допустимые пароли будут состоять только из буквенно-цифровых символов.
    """
    # ^  # begin word
    # (?=.* [a-z])  # at least one lowercase letter
    # (?=.* [A-Z])  # at least one uppercase letter
    # (?=.* [0-9])  # at least one number
    # [a-zA-Z0-9]  # only alphanumeric
    # {6, }  # at least 6 characters long
    # $  # end word
    import re

    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])([a-zA-Z0-9]{6,})$"
    if re.fullmatch(pattern, password):
        return True
    return False


if __name__ == '__main__':
    print(func('fjd3IR9'))
    print(func('fjd3  IR9'))
    print(func('!fdjn345'))
    print(func('123abcABC'))
