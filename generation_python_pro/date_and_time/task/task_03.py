# Напишите программу, которая принимает на вход
# текущие дату и время и определяет количество минут,
# оставшееся до закрытия магазина.
#
# Формат входных данных
# На вход программе подаются текущие дата и время в
# формате DD.MM.YYYY HH:MM.
#
# Формат выходных данных
# Программа должна вывести количество минут,
# которое осталось до закрытия магазина, или текст Магазин не работает,
# если он закрыт.
from datetime import datetime, timedelta, time


d = {(5, 6): (time(10), time(18)),
     (0, 1, 2, 3, 4): (time(9), time(21))
     }

pattern = '%d.%m.%Y %H:%M'
n = input()
dt = datetime.strptime(n, pattern)
day_week, need_time = dt.weekday(), dt.time()

for k,v in d.items():
     if day_week in k:

          if v[0] <= need_time and need_time < v[1]:
               seconds = datetime.combine(dt.date(), v[1]).timestamp() - dt.timestamp()
               print(int(seconds // 60))

          else:
               print('Магазин не работает')


