import random

string = ['самовар', 'весна', 'лето']
slovo = random.choice(string)
bykva = random.choice(slovo)
print(slovo.replace(bykva, '..'))
b = input('вставьте недостающую букву : ')
if bykva == b:
    print('Верно !!!')
else:
    print('НЕВЕРНО!!! Иди в школу!')
