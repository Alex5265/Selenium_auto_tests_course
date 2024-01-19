# Методы множеств
# Необходимо вывести количество уникальных символов во всех считанных словах

myset = [ set(input().lower()) for i in range(int(input()))]
signs = set()
for el in myset:
    for se in el:
        signs.add(se)

print(len(signs))
