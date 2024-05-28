# Реализуйте генераторную функцию filter_names(),
# которая принимает три аргумента в следующем порядке:
#
# names — список имен
# ignore_char — одиночный символ
# max_names — натуральное число
# Функция должна возвращать генератор, порождающий max_names имён из списка names,
# игнорируя имена, которые
#
# начинаются на ignore_char (в любом регистре)
# содержат хотя бы одну цифру
# Если max_names больше количества имен в списке names,
# то генератор должен породить все возможные имена из данного списка.
#
# Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться
# в своем исходном порядке.
#
# Примечание 2. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию filter_names(), но не код, вызывающий ее.



def filter_names(names, ignore_char, max_names):
    clear_char = (i for i in names if not i.lower().startswith(ignore_char.lower()))
    clear_num = (i for i in clear_char if i.isalpha())
    yield from (i for num, i in enumerate(clear_num) if num < max_names)



data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 20))
















