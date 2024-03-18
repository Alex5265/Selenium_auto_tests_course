# Исходные данные: Имеется программа для симуляции снятия денег с банковского счета.
# Счет начинается с 10,000 рублей. В программе осуществляется 9 попыток снять сумму в 1200 рублей асинхронно.
# Из-за асинхронной природы операций снятия средств возникает проблема race condition,
# которая приводит к неправильному расчету оставшихся средств на счете.
#
# Цель: Улучшить стабильность и надёжность работы программы,
# управляющей банковскими транзакциями,
# путём решения проблемы с race condition.

import asyncio

# Инициализация банковского счета
bank_account = 10000
print(f"Исходный баланс: {bank_account}р")


async def withdraw_money(amount, lock):
    global bank_account
    async with lock:
        # Проверка наличия достаточных средств на счете
        print(f"Попытка снять {amount}р. Доступный баланс: {bank_account}р")

        if bank_account >= amount:
            await asyncio.sleep(0.01)  # Имитация долгой операции
            bank_account -= amount
            print(f"Снятие {amount}р успешно. Оставшийся баланс: {bank_account}р")
        else:
            print(f"Снятие {amount}р не удалось. Недостаточно средств. Оставшийся баланс: {bank_account}р")


async def main():
    lock = asyncio.Lock()
    tasks = [asyncio.create_task(withdraw_money(1200, lock)) for _ in range(9)]
    await asyncio.gather(*tasks)
    print(f'Конечный остаток средств: {bank_account}р')

asyncio.run(main())