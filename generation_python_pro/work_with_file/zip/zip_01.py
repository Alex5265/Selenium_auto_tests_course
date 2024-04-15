from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    zip_file.printdir()



# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[6].file_size)                # размер начального файла в байтах
#     print(info[6].compress_size)            # размер сжатого файла в байтах
#     print(info[6].filename)                 # имя файла
#     print(info[6].date_time)


# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[0].is_dir())
#     print(info[6].is_dir())

# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()
#     print(*info, sep='\n')
#

#
# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()                # получаем названия всех файлов архива
#     last_file = zip_file.getinfo(info[-4])    # получаем информацию об отдельном файле
#     print(last_file.file_size)
#     print(last_file.compress_size)
#     print(last_file.filename)
#     print(last_file.date_time)

# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     with zip_file.open('test/Разные файлы/astros.json') as file:
#         print(file.read())


# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     with zip_file.open('test/Разные файлы/astros.json') as file:
#         print(file.read().decode('utf-8'))
#


# from zipfile import ZipFile
#
# with ZipFile('archive.zip', mode='w') as zip_file:
#     zip_file.write('program.py')
#     zip_file.write('lse.jpeg')
#     print(zip_file.namelist())
#

# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     zip_file.extract('test/Картинки/avatar.png')
#     zip_file.extract('test/Программы/image_util.py')
#     zip_file.extract('lse.jpeg')





















