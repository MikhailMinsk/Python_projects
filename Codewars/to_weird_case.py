def func(string):
    """
    Write a function toWeirdCase (weirdcase in Ruby) that accepts a string,
    and returns the same string with all even indexed characters in each word upper cased,
    and all odd indexed characters in each word lower cased.
    The indexing just explained is zero based, so the zero-ith index is even,
    therefore that character should be upper cased.
    The passed in string will only consist of alphabetical characters and spaces(' ').
    Spaces will only be present if there are multiple words.
    Words will be separated by a single space(' ').

    Напишите функцию toWeirdCase (странный случай в Ruby), которая принимает строку и
    возвращает ту же строку со всеми четными индексированными символами в каждом слове
    в верхнем регистре и всеми нечетными индексированными символами в каждом слове в нижнем регистре.
    Только что объясненное индексирование основано на нуле, поэтому индекс с нулевым i-м является четным,
    поэтому этот символ должен быть в верхнем регистре.
    Переданная строка будет состоять только из буквенных символов и пробелов ('').
    Пробелы будут присутствовать только при наличии нескольких слов.
    Слова будут разделены одним пробелом ('').
    :param string:
    :return:
    """
    
    new_string = []
    for word in string.split():
        new_word = []
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i]
        new_string.append(''.join(new_word))
    return ' '.join(new_string)


if __name__ == '__main__':
    string = 'should return the correct value for multiple words'
    print(func(string))
