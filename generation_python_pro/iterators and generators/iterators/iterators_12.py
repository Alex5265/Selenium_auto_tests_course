# Реализуйте функцию is_iterator(), которая принимает один аргумент:
#
# obj — произвольный объект
# Функция должна возвращать True, если объект obj является итератором, или False в противном случае.
#
# Примечание 1. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию is_iterator(), но не код, вызывающий ее.


def is_iterator(obj):
    return '__next__' in dir(obj)






print(is_iterator([1, 2, 3, 4, 5]))
beegeek = map(str.upper, 'beegeek')

print(is_iterator(beegeek))



