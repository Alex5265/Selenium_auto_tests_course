# Для дополнительного заработка Тимур решил заняться продажей овощей.
# У него имеются данные о продажах за год, разделенные на четыре файла по кварталам:
# quarter1.csv, quarter2.csv, quarter3.csv и quarter4.csv.
# В каждом файле в первом столбце указывается название продукта,
# а в последующих — количество проданного продукта в килограммах за определенный месяц:
#
# продукт,январь,февраль,март
# Картофель,39,61,3
# Дайкон,51,96,83
# ...
# Также присутствует файл prices.json, содержащий словарь,
# в котором ключом является название продукта, а значением — цена за килограмм в рублях:
#
# {
#    "Картофель": 53,
#    "Дайкон": 55,
# ...
# }
# Напишите программу, которая выводит единственное число — сумму,
# заработанную Тимуром за год на продаже овощей.

import json
import csv
from collections import Counter

product = dict()
list_file = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']

for files in list_file:
    with open(files, encoding='utf-8') as file, open('prices.json', encoding='utf-8') as price:
        _, *data = csv.reader(file)
        actual_price = json.load(price)

        for row in data:
            name, *mass = row
            mass = sum([int(i) for i in mass]) * actual_price[name]
            product[name] = product.get(name, 0) + mass

result = Counter(product)

print(result.total())

















