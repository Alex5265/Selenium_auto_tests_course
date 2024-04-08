# Тимур планирует пойти в бассейн. Среди всех бассейнов ему подходят те,
# которые открыты в понедельник в период с 10:00 до 12:00.
# Также ему нравится плавать по длинным дорожкам, поэтому из всех работающих
# в это время бассейнов нужно выбрать бассейн с наибольшей длиной дорожки,
# при равных значениях — c наибольшей шириной.
#
# Вам доступен файл pools.json, содержащий список JSON-объектов,
# которые представляют данные о крытых плавательных бассейнах:
# Под «бассейном» будем подразумевать один JSON-объект из этого списка.
# У бассейна имеются следующие атрибуты:
#
# ObjectName — название, будь то фитнес клуб или спортивный комплекс
# AdmArea — административный округ
# District — название района
# Address — адрес
# WorkingHoursSummer — график работы, время начала и закрытия указываются в формате HH:MM
# DimensionsSummer — размеры бассейна, где Square — площадь, Length — длина,
# Width — ширина, Depth — глубина
# Напишите программу, которая определяет бассейн, подходящий Тимуру.
# Программа должна вывести его размеры и адрес в следующем формате:
# <длина>x<ширина>
# <адрес>
# Примечание 1. Пример вывода:
# 25x16
# Писцовая улица, дом 12, строение 1
# Примечание 2. Бассейн должен быть открыт во время всего периода с 10:00 до 12:00.
# Например, если бассейн работает в 10:00, но не работает в 11:30, он не подходит.

import json
from datetime import datetime

def find_time(el):
    pattern = '%H:%M'
    start, end = el['WorkingHoursSummer']['Понедельник'].split('-')
    start = datetime.strptime(start, pattern)
    end = datetime.strptime(end, pattern)
    return 10 >= start.hour and end.hour > 12


with open('pools.json', encoding='UTF-8') as file:
    data = json.load(file)

    suitable_pool = list(filter(find_time, data))
    result = max(suitable_pool, key=lambda i: (i['DimensionsSummer']['Length'], i['DimensionsSummer']['Width']))

    print(f'{result["DimensionsSummer"]["Length"]}x{result["DimensionsSummer"]["Width"]}')
    print(result['Address'])













