# Методы множеств
# Необходимо вывести количество уникальных символов каждого слова без учета регистра

my_li = [ input().lower() for i in range(int(input()))]

for el in my_li:
    print(len(set(el)))

print(my_li)

