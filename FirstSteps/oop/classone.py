class Terminal:
    def hello(self, user_name):
        print('self is the object itself', self)
        print('Hi', user_name)


class Window:
    is_opened = False

    def open(self):
        self.is_opened = not self.is_opened  # меняет состояние на противоположное
        print('window is now', self.is_opened)


class Table:
    def __init__(self, number_of_legs):
        # self.nuber_of_legs=number_of_legs
        print('New table has {} legs'.format(number_of_legs))


class Chair:
    def __init__(self, color):
        self.color = color  # поле которое помогает сохранять значения


def main():
    t = Terminal()
    t.hello('Mike')
    t.hello('Lucy')

    print()
    w = Window()
    w1 = Window()
    print('Initial state', w.is_opened, w1.is_opened)
    w.open()
    print('new state', w.is_opened, w1.is_opened)

    t = Table(4)
    t1 = Table(3)  # Переменные уничтожатся, т.к. они нигде не хранятся

    c = Chair('green')
    print(c, c.color)
    c1 = Chair('Red')


if __name__ == '__main__':
    main()
