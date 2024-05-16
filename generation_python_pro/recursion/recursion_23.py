info = {'name': 'Alyson',
        'surname': 'Hannigan',
        'birthday': {'day': 24, 'month': 'March', 'year': 1974},
        'family': {'parents': {'mother': 'Emilie Posner', 'father': 'Alan Hannigan'}}}


def find_key(data, key):
    if key in data:
        return data[key]  # базовый случай

    for v in data.values():
        if type(v) == dict:
            value = find_key(v, key)  # рекурсивный случай
            if value is not None:
                return value



print(find_key(info, 'year'))
print(find_key(info, 'father'))


import sys

limit = sys.getrecursionlimit() # получаем значение максимальной глубины рекурсии

print(limit)

sys.setrecursionlimit(6000) # изменяем максимальное значение глубины рекурсии
new_limit = sys.getrecursionlimit()
print(new_limit)