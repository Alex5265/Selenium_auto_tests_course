# Создайте асинхронную функцию (корутину) с именем main(),
# которая при вызове выводит на экран сообщение:
# "Hello, Asyncio!"
# Используйте функцию asyncio.run(), чтобы запустить вашу корутину.


import asyncio

async def main():
    print('Hello,', end=' ')
    await asyncio.sleep(1)
    print('Asyncio')


asyncio.run(main())