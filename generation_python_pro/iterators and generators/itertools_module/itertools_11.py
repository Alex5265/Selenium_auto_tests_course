# Реализуйте функцию sum_of_digits(), которая принимает один аргумент:
#
# iterable — итерируемый объект, элементами которого являются натуральные числа
# Функция должна возвращать единственное число — сумму цифр всех чисел, присутствующих в итерируемом объекте iterable.
#
# Примечание 1. Рассмотрим набор чисел
# 13,20,41,2,2,5 из первого теста. Сумма цифр всех представленных чисел будет равна:
# 1+3+2+0+4+1+2+2+5=20
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию sum_of_digits(), но не код, вызывающий ее.
from itertools import chain


def sum_of_digits(iterable):
    strings = map(str, iterable)
    all_elements = chain.from_iterable(strings)
    int_digits = map(int, all_elements)
    return sum(int_digits)



print(sum_of_digits([13, 20, 41, 2, 2, 5]))