# Задачи на модуль рандом и стринг.
# Необходимо написать код, создающий генератор паролей n кол-во m длина
# состоящие из строчных и прописных букв и цифр,
# кроме тех. которые легко перепутать 'l' 'I' '1' 'o' 'O' '0'
# В каждом пароле необязательно должна присутствовать хотя бы одна цифра и буква в верхнем и нижнем регистре

import string
import random

n, m = [ int(input()) for i in range(2)]


def generate_password(length):
    simbols = ''.join((set(string.ascii_letters) | set(string.digits)) - set('lI1oO0'))
    answer = ''
    for i in range(length):
        answer += random.choice(simbols)
    return answer

def generate_passwords(count, length):
    answer = [generate_password(length) for _ in range(count)]
    return answer



print(*generate_passwords(n, m), sep='\n')





