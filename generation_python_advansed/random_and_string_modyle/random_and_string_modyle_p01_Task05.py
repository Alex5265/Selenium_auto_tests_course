# Задачи на модуль рандом.
# Необходимо написать функцию, генерирующую Ip адресс

import random
from random import randrange as R

def generate_ip_try1():
    num = list(range(1, 256))
    ip = [str(i) for i in random.sample(num, 4)]
    return '.'.join(ip)

#еще проще реализация это
def generate_ip_try2():
    return f'{R(256)}.{R(256)}.{R(256)}.{R(256)}'


print(generate_ip_try1())
print(generate_ip_try2())

