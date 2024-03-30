# Реализуйте функцию is_correct(), которая принимает три аргумента в следующем порядке:
#
# day — натуральное число, день
# month — натуральное число, месяц
# year — натуральное число, год
# Функция должна возвращать True, если дата с компонентами day,
# month и year является корректной, или False в противном случае.
#
# Примечание 1. Вспомните про конструкцию try-except.
#
# Примечание 2. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию is_correct(), но не код, вызывающий ее.

from datetime import date

def is_correct(day, month, year):
    try:
        date(int(year), int(month), int(day))
        return True
    except ValueError:
        return False








print(is_correct(31, 12, 2021))
print(is_correct(31, 13, 2021))










