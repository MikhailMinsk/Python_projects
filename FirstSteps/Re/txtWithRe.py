import re

with open('G:\\ProjectPithon\\Fedorov\\txt\\ParseData.txt') as f:
    text = f.read()



def pars(text):
    srch = "\[.*..:..:..]"
    print(re.findall(srch, text))


pars(text)
