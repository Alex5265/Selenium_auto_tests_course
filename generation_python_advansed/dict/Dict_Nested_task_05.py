# Вложенные словари и генераторы
# Необходимо дополнить код, чтобы из словаря s
# в новом словаре ключ и значения поменялись местами при этом числа должны быть типа int
# желательно написать генератор

s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

my_lst = [i.split(':') for i in s.split()]
result = {int(k): v for k, v in [i.split(':') for i in s.split()]}


print(result)



# Так же вариант решения из комментариев
# result = {int(k): v for i in s.split() for k, v in [i.split(':')]}

# изначально решил через фор чтобы написать генератор
# for i in s.split():
#        k, v = i.split(':')
#        result[int(k)] = v



