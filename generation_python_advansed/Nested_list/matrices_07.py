# Тренировка составления и вывода двоичной КВАДРАТНОЙ матрицы.
# Задание на вход приходят длина стороны и элементы матрицы.
# Необходимо вывести вывести сумму элементов в каждой четверти (диагонали не входят)

n = int(input())

mart = [[int(i) for i in input().split()] for j in range(n)]

sum_up = 0
sum_right = 0
sum_left = 0
sum_down = 0

for r in range(n):
    for c in range(n):
        if r < c and r < n - 1 - c:
            sum_up += mart[r][c]
        elif r < c and r > n - 1 - c:
            sum_right += mart[r][c]
        elif r > c and r < n - 1 - c:
            sum_left += mart[r][c]
        elif r > c and r > n - 1 - c:
            sum_down += mart[r][c]

print(f'''
Верхняя четверть: {sum_up}
Правая четверть: {sum_right}
Нижняя четверть: {sum_down}
Левая четверть: {sum_left}
''')


# 4
# 1 2 3 4
# 5 6 7 8
# 3 4 5 6
# 1 2 3 4
# На выходе:
# Верхняя четверть: 5
# Правая четверть: 14
# Нижняя четверть: 5
# Левая четверть: 8
#