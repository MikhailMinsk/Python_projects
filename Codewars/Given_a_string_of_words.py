def func(x):
    """
    Given a string of words, you need to find the highest scoring word.
    Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
    You need to return the highest scoring word as a string.
    If two words score the same, return the word that appears earliest in the original string.
    All letters will be lowercase and all inputs will be valid.

    Учитывая строку слов, вам нужно найти слово с наибольшим количеством очков.
     Каждая буква слова набирает очки в соответствии с его положением в алфавите: a = 1, b = 2, c = 3 и т. Д.
     Вам нужно вернуть слово с наибольшим количеством очков в виде строки.
     Если два слова имеют одинаковую оценку, вернуть слово, которое появляется раньше в исходной строке.
     Все буквы будут строчными, и все входные данные будут действительными.
    """

    def count_point(word):
        """
        :return: point every word in string
        """
        count = 0
        for character in word:
            count += (ord(character) - 96)  # number in ascii
        return count

    point = []  # list for point
    list_x = x.split()  # create list

    for word in list_x:
        point.append(count_point(word))

    return str(list_x[point.index(max(point))])  # find the word by index and return him


if __name__ == '__main__':
    some_str = 'what time are we climbing up the volcano'
    func(some_str)
