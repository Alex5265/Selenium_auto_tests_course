# Создайте корутину с названием print_with_delay, которая принимает один аргумент - целое число,
# и выводит его с интервалом в одну секунду.
#
# Coroutine 0 is done
# Coroutine 1 is done
# ...
# ...
# ...
# Coroutine 8 is done
# Coroutine 9 is done
# Используя только что созданную корутину, создайте 10 задач (tasks) для асинхронного выполнения.
# При создании каждой задачи передавайте в print_with_delay числа от 0 до 9.
#
# Запустите все созданные задачи последовательно, так, чтобы порядок вывода
# сообщений совпадал с переданными числами (от 0 до 9).

import asyncio

async def print_with_delay(n):
    await asyncio.sleep(1)
    print(f'Coroutine {n} is done')

async def main():
    tasks = [asyncio.create_task(print_with_delay(i)) for i in range(10)]

    await asyncio.gather(*tasks)

asyncio.run(main())