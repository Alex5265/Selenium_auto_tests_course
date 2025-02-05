# Реализуйте функцию scrabble(), которая принимает два аргумента в следующем порядке:
#
# symbols — набор символов
# word — слово
# Функция должна возвращать True, если из набора символов symbols
# можно составить слово word, или False в противном случае.
#
# Примечание 1. При проверке учитывается количество символов,
# которые нужны для составления слова, и не учитывается их регистр.
#
# Примечание 2. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию scrabble(), но не код, вызывающий ее.
#
# Примечание 3. Тестовые данные доступны по ссылкам:
from collections import Counter


def scrabble(symbols, word):
    symbl_c = Counter(symbols.lower())
    word_c = Counter(word.lower())
    return symbl_c >= word_c


print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))




