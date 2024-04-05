# Напишите программу, которая определяет количество дней в заданном месяце.
#
# Формат входных данных
# На вход программе подаются год и полное название месяца на английском, разделенные пробелом.
#
# Формат выходных данных
# Программа должна вывести единственное число — количество дней в введенном месяце.

from datetime import datetime
import calendar


dt = datetime.strptime(input(), '%Y %B')

print(calendar.monthrange(dt.year, dt.month)[-1])







