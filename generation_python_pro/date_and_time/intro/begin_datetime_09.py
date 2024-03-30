# Реализуйте функцию saturdays_between_two_dates(),
# которая принимает два аргумента в следующем порядке:
# start — начальная дата, тип date
# end — конечная дата, тип date
# Функция должна возвращать количество суббот между датами start и end включительно.
# Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется, что первая дата меньше второй.
#
# Примечание 2. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию saturdays_between_two_dates(),
# но не код, вызывающий ее.

from datetime import date


def saturdays_between_two_dates(start, end):
    result = [i for i in range(min(start.toordinal(), end.toordinal()), max((end.toordinal() + 1), start.toordinal()+ 1)) if date.fromordinal(i).weekday() == 5]
    return len(result)






date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))