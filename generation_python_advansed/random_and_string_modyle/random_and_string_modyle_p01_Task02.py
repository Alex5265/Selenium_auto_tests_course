# Задачи на модуль рандом.
# Необходимо написать моделирование броска кубика
#

import random

n = int(input())

dice = (1, 2, 3, 4, 5, 6)

for i in range(n):
    print(dice[random.randint(0, 5)])
