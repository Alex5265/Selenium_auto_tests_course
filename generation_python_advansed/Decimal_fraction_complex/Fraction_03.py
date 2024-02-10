# Даны два натуральных числа  m и n. Напишите программу,
# которая сокращает дробь и выводит ее.

from fractions import Fraction as f

m, n = [int(input()) for _ in range(2)]

print(f(m,n))