# Реализуйте функцию get_min_max(), которая принимает один аргумент:
#
# iterable — итерируемый объект, элементы которого сравнимы между собой
# Функция должна возвращать кортеж, в котором первым элементом является минимальный
# элемент итерируемого объекта iterable, вторым — максимальный элемент итерируемого объекта iterable.
# Если итерируемый объект iterable пуст, функция должна вернуть значение None.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую только
# необходимую функцию get_min_max(), но не код, вызывающий ее.


def get_min_max(iterable):
    iterable = iter(iterable)
    try:
        inside_min = inside_max = next(iterable)
    except StopIteration:
        return None
    for el in iterable:
        if el < inside_min:
            inside_min = el
        if el > inside_max:
            inside_max = el
    return inside_min, inside_max



iterable = [69]

print(get_min_max(iterable))

iterable = iter(range(10))

print(get_min_max(iterable))

iterable = iter([])

print(get_min_max(iterable))











