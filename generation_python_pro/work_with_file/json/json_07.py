# Вам доступен файл data.json, содержащий список различных объектов:

# Напишите программу, которая создает список, элементами которого являются объекты из списка,
# содержащегося в файле data.json, измененные по следующим правилам:
#
# если объект является строкой, в его конец добавляется восклицательный знак
# если объект является числом, он увеличивается на единицу
# если объект является логическим значением, он инвертируется
# если объект является списком, он удваивается
# если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
# если объект является пустым значением (null), он не добавляется
# Полученный список программа должна записать в файл updated_data.json.
#
# Примечание 1. Например, если бы файл data.json имел вид:
#
# ["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
# то программа должна была бы создать файл updated_data.json со следующим содержанием:
#
# ["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]

import json

with open('data.json', encoding='UTF-8') as file:
    to_js = json.load(file)
    result = []

    for el in to_js:
        if isinstance(el, str):
            result.append(el + "!")
        elif type(el) == bool:
            result.append(not el)
        elif isinstance(el, int):
            result.append(el + 1)
        elif isinstance(el, list):
            result.append(el + el)
        if isinstance(el, dict):
            result.append(el | {"newkey": None})
with open('updated_data.json', 'w', encoding= 'UTF-8') as out:
    json.dump(result, out)













