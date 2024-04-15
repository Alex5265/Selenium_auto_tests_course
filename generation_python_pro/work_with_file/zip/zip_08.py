# Вам доступен набор различных файлов, названия которых представлены в списке file_names.
# Также вам доступен архив files.zip. Дополните приведенный ниже код,
# чтобы он добавил в архив files.zip только те файлы из списка file_names, объем которых не превышает
# 100
# 100 байт.
#
# Примечание 1. Получить объем файла в байтах позволяет функция getsize() из модуля os.path.
# Данная функция принимает в качестве аргумента путь к файлу и возвращает размер указанного файла в байтах.
#
# Например, вычислить объем архива files.zip в байтах и сохранить его в переменную size можно следующим образом:
#
# import os.path
#
# size = os.path.getsize('files.zip')
# Примечание 2. Вычислить объем файла в байтах можно и вручную,
# не прибегая к использованию сторонних модулей. Подумайте, как 😉

import os
from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

def added_zip_file(file_name, arhive_name):
    with ZipFile(arhive_name, mode='a') as zip_file:
        need_size = [zip_file.write(i) for i in file_names if os.path.getsize(i) < 100]


arhive_name = 'files.zip'
added_zip_file(file_names, arhive_name)












