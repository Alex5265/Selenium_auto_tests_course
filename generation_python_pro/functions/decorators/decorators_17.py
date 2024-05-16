# Реализуйте декоратор takes, который принимает произвольное количество
# позиционных аргументов, каждый из которых является типом данных.
#
# Декоратор должен проверять, что аргументы, передаваемые в декорируемую функцию,
# принадлежат одному из этих типов. Если хотя бы один аргумент не принадлежит одному
# из данных типов, декоратор должен возбуждать исключение TypeError.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать
# возвращаемое значение декорируемой функции, а также должен уметь декорировать
# функции с произвольным количеством позиционных и именованных аргументов.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только
# необходимый декоратор takes, но не код, вызывающий его.
import functools


def takes(*decargs):
    def decor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for el in (*args, *kwargs.values()):
                if not isinstance(el, decargs):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return decor




@takes(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)

try:
    print(append_this([1, 2], [3, 4]))
except TypeError as e:
    print(type(e))







