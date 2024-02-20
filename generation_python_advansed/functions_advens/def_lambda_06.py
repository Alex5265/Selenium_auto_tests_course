# Напишите функцию is_num, используя синтаксис анонимных функций,
# которая принимает строковый аргумент и возвращает значение True,
# если переданный аргумент является числом (целым или вещественным)
# и False в противном случае.


# крайне вымученное решение через лямбду уж лучше обычной функцией.
# проверяем первый символ на знак минус, делаем срез заменив одну точку - если получается число то True
# ИЛИ просто заменяем точку и делаем проверку
is_num = lambda num: (num[0] == '-' and str(num).replace('.', '', 1)[1:].isdigit()) or (str(num).replace('.', '', 1).isdigit())







print(is_num('10.34ab'))# False
print(is_num('10.45'))# True
print(is_num('-18'))# True
print(is_num('-34.67'))# True
print(is_num('987'))# True
print()
print(is_num('abcd'))# False
print(is_num('12345567p'))# False
print(is_num('29.09'))# True
print(is_num('12.3432.89'))# False
print(is_num('0'))########## True
print(is_num('0.003'))# True

print()
print(is_num('0.0'))##True
print(is_num("1-1"))# False
print(is_num('.-95'))# False
print(is_num('a.6'))##False
print()
print(is_num('b1234'))# False
print(is_num('1234p'))# False
print(is_num('12-13-56'))# False
print(is_num('.-95'))# False
print(is_num('--9.34'))# False