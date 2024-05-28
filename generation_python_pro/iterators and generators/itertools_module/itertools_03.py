# Реализуйте функцию alnum_sequence(), которая не принимает никаких аргументов.
#
# Функция должна возвращать итератор, циклично генерирующий
# бесконечную последовательность натуральных чисел и заглавных латинских букв:
# 1,A,2,B,3,C,..,X,25,Y,26,Z
#
# Примечание 1. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию alnum_sequence(), но не код, вызывающий ее.
from itertools import cycle


def alnum_sequence():
    word = (chr(i) for i in range(ord('A'), ord('Z') + 1))
    result = cycle(zip(range(1, 27), word))
    for a, b in result:
        yield a
        yield b




alnum = alnum_sequence()

print(*(next(alnum) for _ in range(100)))














