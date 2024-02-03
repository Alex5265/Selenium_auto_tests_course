import copy

n = int(input())
matr_1 = [[int(j) for j in input().split()] for i in range(n)]

rang = int(input())


matr_2 = copy.deepcopy(matr_1)

matr_3 = [[0] * n for i in range(n)]

for d in range(rang - 1):
    matr_3 = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for x in range(n):
                matr_3[i][j] += matr_1[i][x] * matr_2[x][j]

    matr_2 = copy.deepcopy(matr_3)

for i in matr_3:
    print(*i)