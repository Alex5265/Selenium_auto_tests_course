# Напишите программу, которая принимает на вход время
# и выводит целое количество секунд, прошедшее с начала суток.
# Формат входных данных
# На вход программе подается время в формате HH:MM:SS.
# Формат выходных данных
# Программа должна вывести целое количество секунд, прошедшее с начала суток.
# Примечание 1. Началом суток считается момент времени,
# соответствующий 00:00:00.

from datetime import datetime, timedelta, time

# dt = datetime.strptime(input(), '%H:%M:%S')
# res = timedelta(hours=dt.hour, minutes=dt.minute, seconds=dt.second)
#
# print(int(res.total_seconds()))

h, m, s = map(int, input().split(':'))

td = timedelta(hours=h, minutes=m, seconds=s)

print(int(td.total_seconds()))
