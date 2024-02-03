# Тренировка математических операций над матрицами.
# Задание на вход поступает n и m количество строк и столбцов
# Необходимо сложить поступившие матрицы.

n, m = [int(i) for i in input().split()]

matr_1 = [[int(i) for i in input().split()] for j in range(n)]

space_input = input()

matr_2 = [[int(i) for i in input().split()] for j in range(n)]


for r in range(n):
    for c in range(m):
        matr_1[r][c] += matr_2[r][c]


for i in matr_1:
    print(*i)
