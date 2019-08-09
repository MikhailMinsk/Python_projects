import re

document = 'G:\\ProjectPithon\\Fedorov\\txt\\ParseData.txt'
with open(document) as f:
    text = f.read()


def pars(text):
    """
    print date from document
    """
    srch = "\[.*..:..:..]"
    print(re.findall(srch, text))


if __name__ == '__main__':
    pars(text)
