# Методы множеств
# Необходимо написать код для поступающих 2ух строк и
# вывести все числа в порядке возрастания в первой и второй строке


set_1, set_2 = set(int(i) for i in input().split()), set(int(i) for i in input().split())
set_3 = set_1 & set_2
mylist = list(set_3)
print(*sorted(mylist))

