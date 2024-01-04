# Тренировка составления и вывода двоичной КВАДРАТНОЙ матрицы.
# Задание на вход приходят длина стороны и элементы матрицы.
# Необходимо вывести максимальный элемент в заштрихованной ( правая и левая части при проведении главной и побочной диагонали) области

n = int(input())

matr = [[int (i) for i in input().split()] for j in range(n)]

max_in_area = matr[0][0]

for r in range(n):
    for c in range(n):
        if (r >= c and r <= n - 1 - c) and matr[r][c] > max_in_area:
            max_in_area = matr[r][c]
        elif (r <= c and r >= n - 1 - c) and matr[r][c] > max_in_area:
            max_in_area = matr[r][c]

print(max_in_area)



# 3
# 1 4 5
# 6 7 8
# 1 1 6
# 8 должно быть на выходе