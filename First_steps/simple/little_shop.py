katalog = {}
you_shopping = []
cost = 0
while True:
    goods = input('Введите товар или "n" для выхода: ')
    if goods == 'n':
        print('Вы вышли')
        break
    elif goods == '':
        print('Введите товар или n !')
    elif katalog.get(goods) is None:
        tmp = input("Товара нет в каталоге. Для добаления введите 'y' или 'Enter' для продолжения: ")
        if tmp == 'y':
            katalog.update({goods: input('Ведите цену товара: ')})
            print('Товар добавлен')
        elif tmp == '':
            continue
        else:
            print("Неправельный ввод")
            continue
    elif goods in dict.keys(katalog):
        if input("Если желаете купить товар введите 'y' или 'Enter' для продолжения: ") == 'y':
            cost += int(katalog.get(goods))
            print('Товар добавлен в корзину')
            you_shopping.append(goods)
        else:
            continue
print("Ваши покупки: ", you_shopping, '\nЦена: ', cost)
