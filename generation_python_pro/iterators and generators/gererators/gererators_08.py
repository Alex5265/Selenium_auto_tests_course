# Реализуйте генераторную функцию dates(), которая принимает два аргумента в следующем порядке:
#
# start — дата, тип date
# count — натуральное число, по умолчанию имеет значение None
# Если count имеет значение None, функция должна возвращать генератор,
# порождающий последовательность из максимально допустимого
# количества дат (тип date), начиная с даты start.
#
# Если count имеет в качестве значения натуральное число, функция должна возвращать генератор,
# порождающий последовательность из count дат (тип date), начиная с даты start,
# а затем возбуждающий исключение StopIteration.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую только
# необходимую генераторную функцию dates(), но не код, вызывающий ее.

from datetime import date


def dates(start, count=None):
    if count is None:
        count = -1
    while count:
        try:
            yield start
            start = date.fromordinal(start.toordinal() + 1)
            count -= 1
        except StopIteration:
            return
        except ValueError:
            return






generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
    print(next(generator))
except StopIteration:
    print('Error')


















