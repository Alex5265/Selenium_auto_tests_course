# Задачи на модуль рандом и стринг.
# Необходимо написать функцию, индекс латверии
# Правильный формат - LetterLetterNumber_NumberLetterLetter
# где Letter – заглавная буква английского алфавита, Number – число от 0 до 99(включая)
#

import random as r
import string

def generate_index():
    let = string.ascii_uppercase
    return f"{r.choice(let)}{r.choice(let)}{r.randrange(100)}_{r.randrange(100)}{r.choice(let)}{r.choice(let)}"


print(generate_index())

