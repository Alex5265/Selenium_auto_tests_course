# Вложенные словари и генераторы
# Необходимо дополнить код, чтобы из словаря months
# в новом словаре ключ и значения поменялись местами
# желательно написать генератор

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7:
    'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

result = {v: k for k, v in months.items()}

print(result)