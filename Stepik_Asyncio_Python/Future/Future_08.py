# решение предыдущей задачи по другому

import asyncio

fn_dict = {1: ('первая', lambda x: x + 1), 2: ('вторая', lambda x: x * 2),
           3: ('третья', lambda x: x + 3), 4: ('четвертая', lambda x: x ** 2)}


# Когда един в четырех лицах!)))
async def n_function(x, num):
    key, fn = fn_dict[num]
    print(f"Выполняется {key} функция с аргументом {x}")
    await asyncio.sleep(1)
    print(f"{key.capitalize()} функция завершилась с результатом {(result := fn(x))}")
    return result


async def main():
    x = 1
    print("Начало цепочки асинхронных вызовов")
    for i in range(1, len(fn_dict) + 1):
        x = await asyncio.ensure_future(n_function(x, i))
    print(f"Конечный результат цепочки вызовов: {x}")


asyncio.run(main())