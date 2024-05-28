# Реализуйте функцию first_true(), которая принимает
# два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# predicate — функция-предикат; если имеет значение None,
# то работает аналогично функции bool()
# Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable, для которого функция predicate вернула значение True. Если такого элемента нет, функция first_true() должна вернуть значение None.
#
# Примечание 1. Предикат — это функция, которая возвращает
# True или False в зависимости от переданного в качестве аргумента значения.
#
# Примечание 2. Гарантируется, что итерируемый объект,
# передаваемый в функцию, не является множеством.
from itertools import islice

def first_true(iterable, predicate=None):
    x = islice(filter(predicate, iterable), 1)
    return next(x, None)



numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 0, 10, 100, 200)
numbers_iter = filter(None, numbers)

print(first_true(numbers_iter, lambda num: num < 0))















