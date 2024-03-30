# примеры кода из конспекта

from datetime import date

my_date = date(1992, 10, 6)    # тип date: год + месяц + день

print(my_date)
print(type(my_date))




print('Год =', my_date.year)
print('Месяц =', my_date.month)
print('День =', my_date.day)

creation_date = date.today()
print(creation_date)


date1 = date(2022, 10, 15)
date2 = date(1999, 12, 26)

print(date1.weekday())
print(date2.weekday())
# 5      # суббота
# 6      # воскресенье

print(date.min)
print(date.max)

date1 = date.fromordinal(365)     # дата, соответствуюшая номеру дня 365
date2 = date(1999, 12, 26)

print(date1)
print(date2.toordinal())          # номер дня, соответствующий дате 1999-12-26