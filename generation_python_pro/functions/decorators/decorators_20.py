# Реализуйте декоратор retry, который принимает один аргумент:
#
# times — натуральное число
# Декоратор должен выполнять повторную попытку вызова декорируемой функции,
# если во время ее выполнения возникает ошибка. Декоратор должен вызывать ее до тех пор,
# пока не исчерпает количество попыток times, после чего должен возбуждать исключение
# MaxRetriesException.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать
# возвращаемое значение декорируемой функции, а также должен уметь декорировать
# функции с произвольным количеством позиционных и именованных аргументов.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только
# необходимый декоратор retry, но не код, вызывающий его.
import functools


class MaxRetriesException(Exception):
    pass


def retry(times):
    def decor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    pass
            raise MaxRetriesException
        return wrapper
    return decor


@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')


beegeek()











