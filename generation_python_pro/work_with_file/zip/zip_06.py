# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит названия всех файлов из этого архива
# в лексикографическом порядке, указывая для каждого его дату изменения,
# а также объем до и после сжатия, в следующем формате:
#
# <название файла>
#   Дата модификации файла: <дата изменения>
#   Объем исходного файла: <объем до сжатия> байт(а)
#   Объем сжатого файла: <объем после сжатия> байт(а)
# Между данными о двух файлах должна располагаться пустая строка.
#
# Примечание 1. Если файл находится в папке, вывести следует только название без пути.
#
# Примечание 2. Начальная часть ответа выглядит так (в качестве отступов используйте два пробела):
#
# Alexandra Savior – Crying All the Time.mp3
#   Дата модификации файла: 2021-11-30 13:27:02
#   Объем исходного файла: 5057559 байт(а)
#   Объем сжатого файла: 5051745 байт(а)
#
# Hollow Knight Silksong.exe
#   Дата модификации файла: 2013-08-22 08:20:06
#   Объем исходного файла: 805992 байт(а)
#   Объем сжатого файла: 494930 байт(а)
#
# ...
from datetime import datetime
from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    d = {}

    for i in info:
        if not i.is_dir():
            d.setdefault(i.filename.rsplit('/')[-1], []).extend([i.date_time, i.file_size, i.compress_size])

    for k, v in sorted(d.items()):
        date, size, compress = v
        print(f'''{k}
  Дата модификации файла: {datetime(*date)}
  Объем исходного файла: {size} байт(а)
  Объем сжатого файла: {compress} байт(а)
''')














