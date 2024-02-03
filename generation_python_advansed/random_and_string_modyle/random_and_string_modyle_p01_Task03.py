# Задачи на модуль рандом.
# Необходимо с помощью модуля написать генератор случайного пароля.
# На вход принимается необходимая длина.
# Состоять должен ТОЛЬКО из больших и маленьких англ. букв.

import random

length = int(input())

for i in range(length):
    x = random.randint(0,1)
    if x:
        print(chr(random.randint(ord('a'), ord('z'))), end='')
    else:
        print(chr(random.randint(ord('A'), ord('Z'))),end='')

