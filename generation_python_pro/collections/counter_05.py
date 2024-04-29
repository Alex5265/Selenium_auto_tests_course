# Вам доступен текстовый файл pythonzen.txt, содержащий текст на английском языке:
#
# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# ...
# Напишите программу, которая определяет, сколько раз встречается каждая буква в этом тексте.
# Буквы и их количество должны выводиться в лексикографическом порядке, каждая на отдельной строке, в следующем формате:
#
# <буква>: <количество>
# Примечание 1. Начальная часть ответа выглядит так:
#
# a: 53
# b: 21
# ...
# Примечание 2. Программа не должна учитывать регистр, то есть, например, буквы a и A считаются одинаковыми.
# Примечание 3. Программа должна игнорировать все небуквенные символы.
from collections import Counter

result = Counter()

with open('pythonzen.txt') as file:
    for row in file:
        result.update(filter(str.isalpha, row.lower()))

    for k, v in sorted(result.items()):
        print(f'{k}: {v}')











