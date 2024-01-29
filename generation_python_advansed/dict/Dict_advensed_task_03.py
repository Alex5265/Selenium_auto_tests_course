# Задачи на словари
# На вход приходить 2 фразы. Необходимо понять анаграммы ли они или нет
# (Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово)

dict_1, dict_2 = {}, {}

for i in input().lower():
    if not i.isalpha():
        continue
    dict_1[i] = dict_1.get(i, 0) + 1
for i in input().lower():
    if not i.isalpha():
        continue
    dict_2[i] = dict_2.get(i, 0) + 1

print('YES' if dict_1 == dict_2 else 'NO')

print(dict_1)
print(dict_2)
