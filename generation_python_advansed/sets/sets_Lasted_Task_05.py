# Методы множеств
# На выход поступают балы по 10 бальной шкале. Поступает 3 строки баллов разделенные пробелами
# необходимо вывести множество оценок третьего ученика, которых нет ни у первого на у второго

set1, set2, set3 = set(input().split()), set(input().split()), set(input().split())

set4 = set3 - (set1 | set2)

print(*sorted(set4, key=int, reverse=True))