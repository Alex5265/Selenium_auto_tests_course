# Задачи на модуль рандом и стринг.
# Необходимо написать код, создающий генератор паролей n кол-во m длина
# состоящие из строчных и прописных букв и цифр,
# кроме тех. которые легко перепутать 'l' 'I' '1' 'o' 'O' '0'
# В каждом пароле обязательно должна присутствовать хотя бы одна цифра и буква в верхнем и нижнем регистре

import random
import string

def generate_password(length):
    answer = ''
    rnd_upper = random.randrange(1, length - 1)
    rnd_lower = random.randrange(1, length - rnd_upper)
    rnd_dig = length - rnd_upper - rnd_lower
    upper = ''.join((set(string.ascii_uppercase) - set('lI1oO0')))
    lower = ''.join((set(string.ascii_lowercase) - set('lI1oO0')))
    dig = ''.join((set(string.digits) - set('lI1oO0')))

    for i in range(rnd_upper):
        answer += random.choice(upper)
    for i in range(rnd_lower):
        answer += random.choice(lower)
    for i in range(rnd_dig):
        answer += random.choice(dig)

    answer = ''.join(random.sample(answer, len(answer)))
    return answer

def generate_passwords(count, length):
    answer = [generate_password(length) for _ in range(count)]
    return answer

n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')