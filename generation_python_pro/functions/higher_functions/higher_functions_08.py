# Реализуйте функцию verification(), которая проверяет правильность введенного пароля. Она должна принимать четыре аргумента в следующем порядке:
#
# login — логин пользователя
# password — пароль пользователя
# success — некоторая функция
# failure — некоторая функция
# Пароль считается правильным, если в нем присутствует, хотя бы одна заглавная латинская буква, хотя бы одна строчная латинская буква и хотя бы одна цифра. Функция verification() должна вызывать функцию success() с аргументом login, если переданный пароль является правильным, иначе — функцию failure() с аргументами login и строкой-сообщением об ошибке:
#
# в пароле нет ни одной буквы, если в пароле отсутствуют латинские буквы
# в пароле нет ни одной заглавной буквы, если в пароле отсутствуют заглавные латинские буквы
# в пароле нет ни одной строчной буквы, если в пароле отсутствуют строчные латинские буквы
# в пароле нет ни одной цифры, если в пароле отсутствуют цифры
# Примечание 1. Если пароль не удовлетворяет нескольким условиям, то приоритеты выбора строки-сообщения об ошибке являются следующими:
#
# в пароле нет ни одной буквы
# в пароле нет ни одной заглавной буквы
# в пароле нет ни одной строчной буквы
# в пароле нет ни одной цифры
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию verification(), но не код, вызывающий ее.
import string


def verification(login, password, success, failure):
    d = {0: 'в пароле нет ни одной буквы',
         1: 'в пароле нет ни одной заглавной буквы',
         2: 'в пароле нет ни одной строчной буквы',
         3: 'в пароле нет ни одной цифры'}
    letter = any( i in string.ascii_letters for i in password)
    uppper = any(i.isupper() for i in password)
    lowwer = any(i in string.ascii_lowercase for i in password)
    digi = any(i.isdigit() for i in password)
    result = [letter, uppper, lowwer, digi]

    if all(result):
        return success(login)
    else:
        return failure(login, d[result.index(False)])



def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)



# сторонеерешение разобрал - красивое.

def verification(login, password, success, failure):
    vd = {(str.isalpha, str.isascii): 'в пароле нет ни одной буквы',
          (str.isascii, str.islower): 'в пароле нет ни одной строчной буквы',
          (str.isascii, str.isupper): 'в пароле нет ни одной заглавной буквы',
          (bool,        str.isdigit): 'в пароле нет ни одной цифры'}
    for f in vd:
        if not any(f[0](i) and f[1](i) for i in password):
            return failure(login, vd[f])
    success(login)






