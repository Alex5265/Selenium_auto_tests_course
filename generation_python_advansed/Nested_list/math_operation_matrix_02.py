

n, m_1 = [int(i) for i in input().split()]
matr_1 = [[int(j) for j in input().split()] for i in range(n)]

space = input()

m_2, k = [int(i) for i in input().split()]
matr_2 = [[int(j) for j in input().split()] for i in range(m_2)]

matr_3 = [[0] * n for i in range(k)]

for i in range(n):
    for j in range(k):
        for x in range(m_1):
            matr_3[i][j] += matr_1[i][x] * matr_2[x][j]

for i in matr_3:
    print(*i)