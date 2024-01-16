# Основы работы с множествами
# Необходимо дополнить код и в обратном порядке отсотрированные
# по убыванию элементы (в обратном лексикографическом порядке)
#

fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}

sorted_fruit = sorted(fruits, reverse=True)

print(*sorted_fruit, sep='\n')
