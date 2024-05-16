# Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:
#
# values — список чисел
# group — список, кортеж или множество чисел
# Функция должна сортировать по неубыванию список чисел values,
# делая при этом приоритетной группу чисел из group, которая должна следовать первой.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую
# только необходимую функцию sort_priority(), но не код, вызывающий ее.


#c подсказкой
def sort_priority(numbers, group):
    numbersMax = max(numbers)
    groupMax = max(group)
    numbers.sort(key=lambda x: x if x in group else x + groupMax + numbersMax)



numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers) # [2, 3, 5, 7, 1, 4, 6, 8]

# из решений - мощь

def sort_priority(numbers, group):
    numbers.sort(key=lambda x: (x not in group, x))


