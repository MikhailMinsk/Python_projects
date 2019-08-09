"""Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов.
Сделайте так, что при выводе книги на экран при помощи функции print также будут выводиться
отзывы к ней. """


class book_comment:
    def __init__(self, book, comment):
        self.book = book
        self.comment = comment

    def __str__(self):
        return '\"%s\", \n %s \"%s\"' % (self.book, 'Comment fo this book:', self.comment)


book = input('Inter your book:')
comment = input('Inter comment for this book:')

new_book = book_comment(book, comment)
print(new_book)
