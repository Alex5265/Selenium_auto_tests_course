import json


def create_religion_json(input_file, output_file):
    religion_countries = {}

    # Чтение данных из файла countries.json
    with open(input_file, 'r', encoding='utf-8') as file:
        countries_data = json.load(file)

    # Группировка стран по религиям
    for entry in countries_data:
        country = entry['country']
        religion = entry['religion']
        if religion in religion_countries:
            religion_countries[religion].append(country)
        else:
            religion_countries[religion] = [country]

    # Запись данных в файл religion.json
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(religion_countries, file, ensure_ascii=False, indent=4)


# Вызов функции с указанием входного и выходного файлов
create_religion_json('countries.json', 'religion.json')


# Конечно! Вот более подробное объяснение кода построчно:
#
# Мы начинаем с импорта модуля json, который поможет нам работать с данными в формате JSON.
#
# Создаем функцию create_religion_json, которая принимает два аргумента: input_file (имя входного файла) и output_file (имя файла, в который мы будем записывать результат).
#
# Внутри функции открываем файл countries.json для чтения ('r'), используя open(). Этот файл содержит информацию о странах и религиях, и мы загружаем его содержимое в переменную countries_data с помощью json.load().
#
# Создаем пустой словарь religion_countries, который будет содержать религии в качестве ключей и списки стран в качестве значений.
#
# Проходим по каждой записи в countries_data (каждая запись представляет собой информацию о стране и религии).
#
# Для каждой записи извлекаем название страны и исповедуемую религию.
#
# Проверяем, существует ли уже запись для этой религии в словаре religion_countries. Если да, добавляем текущую страну в список стран для этой религии. Если нет, создаем новую запись в словаре с текущей страной.
#
# После того как мы прошли все записи, словарь religion_countries будет содержать информацию о странах, разделенных по религиям.
#
# Открываем файл religion.json для записи ('w') и используем json.dump() для записи содержимого словаря religion_countries в файл в формате JSON. Мы указываем ensure_ascii=False, чтобы сохранить правильную кодировку для символов не на латинице, и indent=4, чтобы получить красиво отформатированный JSON.
#
# Функция завершена. Мы вызываем эту функцию, передавая ей имена входного и выходного файлов, чтобы она могла выполнить свою работу.