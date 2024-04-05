# Напишите программу, которая определяет день недели, соответствующий заданной дате.
#
# Формат входных данных
# На вход программе подается дата в формате YYYY-MM-DD.
#
# Формат выходных данных
# Программа должна вывести полное название дня недели на английском, который соответствует введенной дате.


from datetime import datetime
import calendar


dt = datetime.strptime(input(), '%Y-%m-%d')
print(calendar.day_name[calendar.weekday(dt.year, dt.month, dt.day)])





