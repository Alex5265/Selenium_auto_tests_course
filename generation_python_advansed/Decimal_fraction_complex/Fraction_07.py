# На вход программе подается натуральное число n.
# Напишите программу, которая находит наибольшую правильную несократимую дробь
# с суммой числителя и знаменателя равной n.


from fractions import Fraction

n = int(input())
my_list = []

for i in range(1, n - 1):
    for j in range(i + 1, n):
        k = Fraction(i, j)
        if k.numerator + k.denominator == n:
            my_list.append(k)

print(max(my_list))