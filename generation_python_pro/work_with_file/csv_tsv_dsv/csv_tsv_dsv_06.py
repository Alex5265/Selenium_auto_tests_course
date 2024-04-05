# Реализуйте функцию csv_columns(), которая принимает один аргумент:
#
# filename — название csv файла, например, data.csv
# Функция должна возвращать словарь, в котором ключом является название столбца файла filename,
# а значением — список элементов этого столбца.
#
# Примечание 1. Гарантируется, что в передаваемом в функцию файле разделителем является запятая,
# при этом кавычки не используются.
#
# Примечание 2. Гарантируется, что у передаваемого в функцию файла первая строка содержит названия столбцов.
#
# Примечание 3. Например, если бы файл exam.csv имел вид:
#
# name,grade
# Timur,5
# Arthur,4
# Anri,5
# то следующий вызов функции csv_columns():
#
# csv_columns('exam.csv')
# должен был бы вернуть:
#
# {'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}
# Примечание 4. Ключи в словаре, а также элементы в списках должны располагаться в своем исходном порядке.
#
# Примечание 5. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию csv_columns(), но не код, вызывающий ее.
import csv


def csv_columns(filename):
    d = {}
    with open(filename, encoding='UTF-8') as file:
        data = csv.DictReader(file)
        for i in data:
            for j in i:
                d[j] = d.get(j, []) + [i[j]]

    return d



# крайне красивое сторонее решение зип превращает строки в столбцы

# import csv
#
# def csv_columns(filename):
#
#     with open(filename, encoding="utf-8") as file_in:
#         rows = list(csv.reader(file_in))
#         return {key: value for key, *value in zip(*rows)}



text = '''name,grade
Timur,5
Arthur,4
Anri,5'''

with open('grades.csv', 'w') as file:
    file.write(text)

print(csv_columns('grades.csv'))








