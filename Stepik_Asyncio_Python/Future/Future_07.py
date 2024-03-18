import asyncio

async def first_function(x):
    print(f"Выполняется первая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 1
    print(f"Первая функция завершилась с результатом {result}")
    return result

async def second_function(x):
    print(f"Выполняется вторая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x * 2
    print(f"Вторая функция завершилась с результатом {result}")
    return result

async def third_function(x):
    print(f"Выполняется третья функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 3
    print(f"Третья функция завершилась с результатом {result}")
    return result

async def fourth_function(x):
    print(f"Выполняется четвертая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x ** 2
    print(f"Четвертая функция завершилась с результатом {result}")
    return result

async def main():
    print("Начало цепочки асинхронных вызовов")
    res1 = await asyncio.ensure_future(first_function(1))
    res2 = await asyncio.ensure_future(second_function(res1))
    res3 = await asyncio.ensure_future(third_function(res2))
    final_result = await asyncio.ensure_future(fourth_function(res3))

    print(f"Конечный результат цепочки вызовов: {final_result}")

asyncio.run(main())