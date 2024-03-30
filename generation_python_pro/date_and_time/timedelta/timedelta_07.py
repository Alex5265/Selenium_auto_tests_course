# Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:
#
# year — натуральное число, год
# Функция должна возвращать количество воскресений в году year.
#
# Примечание 1. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию num_of_sundays(),
# но не код, вызывающий ее.

from datetime import date


def num_of_sundays(year):
    result = [i for i in range(date(year,1,1).toordinal(), (date(year + 1,1,1)).toordinal()) if date.fromordinal(i).weekday() == 6]
    return len(result)



print(num_of_sundays(2021))

year = 2000
print(num_of_sundays(year))


# сторонее решение. %U - показывает то что надо -
# Номер недели в году (неделя начинается с воскр.).Неделя,
# предшествующая первому воскресенью, является нулевой. [00, …, 53]
# from datetime import datetime
#
# def num_of_sundays(year):
#     dt = datetime(year, 12, 31)
#     return int(dt.strftime('%U'))