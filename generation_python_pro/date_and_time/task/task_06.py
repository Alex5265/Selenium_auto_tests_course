# Дан список сотрудников организации, в котором указаны их фамилии,
# имена и даты рождения. Напишите программу, которая определяет,
# в какую из дат родилось больше всего сотрудников.
#
# Формат входных данных
# На вход программе в первой строке подается натуральное число n — количество сотрудников,
# работающих в организации. В последующих n строках вводятся данные о каждом сотруднике:
# имя, фамилия и дата рождения, разделённые пробелом. Дата рождения указывается в формате DD.MM.YYYY.
#
# Формат выходных данных
# Программа должна вывести дату, в которую наибольшее количество сотрудников
# отмечает день рождения, в формате DD.MM.YYYY. Если таких дат несколько,
# программа должна вывести их все в порядке возрастания, каждую на отдельной строке,
# в том же формате.

from datetime import datetime, timedelta

dates = {}
pattern = '%d.%m.%Y'
counter = 0

for _ in range(int(input())):
    *_, birthday = input().split()
    birthday = datetime.strptime(birthday, pattern)
    dates[birthday] = dates.get(birthday, 0) + 1
    if dates[birthday] > counter:
        counter = dates[birthday]

print(dates)
frequent_dates = [dt for dt, amount in dates.items() if amount == counter]

print(frequent_dates)
for dt in sorted(frequent_dates):
    print(dt.strftime(pattern))



































