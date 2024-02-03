#Задачи на модуль рандом.
# Необходимо написать моделирование броска монеты
#
#

import random

n = int(input())
coin = ('Орел', 'Решка')
for i in range(int(n)):
    print(coin[random.randint(0,1)])




