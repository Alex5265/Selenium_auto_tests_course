import random
import sys

# проверяет введеное число. Необходимо чтобы было число и границах от 1 до макс числа от диапазона.
def is_valid(num, x):
    if num.isdigit() and 1 <= int(num) <= int(x):
        return True
    else:
        return False

# запрашивает число, проверяет на проверку, в цикле запрашивает коректные данные.
def inputing_valid_num(x):
    while True:
        write_num = input('число: ')
        if is_valid(write_num, x):
            return int(write_num)
        else:
            print(f"Необходимо вести целое число от 1 до {x}")


# проверяет Х, генерит случайное число, есть счетчик количества попыток, и в цикле происходит основное тело игры
# где сравниваются числа, выдается информация о больше меньше и ответ
def playing_compare(x):
    while True:
        if x.isdigit() and int(x) > 1:
            hidden_num = random.randint(1, int(x))
            count = 0
            print(f'угадайте число от 1 до {x}')
            while True:
                count += 1
                write_num = inputing_valid_num(x)
                if write_num > hidden_num:
                    print('Число меньше загаданного, попробуйте еще раз')
                elif write_num < hidden_num:
                    print('Число больше загаданного, попробуйте еще раз')
                else:
                    print(f'Вы угадали поздравляем! Количество попыток: {count}')
                    return False

        else:
            print("Просьба ввести число для диапазона")
            x = input('x = ')

# функция продолжения игры. в цикле запрашивает ввести д или н для продолжения или прекращения
def continiuator_game():
    ask = input("Хотите снова угадать число ('д' / 'н')? :" )
    while True:
        if ask not in ('д', 'н'):
            ask = input('Необходимо ввести только ("д" / "н") : ')
        elif ask in ('д'):
            return True
        else:
            print("Всего хорошего!")
            return False

# функция старта игры. запрашивается максимальный диапазон.уходит в функцию сравнения и затем в продолжения.
def starting_game():
    print('Добро пожаловать в числовую угадайку')
    while True:
        print('Укажите в каком диапазоне Вы готовы угадывать числа. От 1 до x?')
        x = input('x = ')
        playing_compare(x)
        if continiuator_game():
            continue
        else:
            sys.exit()


starting_game()
