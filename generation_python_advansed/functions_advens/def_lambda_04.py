# Напишите функцию func, используя синтаксис анонимных функций,
# которая принимает строковый аргумент и возвращает значение True,
# если переданный аргумент начинается и заканчивается на английскую букву a
# (регистр буквы неважен) и False в противном случае.


# в данном варианте решил реализовать с помощью конвертации в строку,
# приведения к прописным закам и проверке с помощью функции "начинается с" и "кончается с "
func = lambda x: str(x).lower().startswith('a') and str(x).lower().endswith('a')

# другой вариант через срезы проверяем что строка и срезы прописные равны аа
func_1 = lambda x: isinstance(x, str) and (x[0] + x[-1]).lower() == 'aa'




#проверочные условия
print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))

print()

print(func_1('abcd'))
print(func_1('bcda'))
print(func_1('abcda'))
print(func_1('Abcd'))
print(func_1('bcdA'))
print(func_1('abcdA'))