# Реализуйте функцию get_weekday(), которая принимает один аргумент:
#
# number — целое число (от 1 до 7 включительно)
# Функция должна возвращать полное название дня недели на русском,
# который соответствует числу number, при этом:
#
# если number не является целым числом, функция должна возбуждать исключение:
# TypeError('Аргумент не является целым числом')
# если number является целым числом, но не принадлежит отрезку [1;7],
# функция должна возбуждать исключение:
# ValueError('Аргумент не принадлежит требуемому диапазону')
# Примечание 1. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию get_weekday(), но не код, вызывающий ее.



def get_weekday(number):
    week = { 1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
    if not isinstance(number, int):
        raise TypeError('Аргумент не является целым числом')
    elif number < 1 or number > 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        return week[number]



try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))












