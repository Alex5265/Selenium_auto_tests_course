# Методы множеств
# На выход поступают 2 числа необходимо определить входят ли в запись первого числа все цифры из второго

set1 = set(input())
set2 = set(input())

if set2.issubset(set1):
    print('YES')
else:
    print('NO')


# print(("YES", "NO")[set(input()).issubset(input())])