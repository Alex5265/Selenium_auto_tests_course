# Реализуйте функцию get_all_values(), которая принимает
# два аргумента в следующем порядке:
#
# chainmap — объект типа ChainMap, элементами которого являются словари
# key — произвольный объект
# Функция должна возвращать множество, элементами которого являются
# все значения по ключу key из всех словарей в chainmap. Если ключ key отсутствует
# в chainmap, функция должна вернуть пустое множество.
#
# Примечание 1. Гарантируется, что передаваемый в функцию объект типа
# ChainMap содержит словари с хешируемыми значениями.
#
# Примечание 2. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию get_all_values(), но не код, вызывающий ее.

from collections import ChainMap

def get_all_values(chainmap, key):
    return {i[key] for i in chainmap.maps if key in i}



chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'name')

print(*sorted(result))


