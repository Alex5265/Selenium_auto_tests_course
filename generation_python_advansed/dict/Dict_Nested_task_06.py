# Вложенные словари и генераторы
# Необходимо дополнить код, чтобы преобразовать в словарь список numbers
# ключём должно стать значение элемента, а значением
# отсортированный по возрастанию список всех его делителей начиная с 1
# желательно написать генератор


numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95,
           1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

result = {i: [j for j in range(1, i + 1) if i % j == 0] for i in numbers}

print(result)



# изначальный вариант до написания генератора
# for k in numbers:
#     divaders = []
#     for i in range(1, int(k)+ 1):
#         if int(k) % i == 0:
#             divaders.append(i)
#     result[k] = result.get(k, divaders)
