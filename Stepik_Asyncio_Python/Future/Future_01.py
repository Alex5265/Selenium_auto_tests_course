import asyncio

async def simulate_long_running_task(name, delay, future: asyncio.Future):
    """Асинхронная функция, имитирующая длительную задачу."""
    print(f"Задача '{name}' началась, будет выполнена за {delay} секунд.")
    await asyncio.sleep(delay)
    result = f'Результат задачи "{name}"'
    print(f"Задача '{name}' завершена.")
    if not future.done():
        future.set_result(result)


async def main():
    future = asyncio.Future()
    await simulate_long_running_task("Задача1", 3, future)

    result = future.result()
    print(f'Результат Future: {result}')


asyncio.run(main())