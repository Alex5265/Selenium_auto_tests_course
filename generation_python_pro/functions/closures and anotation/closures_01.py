funcs = {'capitalize': str.capitalize,
         'swapcase': str.swapcase,
         'title': str.title,
         'lower': str.lower,
         'upper': str.upper}

sentence = 'This is the Best course TO study in the world!'

print(funcs['upper'](sentence))
print(funcs['swapcase'](sentence))
print(funcs['title'](sentence))




def func(name, language='Python', year=1992):
    '''какая-то функция что-то делает
    :param name: имя
    :param language: язык
    :param year: год
    :return: нон
    '''
    pass

print(func.__name__)          # имя функции
print(func.__doc__)           # строка документации
print(func.__defaults__)      # кортеж с аргументами по умолчанию






