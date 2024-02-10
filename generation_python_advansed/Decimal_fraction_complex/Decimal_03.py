# Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры
# Decimal числа.


from decimal import *
num = Decimal(input())
x = num.as_tuple()

if num > 1 or num < -1:
    print(max(x.digits) + min(x.digits))
else:
    print(max((*x.digits, 0)) + min((*x.digits, 0)))