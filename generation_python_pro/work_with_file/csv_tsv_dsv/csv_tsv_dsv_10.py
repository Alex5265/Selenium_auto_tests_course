# Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя.
# В первом столбце записано измененное имя пользователя, во втором — адрес электронной почты,
# в третьем — дата и время изменения. При этом email пользователь менять не может, только имя:
#
# username,email,dtime
# rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
# busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
# ...
# Напишите программу, которая отбирает из файла name_log.csv только
# самые свежие записи для каждого пользователя и записывает их в файл new_name_log.csv.
# В файле new_name_log.csv первой строкой должны быть заголовки столбцов такие же, как
# в файле name_log.csv. Логи в итоговом файле должны быть расположены в лексикографическом
# порядке названий электронных ящиков пользователей.
#
# Примечание 1. Для части пользователей в исходном файле запись только одна,
# и тогда в итоговый файл следует записать только ее, для некоторых пользователей есть
# несколько записей с разными именами.
#
# Например, пользователь с электронной почтой c3po@gmail.com несколько раз менял имя:
#
# C=3PO,c3po@gmail.com,16/11/2021 17:10
# C3PO,c3po@gmail.com,16/11/2021 17:15
# C-3PO,c3po@gmail.com,16/11/2021 17:24
# Из этих трех записей в итоговый файл должна быть записана только одна — самая свежая:
#
# C-3PO,c3po@gmail.com,16/11/2021 17:24
from datetime import datetime
import csv

pattern = '%d/%m/%Y %H:%M'

with open('name_log.csv', encoding='UTF-8') as file, open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as writer:
    result = {}
    data = csv.reader(file)
    headers = next(data)
    for i in data:
        name, mail, dait = i
        if mail not in result or result[mail][-1] < dait:
            result[mail] = [name, dait]

    write = csv.writer(writer)
    write.writerow(headers)
    for k, v in sorted(result.items()):
        write.writerow((v[0], k, v[-1]))






