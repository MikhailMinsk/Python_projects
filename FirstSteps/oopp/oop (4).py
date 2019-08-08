"""
1. Напишите код, описывающий класс Animal:
a) Добавьте атрибут имени животного.
b) Добавьте метод eat(), выводящий «Ням-ням».
c) Добавьте методы getName() и setName().
d) Добавьте метод makeNoise(), выводящий «Имя животного говорит Гррр».
e) Добавьте конструктор класса Animal, выводящий «Родилось животное».
2. Пусть Animal будет родительским для класса Cat. Метод makeNoise() класса Cat
выводит «Имя животного говорит Мяу». Конструктор класса Cat выводит «Родился кот»,
а также вызывает родительский конструктор.
3. Пусть Animal будет родительским для класса Dog. Метод makeNoise() для Dog выводит
«Имя животного говорит Гав». Конструктор Dog выводит «Родилась собака», а также вызывает
родительский конструктор.
4. Основная программа. Код, создающий кота, двух собак и одно простое животное.
Дайте имя каждому животному (через вызов методов). Код, вызывающий eat() и makeNoise()
для каждого животного.
"""

class Animal():
    name = ''

    def __init__(self):
        print('Создано животное')

    def eat(self):
        print('Ням-ням')

    def getName(self):
        return self.name

    def setName(self, rename):
        self.name = rename

    def makeNoise(self):
        print(self.name, 'говорит \'Гррр\'')


class Cat(Animal):
    catname = ''

    def __init__(self):
        Animal.__init__(self)
        print("Родилось котэ !")

    def makeNoise(self):
        print(self.getName(), 'говорит \'Мяууу\'')


class Dog(Animal):
    dogname = ''

    def __init__(self):
        Animal.__init__(self)
        print('Родился собакин !')

    def makeNoise(self):
        print(self.getName(), 'говорит \'Гаууу\'')


cat1 = Cat()
cat1.name = 'Kowmarik'
cat1.getName()
cat1.eat()
cat1.makeNoise()
dog1 = Dog()
dog1.name = 'Ares'
dog1.makeNoise()
dog1.eat()
dog2 = Dog()
dog2.name = 'Germes'
dog2.makeNoise()
dog2.eat()

