# Реализуйте функцию tabulate(), которая принимает один аргумент:
#
# func — произвольная функция
# Функция tabulate() должна возвращать итератор, генерирующий бесконечную
# последовательность возвращаемых значений функции func сначала с
# аргументом 1, затем 2, затем 3, и так далее.
#
# Примечание 1. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию tabulate(), но не код, вызывающий ее.
import itertools as it


def tabulate(func):
    return map(func, it.count())



func = lambda x: x + 10
values = tabulate(func)

print(next(values))
print(next(values))
print(next(values))












