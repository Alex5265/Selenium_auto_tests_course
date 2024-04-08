# Реализуйте функцию is_correct_json(), которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна возвращать True, если строка string удовлетворяет формату JSON,
# или False в противном случае.
#
# Примечание 1. Вспомните про конструкцию try-except из урока.
#
# Примечание 2. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию is_correct_json(),
# но не код, вызывающий ее.
import json


def is_correct_json(string):
    try:
        js = json.loads(string)
    except json.decoder.JSONDecodeError:
        return False

    return True



print(is_correct_json('number = 17'))





