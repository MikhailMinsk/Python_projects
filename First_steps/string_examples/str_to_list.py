s = 'строка для изменения'
print(list(s))
lst = list(s)
lst[0] = 'Бббб'
print(lst)
s = ' '.join(lst)
print(s)
s = ''.join(lst)
print(s)
s = '***'.join(lst)
print(s)
print('_________________________________________')

n = 5165661655651
print(list(str(n)))
"""число можно преобразовать в строку, строку в список, список изменить, а потом обратно 
преобразовать в число """

print('_________________________________________')

K = 'а можно сделать еще и вот так, что тоже удобно'
# ставим пробел как разделитель
print(K.split(' '))