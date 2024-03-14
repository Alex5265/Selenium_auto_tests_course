import asyncio

async def task_one():
    await asyncio.sleep(2)
    return "Задача 1 завершена"

async def task_two():
    await asyncio.sleep(1)
    return "Задача 2 завершена"

async def main():
    result_one = await task_one()
    result_two = await task_two()
    print(result_one, result_two)

asyncio.run(main())