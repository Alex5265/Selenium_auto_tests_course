# Даны две дроби в формате a/b.
# Напишите программу, которая вычисляет и выводит их
# сумму, разность, произведение и частное.

from fractions import Fraction

m, n = [(input()) for _ in range(2)]

for i in '+-*/':
    print(f'{m} {i} {n} = {eval(f"Fraction(m){i}Fraction(n)")}')

# from fractions import Fraction
#
# x, y = input(), input()
# for op in '+-*/':
#     print(f'{x} {op} {y} = {eval(f"Fraction(x){op}Fraction(y)")}')


# print(f'{m} + {n} = {f(m) + f(n)}')
# print(f'{m} - {n} = {f(m) - f(n)}')
# print(f'{m} * {n} = {f(m) * f(n)}')
# print(f'{m} / {n} = {f(m) / f(n)}')