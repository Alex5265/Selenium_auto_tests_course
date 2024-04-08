# Напишите программу, которая объединяет два данных JSON-объекта в один JSON-объект,
# причем если пары из первого и второго объектов имеют совпадающие ключи,
# то значение следует взять из второго объекта.
# Полученный JSON-объект программа должна записать в файл data_merge.json.

import json

with open('data1.json', encoding='UTF-8') as data1, open('data2.json', encoding='UTF-8') as data2:
    d1 = json.load(data1)
    d2 = json.load(data2)
    result = d1 | d2

with open('data_merge.json', 'w', encoding='UTF-8') as out:
    json.dump(result, out)





