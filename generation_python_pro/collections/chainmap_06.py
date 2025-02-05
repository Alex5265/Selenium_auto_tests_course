# Реализуйте функцию get_value(), которая принимает три аргумента в следующем порядке:
#
# chainmap — объект типа ChainMap, элементами которого являются словари
# key — произвольный объект
# from_left — булево значение, по умолчанию равное True
# Функция должна возвращать значение по ключу key из chainmap, причем:
#
# если from_left имеет значение True, поиск ключа в chainmap должен
# происходить от первого словаря к последнему
# если from_left имеет значение False, поиск ключа в chainmap
# должен происходить от последнего словаря к первому
# Если ключ key отсутствует в chainmap, функция должна вернуть значение None.

from collections import ChainMap

def get_value(chainmap, key, from_left=True):
    for item in chainmap.maps if from_left else reversed(chainmap.maps):
        if key in item:
            return item[key]
    return None







