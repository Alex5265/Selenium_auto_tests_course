# Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:
#
# funcs — список произвольных функций
# arg — произвольный объект
# Функция get_the_fastest_func() должна возвращать функцию из списка funcs,
# которая затратила на вычисление значения при вызове с аргументом arg наименьшее количество времени.
import time


def get_the_fastest_func(funcs, arg):
    result = []
    for func in funcs:
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        result.append((func, end - start))

    answer = min(result, key=lambda x: x[-1])

    return result


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)

funcs = [for_and_append, list_comprehension, list_function]

print(get_the_fastest_func(funcs, range(100_000)))













