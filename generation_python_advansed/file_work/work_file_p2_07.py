# Вам доступны два текстовых файла first_names.txt и last_names.txt,
# один с именами, другой с фамилиями.
# Напишите программу, которая c помощью модуля random создает
# 3 случайные пары имя + фамилия, а затем выводит их, каждую на отдельной строке.
# Формат входных данных
# На вход программе ничего не подается.
# Формат выходных данных
# Программа должна вывести текст в формате, приведенном в примере.

import random

with (open('first_names_p2_07.txt', 'rt', encoding='utf-8') as f_name,
      open('last_names_p2_07.txt', 'rt', encoding='utf-8') as l_name):
    name_list = f_name.read().split()
    last_name_list = l_name.read().split()
for i in range(3):
    print(random.choice(name_list), random.choice(last_name_list))













# Примечание 1. Если бы файлы first_names.txt и last_names.txt содержали строки:
#
# Aaron
# Abdul
# Abe
# Abel
# Abraham
# Albert
#
# и
#
# Abramson
# Adamson
# Adderiy
# Addington
# Adrian
# Albertson
# Einstein
# то результатом могло быть:
#
# Abdul Albertson
# Abel Adamson
# Albert Einstein