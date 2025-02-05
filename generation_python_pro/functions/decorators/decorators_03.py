# Реализуйте декоратор sandwich, который выводит тексты:
#
# ---- Верхний ломтик хлеба ----
# ---- Нижний ломтик хлеба ----
# до и после вызова декорируемой функции соответственно.
#
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое
# значение декорируемой функции, а также должен уметь декорировать функции с произвольным
# количеством позиционных и именованных аргументов.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый
# декоратор sandwich, но не код, вызывающий его.


def sandwich(func):

    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        result = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return result
    return wrapper


@sandwich
def beegeek():
    return 'beegeek'


print(beegeek())

















