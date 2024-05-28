# Реализуйте класс RandomNumbers, порождающий итераторы,
# конструктор которого принимает три аргумента в следующем порядке:
#
# left — целое число
# right — целое число
# n — натуральное число
# Итератор класса RandomNumbers должен генерировать последовательность
# из n случайных чисел от left до right включительно, а затем возбуждать исключение StopIteration.
#
# Примечание 1. Гарантируется, что left <= right.
#
# Примечание 2. В тестирующую систему сдайте программу,
# содержащую только необходимый класс RandomNumbers.

import random


class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        self.n -= 1
        return random.randint(self.left, self.right)


iterator = RandomNumbers(1, 10, 2)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))














