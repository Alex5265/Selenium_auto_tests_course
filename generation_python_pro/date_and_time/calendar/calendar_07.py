# Реализуйте функцию get_all_mondays(), которая принимает один аргумент:
#
# year — натуральное число
# Функция должна возвращать отсортированный по возрастанию список
# всех дат (тип date) года year, выпадающих на понедельник.
#
# Примечание 1. Например, вызов:
#
# get_all_mondays(2021)
# должен вернуть список:
#
# [datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ...,
# datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]

from datetime import date, datetime, timedelta
import calendar


def get_all_mondays(year):
    result = []
    first_mon = date(year,1,1)
    while first_mon.weekday() != 0:
        first_mon += timedelta(days=1)

    for i in range(first_mon.toordinal(), date(year, 12, calendar.monthrange(year, 12)[-1]).toordinal() + 1, 7):
        result. append(date.fromordinal(i))

    return result


print(get_all_mondays(2021))











