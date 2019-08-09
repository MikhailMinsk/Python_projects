"""
1. Напишите код, описывающий класс Animal:
 добавьте атрибут имени животного
 добавьте метод eat(), выводящий «Ням-ням»
 добавьте методы getName() и setName()
 добавьте метод makeNoise(), выводящий «Имя животного говорит Гррр»
 добавьте конструктор классу Animal, выводящий «Родилось животное имя животного»
2. Основная программа:
 создайте животное, в момент создания определите его имя
 узнайте имя животного через вызов метода getName()
 измените имя животного через вызов метода setName()
 вызовите eat() и makeNoise() для животного
"""

class Animal:
    name = ''

    def __init__(self, newName):
        self.name = newName

    def eat(self):
        print('Ням-ням')

    def getName(self):
        return self.name

    def set_name(self, newName):
        self.name = newName

    def makeNoise(self):
        print(self.name, ' говорит Грррр')


newAnimal = Animal('Rediska')
print(newAnimal.getName())
newAnimal.set_name('Redisoniwe')
newAnimal.eat()
newAnimal.makeNoise()