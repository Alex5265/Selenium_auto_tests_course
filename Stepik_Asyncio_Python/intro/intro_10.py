import asyncio
import time


async def coro(num, loop):
    start = time.time()
    print(f"Задача {num}: Начало работы")
    await asyncio.sleep(2.5 - num)
    print(f"Задача {num}: Завершение работы")
    return f"Задача {num} работала {time.time()-start:.3f} секунды"


async def main():
    loop = asyncio.get_running_loop()
    tasks = [asyncio.create_task(coro(i, loop)) for i in [1, 2]]
    # запуск всех задач в Event Loop
    result = await asyncio.gather(*tasks)
    print(*result, sep='\n')


asyncio.run(main())