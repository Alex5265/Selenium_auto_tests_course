import asyncio

async def main():
    print('Начинаем')
    await asyncio.sleep(1)
    print('Закончили')

asyncio.run(main())