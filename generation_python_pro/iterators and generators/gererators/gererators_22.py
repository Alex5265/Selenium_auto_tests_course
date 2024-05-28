# Реализуйте генераторную функцию years_days(), которая принимает один аргумент:
#
# year — натуральное число
# Функция должна возвращать генератор, порождающий последовательность всех дат (тип date) в году year.
#
#
# Примечание 2. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию years_days(), но не код, вызывающий ее.

from datetime import date


def years_days(year):
    yield from (date.fromordinal(day) for day in range(date(year,1,1).toordinal(), date((year+ 1),1,1).toordinal()))


dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))















