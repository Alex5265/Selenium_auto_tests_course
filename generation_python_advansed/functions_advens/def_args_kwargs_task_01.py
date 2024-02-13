# Напишите функцию count_args(), которая принимает произвольное количество
# аргументов и возвращает количество переданных в нее аргументов.


# Благодаря синтаксису (знаку *) возможно "слепить" все переданные переменные
# в единый кортеж и производить дальнейшие манипуляции
def count_args(*args):
    return len(args)

print(count_args())
print(count_args(10))
print(count_args('stepik', 'beegeek'))
print(count_args([], (''), 'a', 12, False))