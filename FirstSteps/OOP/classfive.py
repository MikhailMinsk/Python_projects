# Написать класс Animal и Human,сделать так, чтобы некоторые
# животные были опасны для человека (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)

class Fauna(object):
        pass


class Human(Fauna):
    def is_dangerous(self):
        print('Some times is dangerous')


class Animal(Fauna):
    def is_dangerous(self):
        print('some are dangerous')


class Homeanimal(Animal):
    def is_dangerous(self):
        print('Not dangerous')


class Predator(Animal):
    def is_dangerous(self):
        print('Dangerous')


if __name__ == '__main__':
    lion = Predator()
    lion.is_dangerous()
    anotherhuman = Human()
    anotherhuman.is_dangerous()
