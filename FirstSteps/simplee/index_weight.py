def index(x, y):
    m = x / pow(y / 100, 2)
    print('your index is :', round(m, 3))
    if 16 < m < 18.5:
        return print('low body weight. eat-eat-eat !!!')
    elif 18.5 < m < 24.99:
        return print('good body weight. you are sexy :)')
    elif 25 < m < 30:
        return print('quiet overweight. run-run-run everyday !')
    elif 30 < m < 35:
        return print('overweight.  aaa-aaaaa-aaa!!! ')
    else:
        return print("I don't now")


m = float(input('input your weight in kilogram : '))
n = float(input('input your height in centimeter : '))
print(index(m, n))
