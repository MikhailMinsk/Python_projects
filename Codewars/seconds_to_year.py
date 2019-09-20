def func(seconds):
    """
The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise,
 the duration is expressed as a combination of years, days, hours, minutes and seconds.

Функция должна принимать неотрицательное целое число. Если он равен нулю, он просто возвращает «сейчас».
В противном случае продолжительность выражается в виде комбинации лет, дней, часов, минут и секунд.
    """
    if seconds == 0:
        return 'now'
    time = (
        ('years', 31536000),
        ('days', 86400),
        ('hours', 3600),
        ('minutes', 60),
        ('seconds', 1),
    )
    res = []
    for name, count in time:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            res.append("{} {}".format(value, name))
    if len(res) == 2 and 'second' in ', '.join(res):
        return ', '.join(res[:len(res) - 2]) + ' and '.join(res[len(res) - 2:])
    if len(res) > 2 and 'second' in ', '.join(res):
        return ', '.join(res[:len(res) - 2]) + ', ' + ' and '.join(res[len(res) - 2:])
    return ', '.join(res)


if __name__ == '__main__':
    print(func(3600))
    print(func(120))
    print(func(3662))
    print(func(225945451))
    print(func(62))
