# В онлайн-школе BEEGEEK мы всегда следим за тем, насколько растет наша
# популярность. Для этого мы собираем публикации из различных соцсетей,
# которые содержат вхождения строки beegeek в нижнем регистре.
# Мы оцениваем публикацию:
# в 3 балла, если она начинается и заканчивается строкой beegeek
# в 2 балла, если она только начинается или только заканчивается строкой beegeek
# в 1 балл, если она содержит строку beegeek только внутри
# в 0 баллов, если она не содержит строку beegeek
# Напишите программу, которая определяет популярность онлайн-школы BEEGEEK
# путем суммирования баллов всех публикаций.
#
# Формат входных данных
# На вход программе подается произвольное число строк,
# каждая из которых представляет очередную публикацию.
#
# Формат выходных данных
# Программа должна определить, во сколько баллов оценивается каждая введенная публикация,
# и вывести сумму всех полученных баллов.
#
# Примечание 1. Если публикация представляет собой просто строку beegeek,
# то она оценивается в 2 балла.
from re import search

balls_3 = r'^(beegeek).*\1$'
balls_2 = r'^(beegeek).*|.*(beegeek)$'
balls_1 = r'.*(beegeek).*'

total = 0

for i in open(0):
    if search(balls_3, i):
        total += 3
    elif search(balls_2, i):
        total += 2
    elif search(balls_1, i):
        total +=1

print(total)
















