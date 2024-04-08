# Вам доступен файл people.json, содержащий список JSON-объектов.
# Причем у различных объектов может быть различное количество ключей:
# Напишите программу, которая добавляет в каждый JSON-объект из данного списка
# все недостающие ключи, присваивая этим ключам значение null. Ключ считается недостающим,
# если он присутствует в каком-либо другом объекте, но отсутствует в данном.
# Программа должна создать список с обновленными JSON-объектами и записать его в файл updated_people.json.
#
# Примечание 1. JSON-объекты в создаваемом программой списке должны располагаться в своем исходном порядке.
# Порядок ключей в JSON-объектах не важен.
import json

with open('people.json', encoding='UTF-8') as orig_data:
    data = json.load(orig_data)
    header = set()

    for el in data:
        header |= el.keys()

    for el in data:
        el |= dict.fromkeys(header - el.keys())



with open('updated_people.json', 'w', encoding='UTF-8') as out:
    json.dump(data, out, indent= 3)









