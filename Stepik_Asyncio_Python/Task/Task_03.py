# Ниже продемонстрирован плохой пример — создание задачи без сохранения ссылок,
# т. е. без создания переменных или списка задач.
# Код ниже хоть и запустится, но в других ситуациях задача может быть удалена сборщиком мусора.

import asyncio

async def my_task():
    print(f"{'-' * 10}\nRunning my task")
    await asyncio.sleep(1)
    print(f"Task complete\n{'-' * 10}")


async def main():
    # Создаем задачу без сохранения ссылки на нее
    asyncio.create_task(my_task())
    # Здесь произойдет запуск задачи, однако стоит помнить,
    # что эта задача может быть удалена сборщиком мусора в любой момент.
    await asyncio.sleep(2)

asyncio.run(main())


# В этом конкретном случае задача скорее всего будет выполнена,
# но такое поведение не гарантировано, в силу особенностей работы сборщика мусора Python.
#
# Пример создания task с сохранением ссылки на задачу:

import asyncio

async def my_task():
    print("Running my task")
    await asyncio.sleep(1)
    print("Task complete")

async def main():
    task = asyncio.create_task(my_task())
    await asyncio.sleep(2)

asyncio.run(main())