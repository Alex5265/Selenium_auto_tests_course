# примеры кода из конспекта

from datetime import time

my_time = time(11, 20, 54, 1234)    # тип time: часы + минуты + секунды + микросекунды

print(my_time)
print(type(my_time))

time1 = time(11, 20, 54, 1234)
time2 = time(11, 20, 54)
time3 = time(11, 20)
time4 = time(11)
time5 = time()
time6 = time(minute=23, second=56)

print(time1, time2, time3, time4, time5, sep='\n')
print(time6)


my_time = time(11, 20, 54, 1234)

print('Часы =', my_time.hour)
print('Минуты =', my_time.minute)
print('Секунды =', my_time.second)
print('Микросекунды =', my_time.microsecond)

from datetime import date, time

my_date = date(2021, 12, 31)
my_time = time(11, 20, 54)

print(my_date)
print(my_time)

from datetime import date, time

my_date = date(2021, 12, 31)
my_time = time(11, 20, 54)

print(str(my_date))
print(str(my_time))

my_date = date(2021, 12, 31)
my_time = time(11, 20, 54)

print(repr(my_date))
print(repr(my_time))

from datetime import date

date1 = date(1992, 10, 6)
date2 = date1.replace(year=1995)            # заменяем год
date3 = date1.replace(month=12, day=17)     # заменяем месяц и число

print(date1)
print(date2)
print(date3)

from datetime import date

my_date = date(2020, 6, 17)
my_date.replace(month=9, day=29)

print(my_date)

import datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)


from datetime import date

dates = [date(2000, 12, 31), date(1999, 3, 8), date(1999, 2, 22)]

max_date = max(dates)
min_date = min(dates)

print(max_date.year + min_date.day)