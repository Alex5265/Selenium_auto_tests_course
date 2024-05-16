class EvenNumbers:
    def __init__(self, begin):  # конструктор принимает один аргумент begin (помимо self)
        self.begin = begin + begin % 2

    def __iter__(self):
        return self

    def __next__(self):
        value = self.begin
        self.begin += 2
        return value


evens1 = EvenNumbers(10)                     # все четные числа от 10 до бесконечности

for index, num in enumerate(evens1):
    if index > 5:
        break
    print(num)

print()
evens2 = EvenNumbers(101)                    # все четные числа от 102 до бесконечности
print(evens2.__dict__)
print(next(evens2))
print(next(evens2))
print(next(evens2))
print(next(evens2))



