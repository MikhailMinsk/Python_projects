"""
Определите частоту встречаемости всех слов для текста,
находящегося в сети Интернет: http://dfedorov.spb.ru/python3/src/romeo.txt
PS: используйте словари (dict).
"""

import urllib.request

lst = []
url = "http://dfedorov.spb.ru/python3/src/romeo.txt"
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        print(line)
        lst += line.split()


def diction(s):
    d = dict()
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d


print('\n\n',diction(lst))
