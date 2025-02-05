# Вам доступен файл zoo.json, содержащий список JSON-объектов с данными об обитателях
# некоторого зоопарка. Ключом в каждом объекте является название животного,
# значением — их количество в зоопарке:
#
# Напишите программу, которая определяет, сколько всего животных обитает в зоопарке,
# и выводит полученный результат.
#
# Примечание 1. Гарантируется, что все ключи в JSON-объектах, различны.


import json
from collections import ChainMap

with open('zoo.json', encoding='utf-8') as file:
    data = json.load(file)
    animals = ChainMap(*data)

    print(sum(animals.values()))













