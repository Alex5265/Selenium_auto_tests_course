# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит суммарный объем файлов
# этого архива в сжатом и не сжатом видах в байтах, в следующем формате:
#
# Объем исходных файлов: <объем до сжатия> байт(а)
# Объем сжатых файлов: <объем после сжатия> байт(а)

from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    start_size = sum([i.file_size for i in info])
    compress = sum([i.compress_size for i in info])

    print(f'Объем исходных файлов: {start_size} байт(а)')
    print(f'Объем сжатых файлов: {compress} байт(а)')








