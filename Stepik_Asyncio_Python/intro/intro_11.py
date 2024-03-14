import asyncio
import time

# Корутина для получения данных
async def fetch_data():
    print("Получение данных #1 ...")
    # Задержка, имитирующая запрос данных
    await asyncio.sleep(2)
    print("Данные #1 получены.")
    return {'data': 123}

# Корутина для получения данных
async def new_fetch_data():
    print("Получение данных #2...")
    # Задержка, имитирующая запрос данных
    await asyncio.sleep(2)
    print("Данные #2 получены.")
    return {'data': 321}

# Базовая корутина
async def process_data():
    # Создание задач по запросу данных
    tasks = [asyncio.create_task(coro) for coro in (fetch_data(), new_fetch_data())]
    print("Запрос данных...")
    data = await asyncio.gather(*tasks)
    # Обработка данных
    print(f"Данные обработаны: {data[0]['data'] + data[1]['data']}")


start = time.time()
asyncio.run(process_data())
print(f'Скрипт выполнен за {time.time() - start:.3f}')