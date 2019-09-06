def func(seconds):
    """
    Write a function, which takes a non-negative integer (seconds) as input
    and returns the time in a human-readable format (HH:MM:SS)
    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59
    The maximum time never exceeds 359999 (99:59:59)

    Напишите функцию, которая принимает неотрицательное целое число (в секундах)
    в качестве входных данных и возвращает время в удобочитаемом формате (ЧЧ: ММ: СС).
    ЧЧ = часы, дополненные до 2 цифр, диапазон: от 00 до 99
    MM = минуты, дополненные до 2 цифр, диапазон: 00 - 59
    SS = секунды, дополненные до 2 цифр, диапазон: 00 - 59
    Максимальное время никогда не превышает 359999 (99:59:59)
    """
    return '%02i:%02i:%02i' % (seconds // 3600, (seconds - 3600 * (seconds // 3600)) // 60,
                               seconds - 3600 * (seconds // 3600) - 60 * ((seconds - 3600 * (seconds // 3600)) // 60))


if __name__ == '__main__':
    print(func(60))
    print(func(86399))
