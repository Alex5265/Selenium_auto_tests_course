# Создайте две корутины: coro_1() и coro_2().
# Каждая из корутин при вызове должна выводить своё уникальное приветственное сообщение.
# Корутины должны "поприветствовать" друг друга в своих сообщениях.
# Создайте корутину main(), в которой одновременно запустите обе корутины.
# Используйте функцию asyncio.run(), чтобы запустить корутину main().



import asyncio

async def coro_1():
    print('coro_1 says, hello coro_2!')

async def coro_2():
    print("coro_2 says, hello coro_1!")

async def main():
    await asyncio.gather(coro_1(), coro_2())

asyncio.run(main())