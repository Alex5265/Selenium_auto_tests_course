# Пример множественного создания task в цикле for.

import asyncio
import random

async def my_task(i):
    print(f"Запуск задачи {i}")
    await asyncio.sleep(random.randint(1,5))
    print(f"Задача {i} Завершена")

async def main():
    tasks = []
    for x in range(5):
        task = asyncio.create_task(my_task(x))
        tasks.append(task)
    await asyncio.gather(*tasks)

asyncio.run(main())