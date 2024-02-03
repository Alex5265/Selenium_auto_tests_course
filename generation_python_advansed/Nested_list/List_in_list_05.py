n = int(input())

triange = []

for i in range(n + 1):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(triange[i - 1][j - 1] + triange[i - 1][j])
    triange.append(row)



for c in triange:
    print(c)