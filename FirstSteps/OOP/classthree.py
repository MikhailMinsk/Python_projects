# пользователь вводит список чисел через пробел, если ввел:
# 1 число - строим квадрат
# 2 числа - строим прямоугольник
# 3 числа - строим трекгольник
# 4 числа - строим многоугольник
# Вычислить периметр и площадь. Вывести в консоль.
# Вывести проверку на возможность построить с такими сторонами.
import math


class Figure:
    def __init__(self, value):
        self.value = value
        self.initialization()

    def initialization(self):
        if len(self.value) == 1:
            a = int(self.value)
            self.square(a)
        elif len(self.value.split()) == 2:
            b = self.value.split()
            self.rectangle(int(b[0]), int(b[1]))
        elif len(self.value.split()) == 3:
            c = self.value.split()
            self.triangle(int(c[0]), int(c[1]), int(c[2]))
        elif len(self.value.split()) == 4:
            d = self.value.split()
            self.quadrilateral(int(d[0]), int(d[1]), int(d[2]), int(d[3]))
        else:
            print('You input many digits')

    def square(self, side):
        print(' _______'
              '\n|       |'
              '\n|       |'
              '\n|_______|')
        print('P = 4a = ', 4 * side)
        print('S = a^2 = ', pow(side, 2))

    def rectangle(self, side_a, side_b):
        p = 2 * side_a + 2 * side_b
        s = side_a * side_b
        print(' _____________'
              '\n|             |'
              '\n|_____________|')
        print('P = 4a = ', p)
        print('S = a^2 = ', s)

    def triangle(self, side_a, side_b, side_c):
        p = 1 / 2 * (side_a + side_b + side_c)
        s = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
        print('|\\'
              '\n| \\'
              '\n|__\\')
        print('P = (a+b+c) = ', p * 2)
        print('S = sqrt(p(p-a)(p-b)(p-c)) = ', round(s, 2))

    def quadrilateral(self, side_a, side_b, side_c, side_d):
        p = 1 / 2 * (side_a + side_b + side_c + side_d)
        s = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c) * (p - side_d))
        print('  ___'
              '\n /   |'
              '\n/____|')
        print('P = (a+b+c+d) = ', p * 2)
        print('S = sqrt(p(p-a)(p-b)(p-c)(p-d) = ', round(s, 2))


if __name__ == '__main__':
    Figure(input('input value or values through the space: '))
    print()
    print()
    print('all:')
    a1 = '1'
    a2 = '1 2'
    a3 = '1 2 3'
    a4 = '1 2 3 4'
    Figure(a1)
    Figure(a2)
    Figure(a3)
    Figure(a4)
