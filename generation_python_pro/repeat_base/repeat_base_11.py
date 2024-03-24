# Реализуйте функцию get_biggest(), которая принимает один аргумент:
#
# numbers — список целых неотрицательных чисел
# Функция должна возвращать наибольшее число,
# которое можно составить из чисел из списка numbers.
# Если список numbers пуст, функция должна вернуть число −1.
#

# (str(i), i)
def get_biggest(numbers):
    if len(numbers) < 1:
        return -1

    big_len = len(str(max(numbers)))
    result = [str(j) for j in sorted(numbers, key=lambda i: str(i) * big_len, reverse=True)]
    result_str = ''.join(result)
    return int(result_str)


print(get_biggest([7, 71, 72]) == 77271)
print(get_biggest([0, 0, 0, 0, 0, 0]) == 0)
print(get_biggest([]) == -1)
print(get_biggest([72, 7274]) == 727472)
print(get_biggest([62, 626]) == 62662)
print(get_biggest([953, 9534]) == 9539534)
print(get_biggest([262, 26]) == 26262)


x = lambda i: str(i) * 3
y = [7, 71, 72]
result = [ x(i) for i in y]
print(sorted(result, reverse=True))
ord_val = []
for el in result:
    res = []
    for i in el:
        res.append(ord(i))
    ord_val.append(res)

print(ord_val)