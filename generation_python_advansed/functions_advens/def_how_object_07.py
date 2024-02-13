# На вход программе подается строка натуральных чисел.
# Из элементов строки формируется список чисел.
# Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр.
# При этом, если у двух чисел одинаковая сумма цифр, их следует вывести в порядке неубывания.


numbers = input().split()

def sum_sign(number):
    count = 0
    for i in number:
        count += int(i)
    return count
numbers.sort(key=int)
numbers.sort(key=sum_sign)

print(*numbers)

# в отличии от предыдущей задачи сначала сотрируем по int а потом по функции
# т.к. порядок сортировки в питоне стабильны
# то есть гарантирует неизменность взаиморасположения равных между собой элементов


def comparator(n):
    return sum([int(i) for i in str(n)]), n

numbers = [int(i) for i in input().split()]

print(*sorted(numbers, key=comparator))

# очень понравилось решение от автора курса(но я бы его модифицировал как оставил ниже)
# в данном случае принимаются несколько значений с помощью сплита они разбиваются,
# и сразу переводятся в int
# функция компаратор возвращает несколько значений - сумма элементов
# (только тут двойное превращение - число превращается в строку
# а сумма вычисляется перебором и превращением элемента в int)
# упаковывается все в кортеж, где первый знак это сумма,
# а второй это числовое значение и сортировка происходит сначала по первому знаку
# и если они совпадают то по второму

# оптимальнее сделать как ниже без тройных превращений.



# def comparator(n):
#     return sum([int(i) for i in n]), int(n)
#
# numbers = input().split()
#
# print(*sorted(numbers, key=comparator))
