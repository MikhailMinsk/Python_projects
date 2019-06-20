class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)


first = Vector2d(5, 6)
second = Vector2d(7, 8)
result = first + second
print(result.x)
print(result.y)


# ____________________________________________________________
class spetialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = '=' * len(other.cont)
        return '\n'.join([self.cont, line, other.cont])


spam = spetialString('spam')
hello = spetialString('Hello world')
print('\n')
print(spam / hello)


# ______________________________________________________________
class specialStr:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont) + 1):
            result = other.cont[:index] + '>' + self.cont
            result += '>' + other.cont[index:]
            print(result)


print('\n')
spam = specialStr('spam')
eggs = specialStr('eggs')
spam > eggs

# _______________________________________________________________
from random import randint


class vaguelist:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, item):
        return self.cont[item + randint(-1, 1)]

    def __len__(self):
        return randint(0, len(self.cont) * 2)


value_list = vaguelist(['A', 'B', 'C', 'D', 'E'])
print('\n')
print(len(value_list))
print(len(value_list))
print(value_list[2])
print(value_list[2])
