import asyncio

global_counter = 0

async def increment():
    global global_counter
    temp = global_counter
    await asyncio.sleep(0.01)  # Имитация долгой операции
    global_counter = temp + 1

async def main():
    await asyncio.gather(increment(), increment())

asyncio.run(main())
print(f"global_counter: {global_counter}")