# Реализуйте функцию custom_sort(), которая принимает два аргумента в следующем порядке:
#
# ordered_dict — словарь OrderedDict
# by_values — булево значение, по умолчанию имеет значение False
# Функция должна сортировать словарь ordered_dict:
#
# по ключам, если by_values имеет значение False
# по значениям, если by_values имеет значение True
# Примечание 1. Функция должна изменять переданный словарь,
# а не возвращать новый. Возвращаемым значением функции должно быть None.
#
# Примечание 2. Гарантируется, что переданный в функцию словарь можно отсортировать,
# то есть он не содержит ключи, имеющие разные типы, а также значения, имеющие разные типы.
#
# Примечание 3. Если два элемента имеют равные значения,
# то следует сохранить их исходный порядок следования.
#
# Примечание 4. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию custom_sort(), но не код, вызывающий ее.
#
# Примечание 5. Тестовые данные доступны по ссылкам:

from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    if not by_values:
        for key in sorted(ordered_dict):
            ordered_dict.move_to_end(key)
    else:
        for key in sorted(ordered_dict, key=lambda x: ordered_dict[x]):
            ordered_dict.move_to_end(key)



data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)

data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)

print(*data.items())

