from random import randint

x = randint(1, 100)
while True:
    chislo_polsovatel = input(' введите число от 1 до 100 или пробел для выхода : ')
    if chislo_polsovatel == ' ':
        print(' Программа закончена. Вы вышли. ')
        break
    elif int(chislo_polsovatel) in range(1, 101):
        chislo_polsovatel = int(chislo_polsovatel)
        if x == chislo_polsovatel:
            print('Вы угадали!!!')
        elif x > chislo_polsovatel:
            print('Задуманное число больше')
        else:
            print('Задуманное число меньше')
    else:
        continue
