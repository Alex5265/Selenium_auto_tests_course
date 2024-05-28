def generate_1234():
    yield 1
    yield 2
    yield 3
    yield 4

print(*generate_1234())


def generate_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')

for char in generate_AB():
    print('-->', char)


def counter(low, high):
    for num in range(low, high + 1):
        yield num


counter1 = counter(3, 10)

for i in counter1:
    print(i)

counter2 = counter(100, 103)
print(next(counter2))
print(next(counter2))














