# Распутайте цепочку корутин;
# Проанализируйте код ниже и определите точку входа в программу;
# Передайте корутину в метод asyncio.run(), которая является точкой входа.

import asyncio


async def coro_1():
    print("Вызываю корутину 0")


async def coro_5():
    print("Вызываю корутину 3")
    await coro_3()


async def coro_3():
    print("Вызываю корутину 2")
    await coro_2()


async def coro_4():
    print("Вызываю корутину 1")
    await coro_1()


async def coro_2():
    print("Вызываю корутину 4")
    await coro_4()


asyncio.run(coro_5())

