"""Создайте класс, описывающий автомобиль. Создайте класс автосалона,
содержащий в себе список автомобилей, доступных для продажи,
и функцию продажи заданного автомобиля."""


class auto:
    def __init__(self, name, color, typ=None, motor=None, volume=0):
        self.name = name
        self.color = color
        self.typ = typ
        self.motor = motor
        self.volume = volume

    def __str__(self):
        return '[%s:,%s,%s,%s,%s]' % (self.name, self.color, self.typ, self.motor, self.volume)


class salon:
    def __init__(self, Mazda=0, Honda=0, Ford=0):
        self.Mazda = Mazda
        self.Honda = Honda
        self.Ford = Ford

    def inStock(self):
        return print('Mazda=', self.Mazda, ';Honda=', self.Honda, ';Ford=', self.Ford)

    def sell_auto(self):
        x = input('Input car you like: ')  # добавить проверку ввода по регистру
        if x == 'Mazda':
            if self.Mazda <= 0:
                print('Car out of stock')
            else:
                self.Mazda -= 1
                print('Congratulation, you buy your new car')
                print('Car Mazda in stock', self.Mazda)
        elif x == 'Honda':
            if self.Honda <= 0:
                print('Car out of stock')
            else:
                self.Honda -= 1
                print('Congratulation, you buy your new car')
                print('Car Honda in stock', self.Honda)
        elif x == 'Ford':
            if self.Ford <= 0:
                print('Car out of stock')
            else:
                self.Ford -= 1
                print('Congratulation, you buy your new car')
                print('Car Mazda in stock', self.Ford)
        else:
            print('incorrect input or  we don’t have this cars in stock')


if __name__ == '__main__':
    mazda = auto('mazda', 'black', 'sedan', 'diesel')
    print(mazda)
    honda = auto('honda', 'blue', 'hetchback', 'benz', 2)
    print(honda)
    ford = auto('ford', 'red', 'pickup', 'diesel', 6)
    print(ford)

    In_stock = salon(Mazda=15, Honda=3, Ford=0)
    In_stock.inStock()
    In_stock.sell_auto()
    In_stock.inStock()
