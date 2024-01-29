# Задачи на словари
# На вход приходить 2 строки. Необходимо понять анаграммы ли они или нет
# (Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово)


dict1, dict2 = {}, {}
for i in input():
    dict1[i] = dict1.get(i, 0) + 1
for i in input():
    dict2[i] = dict2.setdefault(i, 0) + 1
print('YES' if dict1 == dict2 else 'NO')



# thing
# night
# На выходе
# YES
#
# cat
# rat
# На выходе
# NO
#
#

