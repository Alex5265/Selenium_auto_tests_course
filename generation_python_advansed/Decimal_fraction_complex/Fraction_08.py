# На вход программе подается натуральное число n.
# Напишите программу, которая выводит в порядке возрастания все несократимые дроби,
# заключённые между 0 и 1, знаменатель которых не превосходит n.


from fractions import Fraction

n = int(input())
my_list = []

for i in range(1, n):
    for j in range(i + 1, n + 1):
        k = Fraction(i, j)
        my_list.append(k)

print(*sorted(set(my_list)), sep='\n')