# Вам доступен файл countries.json, содержащий список JSON-объектов
# c информацией о странах и исповедуемых в них религиях:
# Каждый объект из этого списка содержит два атрибута:
# country — страна
# religion — исповедуемая религия
# Напишите программу, которая создает единственный JSON-объект,
# имеющий в качестве ключа название религии, а в качестве значения — список стран,
# в которых исповедуется данная религия.
# Полученный JSON-объект программа должна записать в файл religion.json.
import json

with open('countries.json', encoding='UTF-8') as file:
    religions = {}
    data = json.load(file)

    for el in data:
        religions[el['religion']] = religions.get(el['religion'], []) + [el['country']]

with open('religion.json', 'w', encoding='UTF-8') as out:
    json.dump(religions, out)













