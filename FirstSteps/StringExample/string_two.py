str1 = input('введите первую строку : ')
str2 = input('введите вторую строку : ')
if str1.isdigit() and str2.isdigit():
    string = int(str1) + int(str2)
    string = str(string)
    string = list(str1) + string.split() + list(str2)
    print(string)
else:
    string = str1 + str2
    string = list(str1) + string.split() + list(str2)
    print(string)
