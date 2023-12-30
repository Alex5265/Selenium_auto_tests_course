# Тренировка составления и вывода двоичной КВАДРАТНОЙ матрицы.
# Задание на вход приходят длина стороны и элементы матрицы.
# Необходимо вывести максимальный элемент в заштрихованной (нижняя часть главной диагонали) области

n = int(input())

# Принимаем и заполняем матрицу значениями
matr = [[int(i) for i in input().split()] for j in range(n)]

# Создаем переменную заполняя её просто-доступным значением из заштрихованной области
max_in_area = matr[0][0]

# Во вложенном цикле проверяем (по формуле из задания) нахождение значения в нужной области
# и одновременной больше значение в переменной, если все условия совпадают вносим в переменую новое значение
for r in range(n):
    for c in range(n):
        if r >= c and matr[r][c] > max_in_area:
            max_in_area = matr[r][c]

print(max_in_area)
