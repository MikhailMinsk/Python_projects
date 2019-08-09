import os

path = r''  # вставляем путь , r - экран
projectname = ''
folders = ['folder1', 'folder2', 'folder3']

# folders = [['folder1', []],   вложение папок для функции с рекурсией
#            ['folder2', []],   можно создавать структуру через вложенность
#            ['folder3', []]]   папок через вложенность списков

fullpath = os.path.join(path, projectname)  # путь + название проекта


def createfolder(path):
    if not os.path.exists(path):  # проверка на существование папки, иначе выдаст ошибку
        os.mkdir(path)


# def structure(fold, data):   функция рекурсии вложения папок
#     if data:
#         for i in data:
#             path = os.path.join(fold, i[0])
#             createfolder(path)
#             structure(path, i[1])


createfolder(fullpath)

for i in folders:  # циклом создаем папки
    folder = os.path.join(fullpath, i)
    createfolder(folders)
