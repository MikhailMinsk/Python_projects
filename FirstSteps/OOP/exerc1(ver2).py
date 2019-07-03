class cars(object):
    in_stock = 0
    all_cars = 0

    def __init__(self):
        self.color = None
        self.crash = ''
        self.from_country = None
        self.volume = None
        self.dimensions = None
        self.car_count()

    def __str__(self):
        return '[%s%s%s%s%s%s%s%s%s%s%s%s]\n' % ('Type: ', type(self).__name__, \
                                                 '\nColor: ', self.color, \
                                                 '\nCrach: ', self.crash, \
                                                 '\nCountry: ', self.from_country, \
                                                 '\nVolume: ', self.volume, \
                                                 '\nDimensions: ', self.dimensions,)

    def car_count(self):
        if self.crash == 'No':
            cars.in_stock += 1
            cars.all_cars += 1
        elif self.crash == 'Yes':
            cars.all_cars += 1


class bmw(cars):
    def __init__(self):
        super().__init__()
        self.from_country = 'Germany'


class audi(cars):
    def __init__(self):
        super().__init__()
        self.from_country = 'Russia'


class m3(bmw):
    def __init__(self):
        super().__init__()
        self.color = 'Blue'
        self.volume = 3.0
        self.dimensions = '2.5x1.5'
        self.crash = 'Yes'
        self.car_count()


class x6(bmw):
    def __init__(self):
        super().__init__()
        self.color = 'Red'
        self.crash = 'No'
        self.volume = 3.5
        self.dimensions = '3.5x1.7'
        self.car_count()


class a6(audi):
    def __init__(self):
        super().__init__()
        self.color = 'Black'
        self.volume = 2.0
        self.dimensions = '3.2x1.7'
        self.crash = 'No'
        self.car_count()


class q6(audi):
    def __init__(self):
        super().__init__()
        self.color = 'Yellow'
        self.volume = 4.0
        self.dimensions = '4.2x1.5'
        self.crash = 'No'
        self.car_count()


if __name__ == '__main__':
    q6 = q6()
    a6 = a6()
    x6 = x6()
    m3 = m3()
    print(q6)
    print(a6)
    print(x6)
    print(m3)
    print('All cars in garage : ', cars.all_cars)
