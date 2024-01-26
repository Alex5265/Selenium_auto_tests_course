# Методы словарей
# необходимо написать/дополнить код, объединить 2 словаря с условием, что если ключи есть в обоих
# необходимо добавить в конечный словарь сумму значений повторяющихся ключей.

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}

result.update(dict2)
result.update(dict1)


for el in dict2:
    if (el in dict2) and (el in dict1):
        result[el] = sum((result[el], dict2[el]))

print(result)


#второе решение с меньшим количеством манипуляций
#

result_1 =dict1.copy()
for key, value in dict2.items():
    result_1[key] = result_1.get(key, 0) + value

print(result_1)




