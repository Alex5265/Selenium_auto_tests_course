# Тренировка составления и вывода двоичной КВАДРАТНОЙ матрицы.
# Задание на вход приходят длина стороны и элементы матрицы.
# Необходимо вывести количество чисел, которые больше среднего арифметического в строке

n = int(input())
# В одну строку считываем и вносим в матрицу значения
mart = [[int(num) for num in input().split()] for i in range(n)]

for i in range(len(mart)):
    average = sum(mart[i]) / n
    count_higth = 0
    for j in range(len(mart[i])):
        if mart[i][j] > average:
            count_higth += 1
    print(count_higth)


# 4
# 1 2 3 4
# 5 6 3 15
# 0 2 3 1
# 5 2 8 5

# Должный результат:
# 2
# 1
# 2
# 1
