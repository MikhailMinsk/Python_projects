# Написать функцию, которая принимает список и возвращает его отсортированным, если он состоит из чисел,
# в противном случае, выдает ошибку TypeError


# mynewlist = [s for s in mylist if s.isdigit()]

def check_int(Lst):
    for i in Lst:
        if type(i) not in [int, float]:
            raise TypeError
    return print('its all right. All is numbers!')


a = [1, 2, '', 3, 5]
try:
    check_int(a)
except Exception as er:
    print('I found error: ', repr(er))
