"""
Дано число, введенное с клавиатуры.
Определите сумму квадратов нечетных цифр в числе.
"""

number = input('введите число : ')
summ = 0
for i in range(len(number)):
    if int(number[i]) % 2 == 0:
        summ = summ + int(number[i])
    else:
        continue

print('сумма цифр в числе = ', summ)