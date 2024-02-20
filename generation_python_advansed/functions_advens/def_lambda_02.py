# Напишите программу, которая с помощью встроенных
# функций filter(), map(), sorted() и reduce()
# выводит в алфавитном порядке список primary городов с населением более
# 10 000 000 человек, в формате:
#
# Cities: Beijing, Buenos Aires, ...

from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]


# согласно условиям сначала используем фильтр. дата - вложеный список со стандартизированными полями.
# в лямда задаем что город (это всегда второй вложенный параметр)
# должен быть примари
# и население(первый параметр) больше обозначенного условия
result = list(filter(lambda x: x[2] == 'primary' and x[1] > 10 ** 7, data))
#после фильтрации сохраняем только название городов (нулевое значение)
result = list(map( lambda x: x[0], result))
# сортируем города в алфавитном порядке
result = sorted(result)
# используем reduce(вместо простого join) чтобы соединить название городов в единую строку
result = 'Cities: ' + reduce(lambda x, y: f'{x}, {y}', result)

print(result)