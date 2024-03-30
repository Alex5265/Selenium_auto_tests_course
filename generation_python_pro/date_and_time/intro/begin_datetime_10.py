from datetime import date, time

my_date = date(2021, 8, 10)
my_time = time(7, 18, 34)

print(my_date.strftime('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S %f %z %Z %j %U %W %c %x %X'))
print(my_time.strftime('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S %f %z %Z %j %U %W %c %x %X'))


#
# Tue Tuesday 2 10 Aug August 08 21 2021 00 12 AM 00 00 000000   222 32 32 Tue Aug 10 00:00:00 2021 08/10/21 00:00:00
# Mon Monday 1 01 Jan January 01 00 1900 07 07 AM 18 34 000000   001 00 01 Mon Jan  1 07:18:34 1900 01/01/00 07:18:34



given_date = date(2021, 7, 17)

print(given_date.strftime('%A %d %B %Y'))
print(given_date.strftime('%Y/%m/%d'))
print(given_date.strftime('%d.%m.%Y (%A, %B)'))
print(given_date.strftime('Day of year: %j, week number: %U'))


from datetime import date
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

my_date = date(2021, 8, 10)
print(my_date.strftime("%A %d, %B %Y"))    # форматированный вывод даты в русской локализации



my_date = date(2021, 12, 31)
my_time = time(21, 15, 17)

print('Дата: ' + str(my_date))
print('Время: ' + str(my_time))

















