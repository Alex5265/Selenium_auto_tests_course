# Вам доступен файл food_services.json, содержащий список JSON-объектов,
# которые представляют данные о заведениях общественного питания:
# Под «заведением» будем подразумевать один JSON-объект из этого списка.
# У заведения имеются следующие атрибуты:
#
# Name — название
# IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
# OperatingCompany — название сети
# TypeObject — вид (кафе, столовая, ресторан и т.д.)
# AdmArea — административная зона
# District — район
# Address — полный адрес
# SeatsCount — количество мест
# Напишите программу, которая:
#
# определяет район Москвы, в котором находится больше всего заведений,
# и выводит название этого района и количество заведений в нем
# определяет сеть с самым большим числом заведений и выводит название этой сети и количество заведений этой сети
# Полученные значения программа должна вывести в следующем формате:
#
# <район>: <количество заведений>
# <название сети>: <количество заведений>
# Примечание 1. Гарантируется, что искомая сеть единственная.
# Примечание 2. Пример вывода:
# район Метрогородок: 456
# Французская пекарня SeDelice: 144
import json

with open('food_services.json', encoding='utf-8') as file:
    data = json.load(file)
    districts = {}
    company = {}

    for i in data:
        districts[i['District']] = districts.get(i['District'], 0) + 1
        if i['OperatingCompany']:
            company[i['OperatingCompany']] = company.get(i['OperatingCompany'], 0) + 1

    result_dis = max(districts.items(), key=lambda x: x[1])
    result_comp = max(company.items(), key=lambda x: x[1])
    print(f'{result_dis[0]}: {result_dis[1]}')
    print(f'{result_comp[0]}: {result_comp[1]}')


















