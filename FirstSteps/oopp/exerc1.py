class cars(object):
    in_stock = 0
    all_cars = 0

    def __init__(self):
        self.on_the_run = False
        self.crash = False
        self.from_Germany = False
        self.from_Russia = False
        self.in_st()

    def print_info(self):
        print(type(self).__name__ + ':')
        print('On the run : ', self.on_the_run)
        print('Crash :', self.crash)
        print('From Germany :', self.from_Germany)
        print('From Russia :', self.from_Russia)
        print()

    def in_st(self):
        if self.on_the_run == True:
            cars.in_stock += 1
            cars.all_cars += 1
        elif self.crash == True:
            cars.all_cars += 1


class bmw(cars):
    def __init__(self):
        super().__init__()
        self.from_Germany = True


class audi(cars):
    def __init__(self):
        super().__init__()
        self.from_Russia = True


class m3(bmw):
    def __init__(self):
        super().__init__()
        self.on_the_run = True
        self.in_st()


class x6(bmw):
    def __init__(self):
        super().__init__()
        self.crash = True
        self.in_st()


class a6(audi):
    def __init__(self):
        super().__init__()
        self.on_the_run = True
        self.in_st()


class q6(audi):
    def __init__(self):
        super().__init__()
        self.crash = True
        self.in_st()


if __name__ == '__main__':
    q6 = q6()
    q6.print_info()
    a6 = a6()
    a6.print_info()
    x6 = x6()
    x6.print_info()
    m3 = m3()
    m3.print_info()
    print(cars.all_cars)
    print(cars.in_stock)
