import asyncio


# Корутина, которая дважды получает замок
async def task(lock):
    print('Задача пытается захватить замок...')

    # Захватываем замок
    async with lock:
        print('Задача снова пытается захватить замок...')

        # Снова захватываем замок
        # Повторный захват замка приведет к взаимной блокировке, так как замок уже занят той же задачей
        async with lock:
            # Сюда мы никогда не дойдем
            pass


async def main():
    # Создаем общий замок
    lock = asyncio.Lock()
    await task(lock)


asyncio.run(main())