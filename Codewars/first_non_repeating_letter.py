def func(string):
    """
    Write a function named first_non_repeating_letter that takes a string input,
    and returns the first character that is not repeated anywhere in the string.
    For example, if given the input 'stress', the function should return 't', since the
    letter t only occurs once in the string, and occurs first in the string.
    As an added challenge, upper- and lowercase letters are considered the same character,
    but the function should return the correct case for the initial letter.
    For example, the input 'sTreSS' should return 'T'.
    If a string contains all repeating characters, it should return an empty string ("") or None

    Напишите функцию с именем first_non_repeating_letter, которая принимает ввод строки
    и возвращает первый символ, который не повторяется нигде в строке.
    Например, если задано входное «стресс», функция должна вернуть «t»,
    поскольку буква t встречается только один раз в строке и появляется первой в строке.
    В качестве дополнительной задачи заглавные и строчные буквы считаются одним и тем же символом,
    но функция должна возвращать правильный регистр для начальной буквы. Например,
    вход 'sTreSS' должен возвращать 'T'.
    Если строка содержит все повторяющиеся символы, она должна возвращать пустую строку ("") или None
    """
    res = [i for i in string if string.lower().count(i.lower()) == 1]
    if len(res) == 0:
        return None
    return res[0]


if __name__ == '__main__':
    print(func('stress'))
    print(func('moOnmEn'))
