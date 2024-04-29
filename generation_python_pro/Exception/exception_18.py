# Назовем пароль хорошим, если:
#
# его длина равна
# 9
# 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.
#
# Формат входных данных
# На вход программе подается произвольное количество паролей, каждый на отдельной строке. Гарантируется, что среди них присутствует хороший.
#
# Формат выходных данных
# Для каждого введенного пароля программа должна вывести текст:
#
# LengthError, если длина введенного пароля меньше
# 9
# 9 символов
# LetterError, если в нем все буквы имеют одинаковый регистр либо отсутствуют
# DigitError, если в нем нет ни одной цифры
# Success!, если введенный пароль хороший
# После ввода хорошего пароля все последующие пароли должны игнорироваться.
#
# Примечание 1. Приоритет вывода сообщений об ошибке в случае невыполнения нескольких условий: LengthError, затем LetterError, а уже после DigitError.
#
# Примечание 2. Воспользуйтесь функцией is_good_password() из предыдущей задачи.

import sys

class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass



def is_good_password(string):
    if len(string) < 9:
        raise LengthError('LengthError')
    if all((any(i.islower() for i in string),  any(i.isupper() for i in string))) != string == string.lower() or string == string.upper():
        raise LetterError('LetterError')
    if string.isdigit() and not string.isalpha() or len(set('0123456789') & set(string)) == 0:
        raise DigitError('DigitError')
    else:
        return 'Success!'



for string in sys.stdin:
    try:
        print(is_good_password(string.strip()))
    except Exception as err:
        print(err)
    else:
        break

