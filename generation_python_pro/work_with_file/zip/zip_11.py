# Вам доступен архив desktop.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит его файловую структуру и объем каждого файла.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести файловую структуру архива desktop.zip и объем каждого файла в несжатом виде.
# Так как архив имеет собственную иерархию папок, каждый уровень вложенности должен быть выделен двумя пробелами.
#
# Примечание 1. Вывод на примере архива test.zip из конспекта:
#
# test
#   Картинки
#     1.jpg 88 KB
#     avatar.png 19 KB
#     certificate.png 43 KB
#     py.png 33 KB
#     World_Time_Zones_Map.png 2 MB
#     Снимок экрана.png 11 KB
#   Неравенства.djvu 5 MB
#   Программы
#     image_util.py 5 KB
#     sort.py 61 B
#   Разные файлы
#     astros.json 505 B
# Примечание 2. Объем файла записывается в самых крупных единицах измерения с округлением до целых.
from zipfile import ZipFile

UNITS = {
    'B': 1,
    'KB': 1024,
    'MB': 1024 ** 2,
    'GB': 1024 ** 3,
}

def conversed_bytes(b):
    step = 1024
    for size in UNITS:
        if b < step:
            return f'{round(b)} {size}'
        else:
            b /= step


with ZipFile('desktop.zip') as zip_file:
    info = zip_file.infolist()

    for el in info:
        if el.is_dir():
            print('  ' * (len(el.filename.rsplit('/', )) - 2) + el.filename.split('/')[-2])
        else:
            size = conversed_bytes(el.file_size)
            print('  ' * (len(el.filename.rsplit('/', )) - 1) + el.filename.split('/')[-1], size)











