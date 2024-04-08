# Вам доступен файл students.json, содержащий список JSON-объектов,
# которые представляют данные о студентах некоторого курса
# Под «студентом» мы будем подразумевать один JSON-объект из этого списка.
# У студента имеются следующие атрибуты:
# name — имя
# city — город проживания
# age — возраст
# progress — прогресс по курсу в процентах
# phone— контактный номер
# Напишите программу, которая определяет студентов, удовлетворяющих следующим условиям:
# возраст 18 лет или более прогресс по курсу 75 % или более
# Программа должна создать файл data.csv с двумя столбцами — name (имя) и phone (номер),
# и записать в него данные выбранных студентов, расположив их в лексикографическом порядке имён.
# В качестве разделителя в файле data.csv должна быть использована запятая.
# Примечание 1. Гарантируется, что все студенты имеют различные имена.
# Примечание 2. Начальная часть файла data.csv выглядит так:
# name,phone
# Cary,(580) 476-8517
# Catarina,(237) 608-2757
# Catherin,(876) 215-3666

import json, csv


with open('students.json', encoding='UTF-8') as file, \
      open('data.csv', 'w', encoding='UTF-8', newline='') as out:
    data = json.load(file)
    result = []
    for el in data:
        if el['age'] >= 18 and el['progress'] >= 75:
            result.append([el['name'], el['phone']])

    result.sort()
    columns = ['name','phone']

    writer = csv.writer(out)
    writer.writerow(columns)
    for row in result:
        writer.writerow(row)





