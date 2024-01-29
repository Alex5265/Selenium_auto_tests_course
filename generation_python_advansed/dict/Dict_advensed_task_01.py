# Задачи на словари
# На входи приходит количество будующих строк, затем определение специфического термина
# после чего приходит м - количество терминов без определения.
# необходимо вывести определения терминов, если оно отсутствует вывести "Не найдено"

my_list = [[word for word in input().split(':')] for j in range(int(input()))]

definitions = {my_list[i][0].lower(): my_list[i][1].strip() for i in range(len(my_list))}

for _ in range(int(input())):
    finition = input().lower()
    if finition in definitions:
        print(definitions[finition])
    else:
        print("Не найдено")



