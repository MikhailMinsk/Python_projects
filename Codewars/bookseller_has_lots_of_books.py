def func(listOfArt, listOfCat):
    """
    A bookseller has lots of books classified in 26 categories labeled A, B, ... Z.
    Each book has a code c of 3, 4, 5 or more capitals letters. The 1st letter of a code
    is the capital letter of the book category. In the bookseller's stocklist each code c
    is followed by a space and by a positive integer n (int n >= 0) which indicates the
    quantity of books of this code in stock.
    your task is to find all the books of L with codes belonging to each category of M and
    to sum their quantity according to each category.

    У продавца книг есть много книг, классифицированных в 26 категориях, помеченных A, B, ... Z.
    Каждая книга имеет код c из 3, 4, 5 или более заглавных букв. 1-я буква кода - это заглавная буква
    категории книги. В перечне акций продавца книг за каждым кодом c следует пробел и положительное
    целое число n (int n> = 0), которое указывает количество книг с этим кодом на складе.
    ваша задача - найти все книги L с кодами, относящимися к каждой категории M,
    и суммировать их количество по каждой категории.
    """
    new_dict = {}
    new_str = []
    for cat in listOfCat:
        for book in listOfArt:
            if book.startswith(cat):
                if new_dict.get(cat) is None:
                    new_dict.update({cat: int(book.split()[1])})
                else:
                    new_dict.update({cat: new_dict.get(cat) + int(book.split()[1])})
    for cat in listOfCat:
        new_str.append('({} : {})'.format(cat, new_dict.get(cat, 0)))
    if sum(new_dict.values()) == 0:
        return ''
    return ' - '.join(new_str)

    # categories = [(char, book.split()[1]) if book.startswith(char) else (char, 0) for char in listOfCat for book in listOfArt ]
    # grouped = itertools.groupby(categories_quantity, lambda a: a[0])
    # sum_cat = [(i[0], sum(int(a[1]) for a in i[1])) for i in grouped]
    # return ' - '.join((f'({char[0]} : {str(char[1])})') for char in sum_cat)

    # a = [sum([int(i.split(' ')[1]) if i[0] == j else 0 for i in b]) for j in c]
    # if not len(list(filter(lambda x: x, a))): return ''
    # return ' - '.join(['(' + c[i] + ' : ' + str(a[i]) + ')' for i in range(len(a))])


if __name__ == '__main__':
    print(func(["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B"]))
