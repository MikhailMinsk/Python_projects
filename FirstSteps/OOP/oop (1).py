"""
Создайте класс Cat. Определите атрибуты name (имя), color (цвет) и weight (вес).
Добавьте метод под названием meow («мяуканье»). Создайте объект класса Сat,
установите атрибуты, вызовите метод meow.
"""
class cat():
    name = ''
    color = ''
    weight = 0

    def meow(self):
        print('Мяяяяяяуууу!!!')


mycat = cat()
mycat.name = 'Дымок'
mycat.color = 'black'
mycat.weight = 11
mycat.meow()

"""----------------------------------------"""


class MyObject:
    int_val = 8
    str_val = 'a string'


print(MyObject.int_val)
print(MyObject.str_val)

object1 = MyObject()
object2 = MyObject()

print('\n', object1.int_val)
print(object2.str_val)

MyObject.int_val = 10
print('\n', MyObject.int_val)
print(object1.int_val)

object1.str_val = 'another string'
print('\n', MyObject.str_val)
print(object1.str_val)
