# Тренировка составления и вывода двоичной КВАДРАТНОЙ матрицы.
# Задание на вход приходят длина стороны и элементы матрицы.
# Необходимо назвать сумму элементов главной диагонали

n = int(input())
# В одну строку вносим int в матрицу через сплит строки
matr = [[int(num) for num in input().split()] for i in range(n)]


mat_sum = 0
# значения ряда и столбца у главной диагонали совпадают поэтому в один цикл высчитываем сумму
for i in range(n):
    mat_sum += matr[i][i]

print(mat_sum)


# 3
# 1 2 3
# 4 5 6
# 7 8 9
# 15 должно быть на выходе
