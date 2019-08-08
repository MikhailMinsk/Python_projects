"""Создайте класс, описывающий книгу. Он должен содержать информацию об
авторе, названии, годе издания и жанре. Создайте несколько разных книг.
Определите для него операции проверки на равенство и неравенство,
 методы __repr__ и __str__"""


class book_info:
    def __init__(self, author, name_book, genre, year_publishing=None):
        self.author = author
        self.name_book = name_book
        self.year_publishing = year_publishing
        self.genre = genre

    def __str__(self):
        return '[%s: \"%s\" , %s, %s]' % (self.author, self.name_book, self.genre, self.year_publishing)

    def __repr__(self):
        return 'Book_info(%.1f,%1f,%1f,%1f' % (self.author, self.name_book, self.genre, self.year_publishing)

    def __eq__(self, other):
        if self.author == other.author:
            print('This books have one author ')
        elif self.name_book == other.name_book:
            print('This books have one name')
        elif self.year_publishing == other.year_publishing:
            print('This books issued in one year')
        elif self.genre == other.genre:
            print('This books have one genre')
        else:
            print('This book have nothing in common')

    def __ne__(self, other):
        if self.author != other.author and \
           self.name_book != other.name_book and \
           self.year_publishing != other.year_publishing and \
           self.genre != other.genre:
            print('This books have nothing common')
        else:
            print('This books have something common')


book1 = book_info('Seleznev', 'Propaganda and violence', 'public', 1980)
book2 = book_info('Strelkow', 'New earth in fire', 'sci', 2015)
book3 = book_info('Perymov', 'Not time for a dragon', 'sci')

print(book1)
print(book2)
print(book3)


def not_equal(first_book, second_book):
    return first_book != second_book


def equal(first_book, second_book):
    return first_book == second_book


equal(book3, book2)
not_equal(book3, book2)
