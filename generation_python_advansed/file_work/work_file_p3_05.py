# Вам доступен текстовый файл goats.txt
# в первой строке которого написано слово COLOURS,
# далее идет список всех возможных цветов козлов.
# Затем идет строка со словом GOATS, и далее непосредственно перечисление
# козлов разных цветов. Перечень козлов включает только строки из первого списка.
#
# Напишите программу создания файла answer.txt и вывода в него списка козлов,
# которые удовлетворяют условию загадки от Жака Фреско.
#
# Формат входных данных
# На вход программе ничего не подается.
# Формат выходных данных
# Программа должна создать файл с именем answer.txt и вывести в него
# в алфавитном порядке названия цветов козлов,
# которые удовлетворяют условию загадки Жака Фреско.
#
# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

# открываем файл для чтения другой для записи
with (open('goats_p3_05.txt', 'rt', encoding='utf-8') as goats,
      open('answer_p3_05.txt', 'wt', encoding='utf-8') as answer):
    # решить можно по разному, но через словарь считают оптимальным поэтому
    # циклом фор пропускаю строки до начала перечисления козлов
    for line in goats:
        if line.strip() == 'GOATS':
            break
        else:
            continue
    # создаем словать
    count_goat = {}
    # создаем счетчик
    total_count = 0
    # циклом вносим данные в словарь через гет
    # и получается {цвет козла: количество повторений цвета}
    for line in goats:
        total_count += 1
        count_goat[line.strip()] = count_goat.get(line.strip(), 0) + 1

    # итерируем отсортированный словарь по items
    for k,v in sorted(count_goat.items()):
        # если количество превышает условие
        if v > total_count * 0.07:
            # пишем ключ в файл ответа
            print(k, file=answer)













# Примечание 2. Если бы файл goats.txt содержал строки:
#
# COLOURS
# Pink goat
# Green goat
# Black goat
# GOATS
# Pink goat
# Pink goat
# Black goat
# Pink goat
# Pink goat
# Black goat
# Green goat
# Pink goat
# Black goat
# Black goat
# Pink goat
# Pink goat
# Black goat
# Black goat
# Pink goat
# то файл answer.txt имел бы вид:
#
# Black goat
# Pink goat