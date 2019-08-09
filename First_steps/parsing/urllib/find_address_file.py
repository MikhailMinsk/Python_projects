"""
Найдите в файле (файл находится в сети Интернет):
http://dfedorov.spb.ru/python/files/mbox-short.txt
строки, содержащие почтовые адреса. Запишите найденные строки в файл с именем mail.txt.
"""

import urllib.request

url = "http://dfedorov.spb.ru/python/files/mbox-short.txt"
lines_with_url = ''
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        if 'http' in line:
            lines_with_url += line + '\n'
print(lines_with_url)
with open('G:\\ProjectPithon\\Fedorov\\txt\\4_out.txt', 'w') as output_file:
    output_file.write('')
for line in lines_with_url:
    with open('G:\\ProjectPithon\\Fedorov\\txt\\4_out.txt', 'a') as output_file:
        output_file.writelines(line)
