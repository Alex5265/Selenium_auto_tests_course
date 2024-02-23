# Вам доступен текстовый файл input.txt, состоящий из нескольких строк.
# Напишите программу для записи содержимого этого файла в файл output.txt
# в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и пробел.
# Нумерация строк должна начинаться с 1.
#
# Формат входных данных
# На вход программе ничего не подается.
# Формат выходных данных
# Программа должна создать файл с именем output.txt и записать в него
# пронумерованные строки файла input.txt.
# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
# Примечание 2. Используйте встроенную функцию enumerate().


# открываем один файл для чтения другой для записи именуем как инп и оутпут
with (open('input_p3_03.txt', 'rt', encoding='utf-8') as inp,
      open('output_p3_03.txt', 'w', encoding='utf-8') as output):
    # с помощью функции енумерайт генерируем 2 переменные индекс и сами строки из текста
    for index, line in enumerate(inp, 1):
        print(index, line, file=output, end='')












# Примечание 3. Если бы файл input.txt содержал строки:
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# то файл output.txt имел бы вид:
#
# 1) Beautiful is better than ugly.
# 2) Explicit is better than implicit.
# 3) Simple is better than complex.
# 4) Complex is better than complicated.