import time

seconds = time.time_ns()    # получаем количество прошедших секунд в виде float числа
print('Количество секунд с начала эпохи =', seconds)

import time

seconds = 1630387918.354396
local_time = time.ctime(seconds)

print('Местное время:', local_time)

import time

local_time = time.ctime()              # вызов функции без аргумента
print('Местное время:', local_time)

import time

print('Before the sleep statement')
time.sleep(3)
print('After the sleep statement')

import time

for i in [0.7, 0.5, 1.0, 2.5, 3.3]:
    print(f'Waiting for {i} seconds')
    time.sleep(i)
print('The end')

print(sum([i for i in range(1, 11)]))