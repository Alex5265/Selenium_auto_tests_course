def even_numbers(begin):
    begin += begin % 2
    while True:
        yield begin
        begin += 2


evens1 = even_numbers(10)                     # все четные числа от 10 до бесконечности

for index, num in enumerate(evens1):
    if index > 15:
        break
    print(num)

evens2 = even_numbers(101)                    # все четные числа от 102 до бесконечности

print(next(evens2))
print(next(evens2))
print(next(evens2))
print(next(evens2))


def string_wrapper(text, symbol):
    for char in text:
        yield symbol + char + symbol


string_wrapper1 = string_wrapper('beegeek', '~')

for char in string_wrapper1:
    print(char)

string_wrapper2 = string_wrapper('Python', '+')
print(next(string_wrapper2))
print(next(string_wrapper2))
print(next(string_wrapper2))

print(list(string_wrapper('stepik', '-')))



def factorials():
    value = 1
    index = 1
    while True:
        yield value
        index += 1
        value *= index


infinite_factorials = factorials()

for index, num in enumerate(infinite_factorials, 1):
    if index <= 10:
        print(f'Факториал числа {index} равен {num}')


































