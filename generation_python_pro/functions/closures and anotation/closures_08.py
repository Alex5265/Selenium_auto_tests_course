# Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения.
# Она начинается после вопросительного знака и идет до конца адреса. Например:
# https://beegeek.ru?name=timur     # строка запроса: name=timur
# Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:
# https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green
# Реализуйте функцию sourcetemplate(), которая принимает один аргумент:
#
# url — URL адрес
# Функция sourcetemplate() должна возвращать функцию,
# которая принимает произвольное количество именованных аргументов и возвращает url адрес,
# объединенный со строкой запроса, сформированной из переданных аргументов.
# При вызове без аргументов она должна возвращать исходный url адрес без изменений.
#
# Примечание 1. Параметры в строке запроса должны располагаться в лексикографическом порядке ключей.
#
# Примечание 2. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию sourcetemplate(), но не код, вызывающий ее.


def sourcetemplate(url):
    def query(**kwargs):
        if kwargs:
            result = [f'{k}={v}' for k, v in sorted(kwargs.items())]
            return f'{url}?{"&".join(result)}'
        return url
    return query



url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load(name='timur'))



# сторонее решение. заставило переписать собственное.

# def sourcetemplate(url):
#     def inner(**kwargs):
#         l=[f'{key}={value}' for key, value in sorted(kwargs.items())]
#         return url if not kwargs else f'{url}?{"&".join(l)}'
#     return inner

url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))


