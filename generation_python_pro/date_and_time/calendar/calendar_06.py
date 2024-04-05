# Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:
#
# year — натуральное число
# month — полное название месяца на английском
# Функция должна возвращать отсортированный по возрастанию список
# всех дат (тип date) месяца month и года year.
#
# Примечание 1. Например, вызов:
#
# get_days_in_month(2021, 'December')
# должен вернуть список:
#
# [datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ...,
# datetime.date(2021, 12, 30), datetime.date(2021, 12, 31)]

from datetime import date, datetime
import calendar


def get_days_in_month(year, month):
    result = []
    m = datetime.strptime(month, '%B')
    for el in range(date(year, m.month, 1).toordinal(), date(year, m.month, calendar.monthrange(year, m.month)[-1]).toordinal() + 1):
        result.append(date.fromordinal(el))
    return result




print(get_days_in_month(1982, 'January'))





