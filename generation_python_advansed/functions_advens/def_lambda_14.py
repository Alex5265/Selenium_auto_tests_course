# дана формула её необходимо запихать в лямбда функцию.
# На вход программе на первой строке подаются коэффициенты многочлена,
# разделенные символом пробела и целое число x на второй строке.
# Напишите программу, которая вычисляет значение указанного многочлена
# при заданном значении x.

from functools import reduce
from operator import *


# крайне замудренная формула и плохо воспринимается визуально.
def evaluate(coefficients, x):
    a = [int(i) for i in coefficients.split()]
    n = list(range(len(a)))[::-1]
    result = reduce(add, map(lambda a, n: a * int(x) ** n, a, n))
    return result


print((evaluate(input(), input())))