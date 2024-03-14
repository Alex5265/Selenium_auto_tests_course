import asyncio

async def read_data_from_file(filename):
    print(f"Начинаем чтение из файла {filename}")

    await asyncio.sleep(2)
    print(f'Чтение из файла {filename} завершено')
    return f'данные из файла {filename}'

async def send_data_to_internet(data):
    print('Начинаем отправку данных в интернет')

    await asyncio.sleep(3)
    print("Отправка данных в интернет завершена")


async def main():
    filename = 'example.txt'

    file_data = await read_data_from_file(filename)
    
    await send_data_to_internet(file_data)

asyncio.run(main())