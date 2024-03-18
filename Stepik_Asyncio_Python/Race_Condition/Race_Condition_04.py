import asyncio

value = 0
lock = asyncio.Lock()

async def add():
    global value
    async with lock:
        current = value
        await asyncio.sleep(0.1)
        value = current + 1

async def main():
    await asyncio.gather(add(), add(), add())

asyncio.run(main())
print(value)