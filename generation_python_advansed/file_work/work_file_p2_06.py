# Вам доступен текстовый файл file.txt, набранный латиницей.
# Напишите программу, которая выводит количество букв латинского алфавита,
# слов и строк. Выведите три найденных числа в формате, приведенном в примере.
# Формат входных данных
# На вход программе ничего не подается.
# Формат выходных данных
# Программа должна вывести три найденных числа в формате, приведенном в примере.



# открываем файл в режиме чтения
with open('file_p2_06.txt', 'rt', encoding='utf-8') as file:
    # создаем необходимые переменные
    letters, words, lines = 0, 0, 0
    # циклом фор ходим построчно
    for line in file:
        # сразу запускаем прибавление линий
        lines += 1
        # запускаем новый цикл для слов разбивая линию сплитом
        for word in line.split():
            # запускаем счетчик слов
            words += 1
            # единственная сложность это буквы = через фильтр и join очищаем каждое слово
            # от НЕ букв и сумируем в переменной
            letters += len(''.join(filter(str.isalpha, word)))

# с помощью Ф строк выводим на печать в необходимом формате.
print(f'Input file contains:\n'
      f'{letters} letters\n'
      f'{words} words\n'
      f'{lines} lines\n')




# Примечание 1. Если бы файл file.txt содержал строки:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# то результатом было бы:
#
# Input file contains:
# 108 letters
# 20 words
# 4 lines