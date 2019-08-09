"""
Найдите сумму чисел, вводимых с клавиатуры.
Количество вводимых чисел заранее неизвестно.
Окончание ввода, например, слово «Стоп».
"""

summ = 0
while True:
    number = (input('Введите число  или пробел для выхода: '))
    if number == ' ':
        print("Программа завершена. Результат ", summ)
        break
    else:
        if number.isdigit():
            number = int(number)
            summ = summ + number
            print('Сумма = ', summ)
        else:
            continue
