from datetime import datetime

my_datetime = datetime(1992, 10, 6, 9, 40, 23, 51204)    # создаем полную дату-время
only_date = datetime(2021, 12, 31)                       # создаем дату-время с нулевой временной информацией

print(my_datetime)
print(only_date)
print(type(my_datetime))


from datetime import datetime

my_datetime = datetime(2022, 10, 7, 14, 15, 45)
my_date = my_datetime.date()                     # получаем только дату (тип date)
my_time = my_datetime.time()                     # получаем только время (тип time)

print(my_datetime, type(my_datetime))
print(my_date, type(my_date))
print(my_time, type(my_time))


from datetime import datetime

datetime_now = datetime.now()
datetime_utcnow = datetime.utcnow()

print(datetime_now)           # текущее локальное время (московское) на момент запуска программы
print(datetime_utcnow)        # текущее UTC время на момент запуска программы


from datetime import datetime

my_datetime = datetime(2021, 10, 13, 8, 10, 23)

print(my_datetime.timestamp())


from datetime import datetime

my_datetime = datetime.fromtimestamp(1634101823.0)

print(my_datetime)


from datetime import datetime

datetime0 = datetime.strptime('10.08.2034 13:55:59', '%d.%m.%Y %H:%M:%S')
datetime1 = datetime.strptime('10/08/21', '%d/%m/%y')
datetime2 = datetime.strptime('Tuesday 10, August 2021', '%A %d, %B %Y')
datetime3 = datetime.strptime('18.20.34', '%H.%M.%S')
datetime4 = datetime.strptime('2021/08/10', '%Y/%m/%d')
datetime5 = datetime.strptime('10.08.2021 (Tuesday, August)', '%d.%m.%Y (%A, %B)')
datetime6 = datetime.strptime('Year: 2021, Month: 08, Day: 10, Hour: 18.', 'Year: %Y, Month: %m, Day: %d, Hour: %H.')

print(datetime0, datetime1, datetime2, datetime3, datetime4, datetime5, datetime6, sep='\n')


from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

my_datetime = datetime(2021, 8, 10, 12, 34, 15)

print(my_datetime.strftime('%A %d, %B %Y, %H:%M:%S'))












