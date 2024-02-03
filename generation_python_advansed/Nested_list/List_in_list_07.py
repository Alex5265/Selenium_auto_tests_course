# Тренировка вложенных списков.
# Задание повышенной сложности - вывести все возможные подсписки полученных значений

taken_list = input().split()
podspisok_list = [[]]

for r in range(len(taken_list)):
    dop_list = []
    for c in range(len(taken_list)):
        dop_list = taken_list[c:r + c + 1]
        if len(dop_list) == r + 1:
            podspisok_list.append(dop_list)

print(podspisok_list)


# a b c d e f
# На выходе
#  [[], ['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['a', 'b'], ['b', 'c'], ['c', 'd'],
#  ['d', 'e'], ['e', 'f'], ['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e'], ['d', 'e', 'f'],
#  ['a', 'b', 'c', 'd'], ['b', 'c', 'd', 'e'], ['c', 'd', 'e', 'f'], ['a', 'b', 'c', 'd', 'e'],
#  ['b', 'c', 'd', 'e', 'f'], ['a', 'b', 'c', 'd', 'e', 'f']]
