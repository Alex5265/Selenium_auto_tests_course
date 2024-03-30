# Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.
#
# Формат входных данных
# На вход программе подаются две корректные даты в ISO формате (YYYY-MM-DD), каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна выбрать из двух введенных дат меньшую и вывести ее в формате DD-MM (YYYY).

from datetime import date


def take_mini_date():
    result = min(date.fromisoformat(input()) for i in range(2))
    return result.strftime('%d-%m (%Y)')


print(take_mini_date())
