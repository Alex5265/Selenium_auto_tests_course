# Функция ignore_command() принимает на вход один строковый аргумент
# command – команда, которую нужно проверить,и возвращает значение True,
# если в команде содержится подстрока из списка ignore и False – если нет.
# Перепишите функцию ignore_command(), чтобы она использовала
# встроенные функции all()/any(), сохранив при этом ее функционал.




# проверив несколько варинатов понял что удобнее именно игнорируемые слови искать
# в команде. И т.к. если любое слово надо игнорировать то используем any
def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update',
              'exec', 'del', 'truncate']
    return any(map(lambda word: word in command, ignore))



print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))

# ИЗначальная функция
# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#
#     for word in ignore:
#         if word in command:
#             return True
#     return False
#