# Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу
# заданного размера. При этом (в зависимости от переданных аргументов)
# она должна вести себя так:
# matrix() — возвращает матрицу 1 × 1 в которой единственное число равно нулю;
# matrix(n) — возвращает матрицу n × n, заполненную нулями;
# matrix(n, m) — возвращает матрицу из n строк и m столбцов, заполненную нулями;
# matrix(n, m, value) — возвращает матрицу из n строк и m столбцов, в которой
# каждый элемент равен числу value.
# При создании функции пользуйтесь аргументами по умолчанию.





# По умолчанию задаем значение n как единицу, для условия
# В определении функции невозможно приравнять n к m поэтому None для m
# и значение для матрицы по умолчанию - 0
def matrix(n=1, m=None, value=0):
    if m is None: # если при вызове функции параметр m не задали, то M приравнивается к N
        m = n
    answer = [[value] * m for i in range(n)]
    return answer


print(matrix(3, 4, 9))