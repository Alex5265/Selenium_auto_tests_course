from functools import partial, update_wrapper

def multiply(a, b):
    return a * b

double = partial(multiply, 2)
triple = partial(multiply, 3)


print(double(5))        # 2 * 5
print(triple(10))       # 3 * 10

multiply_two_and_five = partial(multiply, 4, 5)

print(multiply_two_and_five())   # вызываем уже без аргументов


print()
print(int('123'))
print(int('123', base=5))
print(int('1001', base=2))
print(int('A12B', base=16))


basetwo = partial(int, base=2)
print()
print(basetwo('101'))
print(basetwo('1000'))
print(basetwo('11111'))
print()
def pretty_print(text, symbol, count):
    print(symbol * count)
    print(text)
    print(symbol * count)

star_pretty_print = partial(pretty_print, 'Hi!!!', symbol='*')

star_pretty_print(count=7)

print(star_pretty_print.args)
print(star_pretty_print.keywords)

star_pretty_print.func('Исходная функция', symbol='~', count=20)
print()

def multiply(a, b):
    '''Функция перемножает два числа и возвращает вычисленное значение.'''
    return a * b

double = partial(multiply, 2)

print(double.func.__name__)
print(double.func.__doc__)
print()

def multiply(a, b):
    '''Функция перемножает два числа и возвращает вычисленное значение.'''
    return a * b

double = partial(multiply, 2)

update_wrapper(double, multiply)   # копируем информацию из функции multiply в partial объект double

print(double.__name__)
print(double.__doc__)











