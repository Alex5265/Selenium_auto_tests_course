import time

start_time = time.time()

for i in range(5):
    print(i)
    time.sleep(0.1)

end_time = time.time()

elapsed_time = end_time - start_time
print(f'Время работы программы = {elapsed_time}')

import time

start_time = time.monotonic_ns()

for i in range(5):
    print(i)
    time.sleep(0.5)

end_time = time.monotonic_ns()

elapsed_time = end_time - start_time
print(f'Время работы программы = {elapsed_time}')

import time

start_time = time.perf_counter()

for i in range(5):
    print(i)
    time.sleep(0.5)

end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f'Время работы программы = {elapsed_time}')