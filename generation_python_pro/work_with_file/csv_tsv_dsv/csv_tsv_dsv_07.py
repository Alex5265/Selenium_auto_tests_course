# Вам доступен файл data.csv, который содержит неповторяющиеся данные
# о пользователях некоторого ресурса.
# В первом столбце записано имя пользователя,
# во втором — фамилия, в третьем — адрес электронной почты:
#
# first_name,surname,email
# John,Wilson,johnwilson@outlook.com
# Mary,Wilson,marywilson@list.ru
# ...
# Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:
#
# domain,count
# rambler.ru,24
# iCloud.com,29
# ...
# где в первом столбце записано название почтового домена,
# а во втором — количество пользователей, использующих данный домен.
# Домены в файле должны быть расположены в порядке возрастания количества их использований,
# при совпадении количества использований — в лексикографическом порядке.
#
# Примечание 1. Разделителем в файле data.csv является запятая,
# при этом кавычки не используются.
import csv


def count_domain(file_name, column_name, create_file):
    with open(file_name, encoding='UTF-8') as file, open(create_file, 'w', encoding='UTF-8', newline='') as create:
        d = {}
        data = csv.reader(file)
        next(data)
        for *_, email in data:
            domain = email.split('@')[-1]
            d[domain] = d.get(domain, 0) + 1

        writer = csv.writer(create)
        writer.writerow(column_name)
        for crow in sorted(d.items(), key=lambda x: (x[1], x[0])):
            writer.writerow(crow)




column = ['domain', 'count']
count_domain('data.csv', column, 'domain_usage.csv')


















