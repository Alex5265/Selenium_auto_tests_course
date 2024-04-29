# Тимур живет в мире, в котором цена товара определяется как сумма
# Unicode кодов букв его названия. Буквенным обозначением данной валюты являются
# две заглавные латинские буквы UC. Например, ручка в его мире стоит:
# 1088+1091+1095+1082+1072=5428UC
# Тимур составляет список покупок, но так как на его клавиатуре перестал
# работать блок с цифрами, то вместо указания количества товара числом,
# он добавляет его в список столько раз, сколько планирует купить.
# Все товары Тимур записывает в нижнем регистре через запятую.
#
# Напишите программу, которая группирует одинаковые товары из данного списка
# покупок и определяет стоимость каждой группы.
#
# Формат входных данных
# На вход программе подается последовательность товаров, разделенных запятой без пробелов.
#
# Формат выходных данных
# Программа должна сгруппировать одинаковые товары, определить общую стоимость
# каждой группы и вывести полученный результат. Товары должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:
#
# <товар>: <цена за единицу товара> UC x <количество товаров в группе> = <общая стоимость группы> UC
# Примечание 1. Программа должна добавлять нужное количество пробелов,
# если название товара имеет меньшую длину, чем другие.
#
# Примечание 2. Получить Unicode код символа можно с помощью функции ord().

from collections import Counter

def price_item(item):
    return sum([ord(i) for i in item if i.isalpha()])

count_items = Counter(input().split(','))
pattern = '{}: {} UC x {} = {} UC'

for prod, count in sorted(count_items.items()):
    price = price_item(prod)
    total = price * count
    prod = prod.ljust(max(map(len, count_items)))
    print(pattern.format(prod, price,count, total))














