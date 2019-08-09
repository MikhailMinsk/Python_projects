"""
Создайте класс StringVar для работы со строковым типом данных,
содержащий методы set() и get(). Метод set() служит для изменения
 содержимого строки, get() – для получения содержимого строки.
 Создайте объект типа StringVar и протестируйте его методы
"""

class StringVar:
    strng = ''

    def __init__(self, strng):
        self.strng = strng

    def setString(self, newstring):
        self.strng = newstring
        print(self.strng.swapcase())

    def getString(self):
        print(self.strng)


mystr = StringVar('а я пишу всякую херь')
mystr.getString()
mystr.setString('а тут еще что то допишу')
mystr.getString()
StringVar.strng = 'а вот опять что то нашло на меня писать'
print(StringVar.strng)


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def func1(self):
        sum = self.x + self.y
        print(sum)

    def func2(self):
        print(self.x * 3)


koord = point(12, 15)
koord.func1()
koord.func2()
