# Тренировка вложенных списков.
# Задание (желательно написать функцию) возвращающая полностью ТРЕУГОЛЬНИК ПАСКАЛЯ

n = int(input())
mylist = []

for i in range(n):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            x = mylist[i - 1][j - 1]
            y = mylist[i - 1][j]
            row[j] = x + y

    mylist.append(row)


for el in mylist:
    print(*el)