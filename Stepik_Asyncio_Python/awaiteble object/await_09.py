# Вам предоставлен код, который предполагает асинхронное выполнение вычислений,
# но, к сожалению, он был написан не полностью.
# Ваша задача - внимательно проанализировать код и восстановить его работоспособность,
# обеспечив асинхронное выполнение.
#
# Определите место для await:
#
# В коде пропущено ключевое слово await, которое необходимо для ожидания асинхронных операций.
# Вам нужно найти место, где его отсутствие мешает правильной работе программы.


import asyncio

async def compute_square(x):
    print(f"Вычисляем квадрат числа: {x}")
    await asyncio.sleep(1)  # Имитация длительной операции
    return x * x

async def main():
    results = [asyncio.create_task(compute_square(i)) for i in range(10)]
    completed, pending = await asyncio.wait(results)
    for task in completed:
        print(f"Результат: {task.result()}")

asyncio.run(main())