"""
Дан произвольный текст.
 Найдите номер первого самого длинного слова в нем.
"""
text = input('введите текст')
text = text.split()
y = 0
x = 0
for i in range(len(text)):
    x = len(text[i])
    if x > y:
        y = x
        t = text.index(text[i])
print(t)
