# Методы множеств
# Необходимо написать код для поступающей строки для каждого элемента встречалось ли данное число раньше

s = input().split()
mega_set = set()
for num in s:
    if int(num) in mega_set:
        print('YES')
    else:
        print('NO')
        mega_set.add(int(num))