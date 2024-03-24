# Реализуйте функцию convert(), которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна возвращать строку string:
#
# полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
# полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
# полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает
# Примечание 1. Символы строки, не являющиеся буквами, следует игнорировать.




def convert(string):
    lower_count = len(list(filter(str.islower, string)))
    upper_count = len((list(filter(str.isupper, string))))
    if lower_count >= upper_count:
        return string.lower()
    return string.upper()



print(convert('BEEgeek'))
# beegeek
print()

print(convert('pyTHON'))
# PYTHON

# сторонее решение красивое
# def convert(string):
#     if sum(1 if c.isupper() else -1 for c in string if c.isalpha()) > 0:
#         return string.upper()
#     return string.lower()




