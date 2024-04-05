# самостоятельно так ине решил. разбор сторонего решения

# Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00.
# Напишите программу, которая принимает на вход текущие дату и время и определяет,
# сколько времени осталось до выхода курса.

from datetime import date, time, datetime, timedelta

def choose_plural(amount, variants): # функция
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and \
            (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    else:
        variant = 2
    return '{} {}'.format(amount, variants[variant])


date_now = datetime.strptime(input(), '%d.%m.%Y %H:%M')
date_x = datetime(2022, 11, 8, 12)

if date_x > date_now:
    delta = date_x - date_now
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds - hours * 3600) // 60
    result = ''
    if days > 0:
        result = choose_plural(days, ('день', 'дня', 'дней'))
        if hours > 0:
            result += ' и ' + choose_plural(hours, (' час', 'часа', 'часов'))
    elif hours > 0:
        result = choose_plural(hours, ('час', 'часа', 'часов'))
        if minutes > 0:
            result += ' и ' + choose_plural(minutes, ('минута', 'минуты', 'минут'))
    else:
        result = choose_plural(minutes, ('минута', 'минуты', 'минут'))
    print('До выхода курса осталось: ' + result)
else:
    print('Курс уже вышел!')