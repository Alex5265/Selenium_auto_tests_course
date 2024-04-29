
from collections import namedtuple
from pympler import asizeof

Person = namedtuple('Person', ['name', 'age', 'height'])

timur = Person('Тимур', 29, 170)
timur_dct = {'name': 'Тимур', 'age': 29, 'height': 170}

print(f'Именованный кортеж: {asizeof.asizeof(timur)} байт')
print(f'Словарь: {asizeof.asizeof(timur_dct)} байт')





# from collections import namedtuple
#
# Device = namedtuple('Device', ['devicetype', 'model'])
#
# device1 = Device(**{'devicetype': 'keyboard', 'model': 'Logitech G213'})
# device2 = Device(*{'devicetype': 'keyboard', 'model': 'Logitech G213'})
#
# print(*device1, sep=', ')
# print(*device2, sep=', ')



# from collections import namedtuple
# from pympler import asizeof
#
# Point = namedtuple("Point", "x y z")
# point = Point(1, 2, 3)
# point_t = (1, 2, 3)
# namedtuple_size = asizeof.asizeof(point)
# dict_size = asizeof.asizeof(point._asdict())
# tuple_size = asizeof.asizeof(point_t)
# gain = 100 - namedtuple_size / dict_size * 100
#
# print(f"namedtuple: {namedtuple_size} bytes ({gain:.2f}% smaller)")
# print(f"dict:       {dict_size} bytes")
# print(f"tuple:      {tuple_size} bytes")



# from collections import namedtuple
# from time import perf_counter
#
# def average_time(structure, test_func):
#     time_measurements = []
#     for _ in range(1_000_000):
#         start = perf_counter()
#         test_func(structure)
#         end = perf_counter()
#         time_measurements.append(end - start)
#     return sum(time_measurements) / len(time_measurements) * int(1e9)
#
# def time_dict(dictionary):
#     "x" in dictionary
#     "missing_key" in dictionary
#     2 in dictionary.values()
#     "missing_value" in dictionary.values()
#     dictionary["y"]
#
# def time_namedtuple(named_tuple):
#     "x" in named_tuple._fields
#     "missing_field" in named_tuple._fields
#     2 in named_tuple
#     "missing_value" in named_tuple
#     named_tuple.y
#
# Point = namedtuple("Point", "x y z")
# point = Point(x=1, y=2, z=3)
#
# namedtuple_time = average_time(point, time_namedtuple)
# dict_time = average_time(point._asdict(), time_dict)
# gain = dict_time / namedtuple_time
#
# print(f"namedtuple: {namedtuple_time:.2f} ns ({gain:.2f}x faster)")
# print(f"dict:       {dict_time:.2f} ns")

