# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения.
# Напишите программу, которая определяет самого молодого сотрудника,
# празднующего свой день рождения в течение ближайших семи дней от текущей даты.
#
# Формат входных данных
# На вход программе в первой строке подается текущая дата в формате DD.MM.YYYY,
# в следующей строке вводится натуральное число n — количество сотрудников,
# работающих в организации. В последующих n строках вводятся данные о каждом сотруднике:
# имя, фамилия и дата рождения, разделённые пробелом.
# Дата рождения указывается в формате DD.MM.YYYY.
#
# Формат выходных данных
# Программа должна определить самого молодого сотрудника,
# празднующего свой день рождения в течение ближайших семи дней,
# и вывести его имя и фамилию, разделив пробелом. Если таких сотрудников нет,
# программа должна вывести текст:
# Дни рождения не планируются
# Примечание 1. Гарантируется, что у всех сотрудников даты рождения различны.
# Примечание 2. Например, для даты 01.11.2021 ближайшими семью днями являются:
# 02.11.2021, 03.11.2021, 04.11.2021, 05.11.2021, 06.11.2021, 07.11.2021, 08.11.2021

from datetime import datetime, timedelta

pattern = '%d.%m.%Y'
data_start = datetime.strptime(input(), pattern)
data_person = []

for _ in range(int(input())):
    name, birthday = input().rsplit(' ', 1)
    birthday = datetime.strptime(birthday, pattern)
    data_person.append((name, birthday))

data_person = sorted(data_person, key=lambda x: x[-1], reverse=True)

result = []

for el in data_person:
    name, dt = el
    if data_start + timedelta(hours=24) < dt.replace(year=data_start.year) <= data_start + timedelta(hours=24 * 7) or data_start + timedelta(hours=24) < dt.replace(year=data_start.year + 1) <= data_start + timedelta(hours=24 * 7):
        result.append(name)

if len(result) > 0:
    print(result[0])
else:
    print('Дни рождения не планируются')













