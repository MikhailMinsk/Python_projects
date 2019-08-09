# Функция принимает словарь, ключи словаря преобразовывает в строку.
# Возвращает новый словарь

my_dict = {1: 'Страна', 2: 'Город', '3': 'Улица', 4.2: 'Дом'}


# def keys_from_int_to_str(d):
#     new_dict = {}
#
#     for key, value in d.items():
#
#         if isinstance(key, str):
#             new_dict.update({key: value})
#
#         else:
#             key = str(key)
#             new_dict.update({key: value})
#
#     return new_dict
#
#
# print(keys_from_int_to_str(my_dict))

def keyToStr(Dict):
    new_dict = {}
    for key, value in Dict.items():
        if not isinstance(key, str):
            new_key = str(key)
            new_dict.update({new_key: value})
        else:
            new_dict.update({key: value})
    return new_dict


# def keyToStr(Dct):
#     for key in Dct.keys():
#         if not isinstance(key, str):
#             New_key = str(key)
#             Dct[New_key] = Dct.pop(key)


if __name__ == '__main__':
    print(keyToStr(my_dict))
