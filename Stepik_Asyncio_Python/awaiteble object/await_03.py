import asyncio

# что можно использовать с AWAIT
# -Асинхронные функции (коррутины)

async def async_function():
    # имитация асинхронной операции
    await asyncio.sleep(1)
    return "Результат асинхронной функции"

# использование await с асинхронной функцией
asyncio.run(async_function())


# Объекты Future - то специальный объект, представляющий
# отложенный результат асинхронной операции.
# Future можно ожидать, т.е. использовать с await

future = asyncio.Future()

# Предположим, какая-то функция устанавливает результат future
async def set_future_result():
    await asyncio.sleep(1)
    future.set_result("Результат Future")

# Можно использовать await с Future
result = await future
