# Задача: У вас есть глобальный счётчик global global_counter,
# который увеличивается асинхронными корутинами. Каждая корутина увеличивает
# значение счётчика на значение  = 2.39.
#
# В исходном коде корутины увеличивают глобальный счётчик без защиты от условий гонки,
# что приводит к некоректному результату из-за одновременного доступа к переменной global_counter.
#
#
#
# Ваша задача — модифицировать исходный код так, чтобы устранить проблему
# условий гонки с помощью асинхронного замка asyncio.Lock().
# Код должен вывести корректное значение global_counter.


import asyncio

global_counter = 0
# Создаем асинхронный замок для обеспечения безопасности
lock = asyncio.Lock()

async def increment():
    global global_counter
    # Используем асинхронный замок для обеспечения безопасности при обновлении
    async with lock:
        temp = global_counter
        await asyncio.sleep(.01)
        global_counter = temp + 2.39

async def main():
    await asyncio.gather(*[increment() for x in range(99)])

asyncio.run(main())
print(f"global_counter: {round(global_counter,2)}")













