import re

# Чтение входных данных
slice_range = list(map(int, input().split()))
text = input()

# Выбор подстроки по заданному диапазону
text = text[slice_range[0]: slice_range[1]]

# Поиск всех натуральных чисел в подстроке
numbers = re.findall(r'\d+', text)

# Суммирование чисел
result = sum(int(num) for num in numbers)

print(result)



