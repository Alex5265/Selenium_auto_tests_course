# Напишите функцию mean(), которая принимает произвольное количество аргументов и
# возвращает среднее арифметическое переданных в нее числовых (int или float) аргументов.


# задание аналогично - благодаря синтаксису принимаем любое количество аргументов
# и перебирая типы каждого значения высчитывает сумму и количество элементов
def mean(*args):
    count = 0
    sum_args = 0
    for el in args:
        if type(el) in [int, float]:
            sum_args += el
            count += 1
    if count == 0:
        return float(0)
    return sum_args / count








print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))