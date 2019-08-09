import random

x = ' '
while x == ' ':
    x = input('введите пробел для броска  или любое число для последнего броска: ')
    m = random.randint(1, 7) + random.randint(1, 7)
    n = random.randint(1, 7) + random.randint(1, 7)
    if m > n:
        print('победил 1й игрок')
        print('m=', m)
        print('n=', n)
    elif m < n:
        print('победил 2й игрок')
        print('m=', m)
        print('n=', n)
    else:
        print('вы выбросили поровну')
        print('m=', m)
        print('n=', n)

# тут конечно надо бы подпеределать...Не нравится мне это любое число ... Надо бы сделать через Break