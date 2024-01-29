# Задачи на словари
# На вход приходить число и количество слов синонимов разделеных проблемом
# После чего приходит слово на которое необходимо вывести синоним.

sinonim = {}

for _ in range(int(input())):
    key, value = input().split()
    sinonim[key] = value
    sinonim[value] = key

print(sinonim[input()])


# 4
# Awful Terrible
# Beautiful Pretty
# Great Excellent
# Generous Bountiful
#Pretty
# НА выходе
# Beautiful
#
#
#
#
#
#
#
#
# Сторонее решение не через удвоение словаря а с помощью поиска в значениях и в ключях

d = {i[0]: i[1] for i in [input().split() for _ in range(int(input()))]}
word = input()
for key, value in d.items():
    if value == word:
        print(key)
    elif key == word:
        print(value)


