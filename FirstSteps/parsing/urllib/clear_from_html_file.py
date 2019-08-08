"""
Очистите файл от HTML-тегов: http://dfedorov.spb.ru/python/files/p.html
Выведите на экран «чистый» текст. PS. можно использовать только стандартные модули Python.
"""

import urllib.request
import re

url = "http://dfedorov.spb.ru/python/files/p.html"
lines_from_url = ''
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        print(line)
        lines_from_url += line + '\n'
print(lines_from_url)
pattern = r"<.*?>"
lines_from_url = re.sub(pattern, '', lines_from_url)
print(lines_from_url)
with open('G:\\ProjectPithon\\Fedorov\\txt\\5_out.txt', 'w') as output_file:
    output_file.write('')
for line in lines_from_url:
    with open('G:\\ProjectPithon\\Fedorov\\txt\\5_out.txt', 'a') as output_file:
        output_file.writelines(line)
