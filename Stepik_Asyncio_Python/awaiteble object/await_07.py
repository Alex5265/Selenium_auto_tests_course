# Вы - начинающий Python-разработчик, и вам было поручено ускорить работу
# одной из сложных конкурентных систем вашей компании.
#
# Описание задачи:
# Расставьте ключевое слово await там, где это необходимо, чтобы код заработал;


# импортируем асинхроность
import asyncio

# перед заксыпанием на секунду ставим await
async def task1():
    await asyncio.sleep(1)
    print("Привет из корутины task1")

# тк же перед заксыпанием на секунду ставим await
async def task2():
    await asyncio.sleep(1)
    print("Привет из корутины task2")

# в основоной функции создаем конкурентность -
async def main():
    await asyncio.gather(task1(), task2())


asyncio.run(main())


