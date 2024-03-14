import asyncio

async def my_coroutine():
    await asyncio.sleep(1)
    print("Задача выполнена")

async def main():
    task = asyncio.create_task(my_coroutine())

    await task

asyncio.run(main())