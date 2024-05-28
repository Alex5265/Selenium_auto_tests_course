# Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:
#
# language — код языка: ru — русский, en — английский
# Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:
#
# русского алфавита, если language имеет значение ru
# английского алфавита, если language имеет значение en
# Примечание 1. Буква ё в русском алфавите не учитывается.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Alphabet.


class Alphabet:
    def __init__(self, language):
        self.dict_lang = {'ru': range(ord('а'), ord('я') + 1),
                          'en': range(ord('a'), ord('z') + 1)}
        self.take_lang = language
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        self.index %= len(self.dict_lang[self.take_lang])
        return chr(self.dict_lang[self.take_lang][self.index])


ru_alpha = Alphabet('ru')

print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))

















