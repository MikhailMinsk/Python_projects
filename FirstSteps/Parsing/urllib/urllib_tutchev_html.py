"""
Напишите программу, которая создает (генерирует) полноценный HTML-документ,
содержащий текст, приведенный по ссылке: http://dfedorov.spb.ru/python/files/tutchev.txt
и под текстом размещает картинку: http://dfedorov.spb.ru/python/files/tutchev.jpg
Пример итогового HTML-документа: http://dfedorov.spb.ru/python/files/p.html
(обратите внимание на код страницы, содержащей HTML-теги).
Выполните обработку ошибок.
PS. в момент чтения и записи используйте параметр функции open() encoding='utf-8'.
"""

import urllib.request


# Открыть файл получается почему то только в Хроме , ИЕ не  декодирует текст кирилицы
# Пока не знаю как схранить в html файле.Выдает набор символов


with open('G:\\ProjectPithon\\Fedorov\\txt\\3_out.html', 'w', encoding="utf-8") as output_file:
    output_file.write('\n')

url = "http://dfedorov.spb.ru/python/files/tutchev.txt"
text = []
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        print(line)
        text += line + '\n'
        with open('G:\\ProjectPithon\\Fedorov\\txt\\3_out.html', 'a', encoding="utf-8") as output_file:
            output_file.writelines(line)
print(text)
del text[0]
print(text)
for line in text:
    with open('G:\\ProjectPithon\Fedorov\\txt\\3_out.txt', 'a') as output_file:
        output_file.writelines(line)

image = urllib.request.urlopen("http://dfedorov.spb.ru/python/files/tutchev.jpg")
# out = open('G:\\Python_programs\\fedorov\\txt\\3.jpg', 'wb')
out = open('G:\\ProjectPithon\\Fedorov\\txt\\3_out.html', 'ab')# возможно надо знать кодировку jpg для html
out.write(image.read())
out.close()
