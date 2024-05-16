# Реализуйте функцию random_numbers(), которая принимает два аргумента:
#
# left — целое число
# right — целое число
# Функция должна возвращать итератор, генерирующий бесконечную последовательность
# случайных целых чисел в диапазоне от left до right включительно.
#
# Примечание 1. Гарантируется, что left <= right.
#
# Примечание 2. В тестирующую систему сдайте программу,
# содержащую только необходимый итератор random_numbers(), но не код, вызывающий его.
import random


def random_numbers(left, right):
    res = random.randint(left, right)
    return iter(lambda: res, (right + 2))


iterator = random_numbers(1, 20)


print(next(iterator))













