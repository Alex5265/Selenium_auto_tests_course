# Реализуйте генераторную функцию reverse(), которая принимает один аргумент:
#
# sequence — последовательность
# Функция должна возвращать генератор, порождающий элементы последовательности
# sequence в обратном порядке, а затем возбуждающий исключение StopIteration.
#
# Примечание 1. Последовательностью является коллекция, поддерживающая
# индексацию и имеющая длину. Например, объекты типа list, str, tuple являются последовательностями.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую
# только необходимую генераторную функцию reverse(), но не код, вызывающий ее.


def reverse(sequence):
    for i in range(len(sequence) - 1, -1, -1):
        yield sequence[i]


generator = reverse('beegeek')

print(type(generator))
print(*generator)






