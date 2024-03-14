import asyncio
import random

async def boil_water(time: int):
    print('Ставим чайник с водой на плиту...')
    await asyncio.sleep(time)                               # Передаем управление плите
    print('Чайник закипел!')

async def chop_vegetables():
    print('Начинаем нарезать овощи...')
    await asyncio.sleep(random.randint(2, 4))               # Передаем управление нарезке овощей
    print('Овощи нарезаны!')

async def prepare_dinner():
    await asyncio.gather(boil_water(5), chop_vegetables())   # Запускаем задачи параллельно


asyncio.run(prepare_dinner())