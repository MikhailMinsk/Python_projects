# Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# Также у него должен быть следующий набор методов: know(person), который позволяет
# добавить другого человека в список знакомых. И метод is_known(person),
# который возвращает знакомы ли два человека

# Есть класс, который выводит информацию в консоль: Printer, у него есть метод: log(*values).
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *


class Person:
    dict_known = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def know(self):
        Person.dict_known.append(self.name)

    def is_know(self, some_person):
        if self.name in Person.dict_known and some_person.name in Person.dict_known:
            print('{} and {} are familiar'.format(self.name, some_person.name))
        else:
            print("{} and {} aren't familiar".format(self.name, some_person.name))


# ----------------------------------------------------------------------

class Printer(object):
    def log(self, *values):
        return values


class Formattedprinter():
    def __init__(self, value):
        self.value = value
        self.some_func()

    def some_func(self):
        print('*' * 10)
        print(self.value)
        print('*' * 10)


if __name__ == '__main__':
    a = Printer()
    Formattedprinter(a.log(1, 2, 3, 3, 4))
    # -------------------------------------------------
    print()
    Alex = Person('Alex', 30)
    Anna = Person('Anna', 27)
    Artem = Person('Artem', 29)
    Alex.know()
    Anna.know()
    print(Person.dict_known)
    Alex.is_know(Anna)
    Anna.is_know(Alex)
    Artem.is_know(Anna)
