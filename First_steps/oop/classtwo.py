# Создать класс корзина, у которого можно выставить разную вместимость для разных объектов.
# В объект класса корзина можно помещать разные объекты.
# Создать класс пакет, в который так же можно помещать предметы, у него тоже есть вместимость.
# создать любой класс, объекты которого омжно помещать и в корзину и в пакет.
# Если вместимости недостаточно, сказать, что объект поместить нельзя.

class Basket:
    def __init__(self, value):
        self.value = value
        self.put_in_basket()

    def put_in_basket(self):
        print('The subject is already in basket. Weight: ', self.value)


class Package:
    def __init__(self, value):
        self.value = value
        self.put_in_package()

    def put_in_package(self):
        print('The subject is already in package. Weight:', self.value)


class Some_capacity:
    def __init__(self, value):
        self.value = value
        self.weight()

    def weight(self):
        value = self.value
        if value < 6:
            print('Put in packege')
            Basket(value)
        elif value in range(6, 15):
            print('Put in basket')
            Package(value)
        else:
            print('The subject has very big weight')


if __name__ == '__main__':
    Some_capacity(int(input('Please, input weight: ')))
