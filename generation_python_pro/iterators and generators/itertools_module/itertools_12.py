# Реализуйте функцию is_rising(), которая принимает один аргумент:
#
# iterable — итерируемый объект, элементами которого являются числа
# Функция должна возвращать True, если элементы итерируемого объекта
# расположены строго по возрастанию, или False в противном случае.
#
# Примечание 1. Гарантируется, что итерируемый объект, передаваемый
# в функцию, не является множеством, а также содержит не менее двух элементов.
#
# Примечание 2. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию is_rising(), но не код, вызывающий ее.
from itertools import pairwise


def is_rising(iterable):
    return all(a < b for a, b in pairwise(iterable))


print(is_rising([1, 2, 3, 4, 5]))


