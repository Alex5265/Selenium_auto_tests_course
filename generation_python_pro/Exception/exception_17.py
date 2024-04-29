# Назовем пароль хорошим, если
#
# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Реализуйте функцию is_good_password() в стиле EAFP, которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна возвращать True, если строка string представляет собой хороший пароль, или возбуждать исключение:
#
# LengthError, если его длина меньше
# 9
# 9 символов
# LetterError, если в нем отсутствуют буквы или все буквы имеют одинаковый регистр
# DigitError, если в нем нет ни одной цифры
# Примечание 1. Исключения LengthError, LetterError и DigitError уже определены и доступны.
#
# Примечание 2. Приоритет возбуждения исключений в случае невыполнения нескольких условий:
# LengthError, затем LetterError, а уже после DigitError.
#
# Примечание 3. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию is_good_password(), но не код, вызывающий ее.

class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass


def is_good_password(p: str) -> bool:
    try:
        p[8]
    except Exception:
        raise LengthError
    try:
        list(filter(str.isalpha, p))[0]
        list(filter(str.isupper, p))[0]
        list(filter(str.islower, p))[0]
    except Exception:
        raise LetterError
    try:
        list(filter(str.isdigit, p))[0]
    except Exception:
        raise DigitError
    return True












