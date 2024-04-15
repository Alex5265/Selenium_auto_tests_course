# Вам доступен архив data.zip, содержащий различные папки и файлы.
# Среди них есть несколько JSON файлов,
# каждый из которых содержит информацию о каком-либо футболисте:
# {
#    "first_name": "Gary",
#    "last_name": "Cahill",
#    "team": "Chelsea",
#    "position": "Defender"
# }
# У футболиста имеются следующие атрибуты:
#
# first_name — имя
# last_name — фамилия
# team — название футбольного клуба
# position — игровая позиция
# Напишите программу, которая обрабатывает только данные JSON файлы
# и выводит имена и фамилии футболистов, выступающих за футбольный клуб Arsenal.
# Футболисты должны быть расположены в лексикографическом порядке имен,
# а при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.
#
# Примечание 1. Обратите внимание, что наличие у файла расширения
# .json не гарантирует, что он является корректным текстовым файлом в формате JSON.
# Для того чтобы определить, является ли файл корректным текстовым файлом в формате JSON, воспользуйтесь конструкцией try-except и функцией is_correct_json() из предыдущего урока.
#
# Примечание 2. Начальная часть ответа выглядит так:

from zipfile import ZipFile
import json

def is_correct_json(string):
    try:
        js = json.loads(string)
    except json.decoder.JSONDecodeError:
        return False
    return True


with ZipFile('data.zip') as zip_file:
    file_names = []
    d = []
    info = zip_file.infolist()

    for i in info:
        if not i.is_dir():
            if i.filename.split('.')[-1] == 'json':
                file_names.append(i.filename)

    for name in file_names:
        with zip_file.open(name) as file:
            try:
                js = json.loads(file.read().decode('latin-1'))
            except json.decoder.JSONDecodeError:
                continue
            if js['team'] == 'Arsenal':
                d.append(' '.join((js['first_name'], js['last_name'])))

    print(*sorted(d), sep='\n')










































