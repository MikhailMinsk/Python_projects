"""число повторений стороки в указанном файле
Находит почему то не все слова (
"""
import re


def pov_str(pattern, fayl):
    count = 0
    for line in fayl:
        if re.search(pattern, line):
            count += 1
    return count


vvod = input('Введите текст для поиска : ')+r'.*?'
with open('G:\\ProjectPithon\\Fedorov\\txt\\5_out.txt') as f:
    text = f.readlines()
print(text)

print('Количество раз сколько встречается в тексте', vvod, '=', pov_str(vvod, text))