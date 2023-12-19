import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuations = '!#$%&*+-=?@^_'
chars = ''

def generate_pass(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

how_much_pass = int(input('Количество паролей для генерации: '))
len_pass = int(input('Длина одного пароля: '))
digits_need = input('Включать ли цифры?("да" если необходимо) ')
lowercase_letters_need = input('Включать ли прописные буквы?("да" если необходимо) ')
uppercase_letters_need = input('Включать ли строчные буквы?("да" если необходимо) ')
punctuations_need = input('Включать ли символы?("да" если необходимо) ')
undarstable_need = input('Исключать ли неоднозначные символы il1Lo0O?("да" если необходимо) ')

if digits_need == 'да':
    chars += digits
if lowercase_letters_need == 'да':
    chars += lowercase_letters
if uppercase_letters_need == 'да':
    chars += uppercase_letters
if punctuations_need == 'да':
    chars += punctuations
if undarstable_need == 'да':
    chars += 'il1Lo0O'

for _ in range(how_much_pass):
    print(generate_pass(len_pass, chars))