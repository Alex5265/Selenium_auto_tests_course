# Напишите функцию is_non_negative_num, используя синтаксис анонимных функций,
# которая принимает строковый аргумент и возвращает значение True,
# если переданный аргумент является неотрицательным числом (целым или вещественным)
# и False в противном случае.





# is_non_negative_num = lambda num: str(num).count('.') < 2 and str(num).replace('.', '1').isdigit()

is_non_negative_num = lambda num: num.replace('.', '', 1).isdigit()
# изначально намудрил и решал через ор сравнивал коилчество запятых и т.д. (решение закоментировал)
# посмотрел на решение остальных очень оказалось просто и элегантно
# достаточно заменить знак точки на отсутствующий задать что будет делаться один раз
# и затем проверить являются ли значения числами (знак - не пройдет проверку и отрицательные значения отсеятся)




print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))