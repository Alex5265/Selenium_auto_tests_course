# Я в аду?
# Напишите программу, которая в заданном тексте находит все телефонные номера, соответствующие следующим форматам:
#
# 7-ddd-ddd-dd-dd
# 8-ddd-dddd-dddd
# где d — цифра от
# 0
# 0 до
# 9
# 9.
#
# Формат входных данных
# На вход программе подается строка произвольного содержания.
#
# Формат выходных данных
# Программа должна в введенном тексте найти все телефонные номера, соответствующие форматам,
# указанным в условии задачи, и вывести их в том порядке,
# в котором они были найдены, каждый на отдельной строке.












def is_phone_number(phone):
    groups = phone.split('-')
    if len(groups) != 4:
        return False
    chars = ''.join(groups)
    return all(c.isdigit() for c in chars)

def get_all_numbers(text):
    for c in range(len(text)):
        chunk = text[c:c + 15]
        regex_7 =r'7-\d\d\d-\d\d\d-\d\d-\d\d'
        if chunk is regex_7:
            yield chunk

txt = 'Перезвони мне, пожалуйста: 7-919-667-21-19'

result = get_all_numbers(txt)

for i in result:
    print(i)