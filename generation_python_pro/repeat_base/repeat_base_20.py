# Вам доступен текстовый файл files.txt, содержащий информацию о файлах.
# Каждая строка файла содержит три значения, разделенные символом пробела — имя файла,
# его размер (целое число) и единицы измерения:
#
# cant-help-myself.mp3 7 MB
# keep-yourself-alive.mp3 6 MB
# bones.mp3 5 MB
# ...
# Напишите программу, которая группирует данные файлы по расширению,
# определяя общий объем файлов каждой группы, и выводит полученные группы файлов,
# указывая для каждой ее общий объем. Группы должны быть расположены в лексикографическом
# порядке названий расширений, файлы в группах — в лексикографическом порядке их имен.


UNITS = {
    'B': 1,
    'KB': 1024,
    'MB': 1024 ** 2,
    'GB': 1024 ** 3,
}


def convert_bytes(num: int) -> str:
    step_unit = 1024
    for unit in UNITS.keys():
        if num < step_unit:
            return f'{round(num)} {unit}'
        num /= step_unit


with open('files.txt', encoding='utf-8') as f:
    files = [file.strip() for file in f.readlines()]

file_extensions = {}
for file in files:
    file_name, file_size, file_unit = file.split()
    index = file_name.rfind('.')
    key = file_name[index:]
    bytes_size = int(file_size) * UNITS[file_unit]
    file_extensions.setdefault(key, []).append((file_name, bytes_size))

for extension in sorted(file_extensions.keys()):
    size = 0
    for file_name, file_size in sorted(file_extensions[extension]):
        print(file_name)
        size += file_size
    print('-' * 10)
    print(f'Summary: {convert_bytes(size)}\n')