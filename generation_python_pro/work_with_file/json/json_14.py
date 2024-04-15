# Вам доступен файл exam_results.csv, который содержит информацию о прошедшем экзамене
# в некотором учебном заведении. В первом столбце записано имя студента, во втором — фамилия,
# в третьем — оценка за экзамен, в четвертом — дата
# и время сдачи в формате YYYY-MM-DD HH:MM:SS, в пятом — адрес электронной почты:
# Каждый студент имеет право пересдать экзамен два раза,
# поэтому он может встречаться в исходном файле до трёх раз
# с различной оценкой и различными датой и временем сдачи.
#
# Напишите программу, которая для каждого студента определяет его максимальную оценку,
# а также дату и время ее получения. Программа должна создать список словарей,
# каждый из которых содержит следующие пары ключ-значение:
#
# name — имя студента
# surname — фамилия студента
# best_score — максимальная оценка за экзамен
# date_and_time — дата и время получения максимальной оценки в исходном формате
# email — адрес электронной почты
# Полученный список программа должна записать в файл best_scores.json,
# причем словари в списке должны быть расположены в лексикографическом порядке названий электронных почт.
#
# Примечание 1. Если при пересдаче студент получил такую же оценку,
# что и в прошлый раз, то в качестве даты следует указать дату пересдачи.
import csv
from datetime import datetime
import json

def to_date(date):
    patern = '%Y-%m-%d %H:%M:%S'
    return datetime.strptime(date, patern)


with open('exam_results.csv', encoding='UTF-8') as file:
    data = csv.DictReader(file)
    best_score = {}

    for row in data:
        key = row['email']
        if key not in best_score  or (to_date(row['date_and_time']) > to_date(best_score[key]['date_and_time']) and int(row['score']) == best_score[key]['best_score']) or int(row['score']) > best_score[key]['best_score']:
            best_score[key] = {
                    'name': row['name'],
                    'surname': row['surname'],
                    'best_score': int(row['score']),
                    'date_and_time': row['date_and_time'],
                    'email': key  # Добавляем ключ 'email' в словарь для полной информации
                }
    result = sorted(best_score.values(), key=lambda x: x.get('email'))

with open('best_scores.json', 'w', encoding='UTF-8') as out:
    json.dump(result, out, indent=3)









