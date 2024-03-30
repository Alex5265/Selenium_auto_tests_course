# Вам доступен текстовый файл diary.txt,
# в который космонавт записывал небольшие отчёты за день.
# Каждый новый отчёт он мог записать либо в начало файла, либо в середину, либо в конец.
# Все отчеты разделены между собой пустой строкой.
# Каждый новый отчёт начинается со строки с датой и временем в формате DD.MM.YYYY; HH:MM,
# после которой следуют события, произошедшие за указанный день:

from datetime import datetime


pises = []
with open('diary.txt', 'r', encoding='UTF-8') as file:
    pises.extend(file.read().split('\n\n'))

pises = sorted(pises, key=lambda dt: datetime.strptime(dt[:17], '%d.%m.%Y; %H:%M'))

print(*pises, sep='\n\n')















