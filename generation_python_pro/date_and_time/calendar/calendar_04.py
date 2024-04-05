# Напишите программу, которая определяет количество дней в заданном месяце.
#
# Формат входных данных
# На вход программе подаются год и порядковый номер месяца (начиная с 1), разделенные пробелом.
#
# Формат выходных данных
# Программа должна вывести единственное число — количество дней в введенном месяце.
import calendar

y, m = map(int, input().split())
print(calendar.monthrange(y, m)[-1])














