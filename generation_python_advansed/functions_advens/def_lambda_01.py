# Требовалось написать программу, которая:
#
# преобразует список floats в список чисел, возведенных в квадрат и
# округленных с точностью до одного десятичного знака;
# фильтрует список words  и оставляет только палиндромы длиной более 4 символов;
# находит произведение чисел из списка numbers.
# Программист торопился и написал программу неправильно. Доработайте его программу.



from functools import reduce

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun',
         'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправлена лямбда функция - отсутствовал квадрат числа. и округление до 1 знака
map_result = list(map(lambda num: round(num**2, 1), floats))
# в лямда функции отсутсовали условия о длине слова. полиндром проверяется не оптимальным способом, но единственным способом для условий
filter_result = list(filter(lambda name: len(name) > 4 and name == name[::-1], words))
# вместо произведения было сложение. Убрал начальное значение т.к. условие лямды простое
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)

print(map_result)
print(filter_result)
print(reduce_result)



# изначально данно :
#  from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: num, floats))
# filter_result = list(filter(lambda name: name, words))
# reduce_result = reduce(lambda num1, num2: num1 + num2, numbers, 0)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)
#
