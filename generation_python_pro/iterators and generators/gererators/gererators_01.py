def generate_ints(n):
    for num in range(n):
        yield num




generator1 = generate_ints(5)           # создаем генератор, порождающий числа 0 1 2 3 4

print(type(generator1))

print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))
print()

generator2 = generate_ints(3)           # создаем генератор, порождающий числа 0 1 2

for num in generator2:
    print(num)

num1, num2 = generate_ints(2)           # создаем генератор, порождающий числа 0 1

print(num1, num2)


class GenerateInts:
    def __init__(self, n):  # конструктор принимает верхнюю границу диапазона
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.n:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1




iterator1 = GenerateInts(5)           # создаем итератор, содержащий числа 0 1 2 3 4

print(type(iterator1))

print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print()

iterator2 = GenerateInts(3)           # создаем итератор, содержащий числа 0 1 2

for num in iterator2:
    print(num)

num1, num2 = GenerateInts(2)          # создаем итератор, содержащий числа 0 1

print(num1, num2)















