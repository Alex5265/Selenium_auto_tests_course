# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет и выводит рациональное число,
# равное значению выражения

from fractions import Fraction as f
answer = 0
for i in range(1, int(input()) + 1):
    answer += f(1, i ** 2)

print(answer)